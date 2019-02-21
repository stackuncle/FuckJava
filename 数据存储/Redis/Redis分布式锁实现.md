> Jedis分布式锁

```java
public class JedisLock {
  private final MifiRedisClient client;
  private final String lockKey;
  private final int expireTime;
  private final int waitTime;
  private boolean locked = false;

  public JedisLock(MifiRedisClient client, String lockKey, int expireTime, int waitTime) {
    this.client = client;
    this.lockKey = lockKey;
    this.expireTime = expireTime;
    this.waitTime = waitTime;
  }

  public synchronized boolean lock() throws InterruptedException {
    int timeout = this.waitTime;

    while(timeout >= 0) {
      long expires = System.currentTimeMillis() + (long)this.expireTime + 1L;
      String expiresStr = String.valueOf(expires);
      if(this.client.setNx(this.lockKey, expiresStr)) {
        this.locked = true;
        return true;
      }

      String currentValueStr = this.client.get(this.lockKey);
      if(currentValueStr != null && Long.parseLong(currentValueStr) < System.currentTimeMillis()) {
        String oldValueStr = this.client.getSet(this.lockKey, expiresStr);
        if(oldValueStr != null && oldValueStr.equals(currentValueStr)) {
          this.locked = true;
          return true;
        }
      }

      timeout -= 50;
      Thread.sleep(50L);
    }

    return false;
  }

  public synchronized void unlock() {
    if(this.locked) {
      this.client.delKey(this.lockKey);
      this.locked = false;
    }

  }
}

```