## Redis中key的的过期时间
通过EXPIRE key seconds命令来设置数据的过期时间。返回1表明设置成功，返回0表明key不存在或者不能成功设置过期时间。在key上设置了过期时间后key将在指定的秒数后被自动删除。被指定了过期时间的key在Redis中被称为是不稳定的。

当key被DEL命令删除或者被SET、GETSET命令重置后与之关联的过期时间会被清除

## Redis过期键删除策略
Redis key过期的方式有三种：

- 被动删除：当读/写一个已经过期的key时，会触发惰性删除策略，直接删除掉这个过期key
- 主动删除：由于惰性删除策略无法保证冷数据被及时删掉，所以Redis会定期主动淘汰一批已过期的key
- 当前已用内存超过maxmemory限定时，触发主动清理策略

### 被动删除
只有key被操作时(如GET)，REDIS才会被动检查该key是否过期，如果过期则删除之并且返回NIL。

1. 这种删除策略对CPU是友好的，删除操作只有在不得不的情况下才会进行，不会其他的expire key上浪费无谓的CPU时间。

2. 但是这种策略对内存不友好，一个key已经过期，但是在它被操作之前不会被删除，仍然占据内存空间。如果有大量的过期键存在但是又很少被访问到，那会造成大量的内存空间浪费。expireIfNeeded(redisDb *db, robj *key)函数位于src/db.c。

但仅是这样是不够的，因为可能存在一些key永远不会被再次访问到，这些设置了过期时间的key也是需要在过期后被删除的，我们甚至可以将这种情况看作是一种内存泄露----无用的垃圾数据占用了大量的内存，而服务器却不会自己去释放它们，这对于运行状态非常依赖于内存的Redis服务器来说，肯定不是一个好消息


### 主动删除(定时删除)
先说一下时间事件，对于持续运行的服务器来说， 服务器需要定期对自身的资源和状态进行必要的检查和整理， 从而让服务器维持在一个健康稳定的状态， 这类操作被统称为常规操作（cron job）

在 Redis 中， 常规操作由 redis.c/serverCron 实现， 它主要执行以下操作：
- 更新服务器的各类统计信息，比如时间、内存占用、数据库占用情况等。
- 清理数据库中的过期键值对。
- 对不合理的数据库进行大小调整。
- 关闭和清理连接失效的客户端。
- 尝试进行 AOF 或 RDB 持久化操作。
- 如果服务器是主节点的话，对附属节点进行定期同步。
- 如果处于集群模式的话，对集群进行定期同步和连接测试。

Redis 将 serverCron 作为时间事件来运行， 从而确保它每隔一段时间就会自动运行一次， 又因为 serverCron 需要在 Redis 服务器运行期间一直定期运行， 所以它是一个循环时间事件： serverCron 会一直定期执行，直到服务器关闭为止。

在 Redis 2.6 版本中， 程序规定 serverCron 每秒运行 10 次， 平均每 100 毫秒运行一次。 从 Redis 2.8 开始， 用户可以通过修改 hz选项来调整 serverCron 的每秒执行次数， 具体信息请参考 redis.conf 文件中关于 hz 选项的说明

也叫定时删除，这里的“定期”指的是Redis定期触发的清理策略，由位于src/redis.c的activeExpireCycle(void)函数来完成。

serverCron是由redis的事件框架驱动的定位任务，这个定时任务中会调用activeExpireCycle函数，针对每个db在限制的时间REDIS_EXPIRELOOKUPS_TIME_LIMIT内迟可能多的删除过期key，之所以要限制时间是为了防止过长时间 的阻塞影响redis的正常运行。这种主动删除策略弥补了被动删除策略在内存上的不友好。

因此，Redis会周期性的随机测试一批设置了过期时间的key并进行处理。测试到的已过期的key将被删除。典型的方式为,Redis每秒做10次如下的步骤：

随机测试100个设置了过期时间的key
删除所有发现的已过期的key
若删除的key超过25个则重复步骤1
这是一个基于概率的简单算法，基本的假设是抽出的样本能够代表整个key空间，redis持续清理过期的数据直至将要过期的key的百分比降到了25%以下。这也意味着在任何给定的时刻已经过期但仍占据着内存空间的key的量最多为每秒的写操作量除以4.

Redis-3.0.0中的默认值是10，代表每秒钟调用10次后台任务。 

除了主动淘汰的频率外，Redis对每次淘汰任务执行的最大时长也有一个限定，这样保证了每次主动淘汰不会过多阻塞应用请求，以下是这个限定计算公式：

```
#define ACTIVE_EXPIRE_CYCLE_SLOW_TIME_PERC 25 /* CPU max % for keys collection */ 
... 
timelimit = 1000000*ACTIVE_EXPIRE_CYCLE_SLOW_TIME_PERC/server.hz/100;
```

hz调大将会提高Redis主动淘汰的频率，如果你的Redis存储中包含很多冷数据占用内存过大的话，可以考虑将这个值调大，但Redis作者建议这个值不要超过100。我们实际线上将这个值调大到100，观察到CPU会增加2%左右，但对冷数据的内存释放速度确实有明显的提高（通过观察keyspace个数和used_memory大小）。 

可以看出timelimit和server.hz是一个倒数的关系，也就是说hz配置越大，timelimit就越小。换句话说是每秒钟期望的主动淘汰频率越高，则每次淘汰最长占用时间就越短。这里每秒钟的最长淘汰占用时间是固定的250ms（1000000*ACTIVE_EXPIRE_CYCLE_SLOW_TIME_PERC/100），而淘汰频率和每次淘汰的最长时间是通过hz参数控制的。 

从以上的分析看，当redis中的过期key比率没有超过25%之前，提高hz可以明显提高扫描key的最小个数。假设hz为10，则一秒内最少扫描200个key（一秒调用10次*每次最少随机取出20个key），如果hz改为100，则一秒内最少扫描2000个key；另一方面，如果过期key比率超过25%，则扫描key的个数无上限，但是cpu时间每秒钟最多占用250ms。 

当REDIS运行在主从模式时，只有主结点才会执行上述这两种过期删除策略，然后把删除操作”del key”同步到从结点。


### maxmemory
当前已用内存超过maxmemory限定时，触发主动清理策略
- volatile-lru：只对设置了过期时间的key进行LRU（默认值）
- allkeys-lru ： 删除lru算法的key
- volatile-random：随机删除即将过期key
- allkeys-random：随机删除
- volatile-ttl ： 删除即将过期的
- noeviction ： 永不过期，返回错误当mem_used内存已经超过maxmemory的设定，对于所有的读写请求，都会触发redis.c/freeMemoryIfNeeded(void)函数以清理超出的内存。注意这个清理过程是阻塞的，直到清理出足够的内存空间。所以如果在达到maxmemory并且调用方还在不断写入的情况下，可能会反复触发主动清理策略，导致请求会有一定的延迟。 

当mem_used内存已经超过maxmemory的设定，对于所有的读写请求，都会触发redis.c/freeMemoryIfNeeded(void)函数以清理超出的内存。注意这个清理过程是阻塞的，直到清理出足够的内存空间。所以如果在达到maxmemory并且调用方还在不断写入的情况下，可能会反复触发主动清理策略，导致请求会有一定的延迟。

清理时会根据用户配置的maxmemory-policy来做适当的清理（一般是LRU或TTL），这里的LRU或TTL策略并不是针对redis的所有key，而是以配置文件中的maxmemory-samples个key作为样本池进行抽样清理。

maxmemory-samples在redis-3.0.0中的默认配置为5，如果增加，会提高LRU或TTL的精准度，redis作者测试的结果是当这个配置为10时已经非常接近全量LRU的精准度了，并且增加maxmemory-samples会导致在主动清理时消耗更多的CPU时间，建议：

尽量不要触发maxmemory，最好在mem_used内存占用达到maxmemory的一定比例后，需要考虑调大hz以加快淘汰，或者进行集群扩容。
如果能够控制住内存，则可以不用修改maxmemory-samples配置；如果Redis本身就作为LRU cache服务（这种服务一般长时间处于maxmemory状态，由Redis自动做LRU淘汰），可以适当调大maxmemory-samples。

## Replication link和AOF文件中的过期处理
为了获得正确的行为而不至于导致一致性问题，当一个key过期时DEL操作将被记录在AOF文件并传递到所有相关的slave。也即过期删除操作统一在master实例中进行并向下传递，而不是各salve各自掌控。这样一来便不会出现数据不一致的情形。当slave连接到master后并不能立即清理已过期的key（需要等待由master传递过来的DEL操作），slave仍需对数据集中的过期状态进行管理维护以便于在slave被提升为master会能像master一样独立的进行过期处理。

# 参考
- [关于Redis数据过期策略](https://www.cnblogs.com/chenpingzhao/p/5022467.html)