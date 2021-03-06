# MySql事务

## 事务
事务是一组不可被分割执行的SQL语句集合，如果有必要，可以撤销。银行转账是经典的解释事务的例子。用户A给用户B转账5000元主要步骤可以概括为如下两步。 
    第一，账户A账户减去5000元； 
    第二，账户B账户增加5000元； 
这两步要么成功，要么全不成功，否则都会导致数据不一致。这就可以用到事务来保证，如果是不同银行之间的转账还需要用到分布式事务。


## 事务ACID
![事务的特性](https://user-gold-cdn.xitu.io/2018/5/20/1637b08b98619455?w=312&h=305&f=png&s=22430)

- 原子性（Autmic）：构成事务的的所有操作必须是一个逻辑单元，要么全部执行，要么全部不执行。 

- 一致性（Consistency）：数据库在事务执行前后状态都必须是稳定的。

- 隔离性（Isolation）：并发访问数据库时，一个用户的事物不被其他事物所干扰，各并发事务之间数据库是独立的；

- 持久性（Durability）：一个事务被提交之后。它对数据库中数据的改变是持久的，即使数据库 发生故障也不应该对其有任何影响。
   

## 事务隔离
事务的隔离用是通过锁机制实现的，不同于MyISAM使用表级别的锁，InnoDB采用更细粒度的行级别锁，提高了数据表的性能。

InnoDB的锁通过锁定索引来实现，如果查询条件中有主键则锁定主键，如果有索引则先锁定对应索引然后再锁定对应的主键（可能造成死锁），如果连索引都没有则会锁定整个数据表。

## MVCC
多版本并发控制是指InnoDB存储引擎通过行多版本的方式来读取当前执行时间数据库中的行数据，简单说就是读不加锁，读写不冲突。这样会极大的增加数据库的并发性能。有人问了，读不加锁，那么写会加锁的啊，这个时候再同时进行读能正常读取吗，答案是肯定的，读取操作不会因为锁没释放而等待，而是会去读取行的一个快照数据（不同事务的隔离级别，访问的快照数据不同）。

针对可能的问题，InnoDB提供了四种不同级别的机制保证数据隔离性。

　　
## 事务隔离级别
- **READ_UNCOMMITTED（未授权读取）:** 最低的隔离级别，允许读取尚未提交的数据变更，**可能会导致脏读、幻读或不可重复读**

- **READ_COMMITTED（授权读取）:** 	允许读取并发事务已经提交的数据，**可以阻止脏读，但是幻读或不可重复读仍有可能发生**

- **REPEATABLE_READ（可重复读）:** 	对同一字段的多次读取结果都是一致的，除非数据是被本身事务自己所修改，**可以阻止脏读和不可重复读，但幻读仍有可能发生。**

- **SERIALIZABLE（串行）:** 	最高的隔离级别，完全服从ACID的隔离级别。所有的事务依次逐个执行，这样事务之间就完全不可能产生干扰，也就是说，**该级别可以防止脏读、不可重复读以及幻读**。但是这将严重影响程序的性能。通常情况下也不会用到该级别。

### read uncommitted
`READ UNCOMMITTED`允许某个事务看到其他事务并没有提交的数据。可能会导致脏读、不可重复读、幻读。 
原理：`READ UNCOMMITTED`不会采用任何锁。
 
### read committed

`READ COMMIT`允许某个事务看到其他事务已经提交的数据。可能会导致不可重复读和幻读。 
原理：数据的读是不加锁的，但是数据的写入、修改、删除加锁，避免了脏读。
 
### repeatable read
可以重复读取，但有幻读。

原理：数据的读、写都会加锁，当前事务如果占据了锁，其他事务必须等待本次事务提交完成释放锁后才能对相同的数据行进行操作。读取的数据行不可写，但是可以往表中新增数据。
在MySQL中，其他事务新增的数据，看不到，不会产生幻读。采用多版本并发控制（MVCC）机制解决幻读问题。
 
### serializable
可读，不可写。SERIALIZABLE 级别在InnoDB中和REPEATABLE READ采用相同的实现。像java中的锁，写数据必须等待另一个事务结束。

其中，Read Uncommitted 和 Serializable 比较极端，前一个可以读取未提交的记录，后一个读写冲突，并发性低，所以两者在一般情况下都不建议使用，用的最多是RC和RR。


这里需要注意的是：**Mysql 默认采用的 REPEATABLE_READ隔离级别 Oracle 默认采用的 READ_COMMITTED隔离级别.**

事务隔离机制的实现基于锁机制和并发调度。其中并发调度使用的是MVVC（多版本并发控制），通过保存修改的旧版本信息来支持并发一致性读和回滚等特性。

详细内容可以参考:[可能是最漂亮的Spring事务管理详解](https://blog.csdn.net/qq_34337272/article/details/80394121)

# 参考
- [《高性能MySql》](https://s.click.taobao.com/6e2O6Lw)