# 题目描述
> 在未排序的数组中找到第 k 个最大的元素。

> 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

## 思路1
对数组排序

```java
class Solution {
    public int findKthLargest(int[] nums, int k) {
        Arrays.sort(nums);
        return nums[nums.length - k];
    }
}
```

## 思路2
利用优先队列

```java
class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int i = 0; i < nums.length; i++) {
            pq.add(nums[i]);
            if(pq.size() > k) {
                pq.poll();
            }
        }
        return pq.peek();
    }
}
```

## 思路3
利用快排partition

```java

```