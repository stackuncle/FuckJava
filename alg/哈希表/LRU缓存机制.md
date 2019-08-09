# 题目描述
> 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。

> 获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。

>写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。

## 进阶:

> 你是否可以在 O(1) 时间复杂度内完成这两种操作？


```java
public class LRUCache<K, V> extends LinkedHashMap<K, V> {
    private final int MAX_CACHE_SIZE;

    public LRUCache2(int cacheSize) {
        super((int) Math.ceil(cacheSize / 0.75) + 1, 0.75f, true);
        MAX_CACHE_SIZE = cacheSize;
    }

    @Override
    protected boolean removeEldestEntry(Map.Entry eldest) {
        return size() > MAX_CACHE_SIZE;
    }
 }
```


```java
class LRUCache {
  public class LRUNode {
    int key;
    int val;
    LRUNode prev;
    LRUNode next;

    LRUNode(int key, int val) {
      this.key = key;
      this.val = val;
    }
  }

  private int capacity;
  private HashMap<Integer, LRUNode> map;
  private LRUNode head;
  private LRUNode tail;
  
  LRUCache(int capacity) {
    this.capacity = capacity;
    map = new HashMap<>();
  }

  public int get(int key) {
    LRUNode node = map.get(key);
    if (node == null) {
      return -1;
    }
    remove(node, false);
    setHead(node);
    return node.val;
  }

  public void put(int key, int value) {
    LRUNode node = map.get(key);
    if (node == null) {
      node = new LRUNode(key, value);
      if (map.size() >= capacity) {
        remove(tail, true);
      }
      map.put(key, node);
      setHead(node);
    } else {
      node.val = value;
      remove(node, false);
      setHead(node);
    }
  }

  public void setHead(LRUNode node) {
    if (head != null) {
      node.next = head;
      head.prev = node;
    }
    head = node;
    if (tail == null) {
      tail = node;
    }
  }

  public void remove(LRUNode node, boolean flag) {
    if (node.prev != null) {
      node.prev.next = node.next;
    } else {
      head = node.next;
    }
    if (node.next != null) {
      node.next.prev = node.prev;
    } else {
      tail = node.prev;
    }
    node.next = null;
    node.prev = null;
    if (flag) {
      map.remove(node.key);
    }
  }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
```