# 题目描述
> 输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。

## 思路1： 利用快排partition
```java
import java.util.*;

public class Solution {
    void swap(int[] a, int x, int y) {
        int tmp = a[x];
        a[x] = a[y];
        a[y] = tmp;
    }
    
    int partition(int[] arr, int left, int right) {
        int p = arr[left];
        while(left < right) {
            while(left < right && arr[right] > p) right--;
            if(left<right) swap(arr, left, right);
            while(left < right && arr[left] <= p) left++;
            if(left<right) swap(arr, left, right);
        }
        return left;
    }
    
    public ArrayList<Integer> GetLeastNumbers_Solution(int [] input, int k) {
        ArrayList<Integer> ans = new ArrayList<>();
        if(input == null || k <=0 || k > input.length) return ans;
        
        int start = 0;
        int end = input.length - 1;
        int p = partition(input, start, end);
        while(p != k-1) {
            if(p < k-1) {
                start = p+1;
                p = partition(input, start, end);
            } else {
                end = p-1;
                p = partition(input, start, end);
            }
        }
        
        
        for(int i=0; i<k; i++) {
            ans.add(input[i]);
        }
        return ans;
    }
}
```

## 思路2： 利用优先队列

```java
import java.util.*;

public class Solution {
 
    public ArrayList<Integer> GetLeastNumbers_Solution(int [] input, int k) {
        ArrayList<Integer> ans = new ArrayList<Integer>();
        if (input.length == 0 || k <= 0 || k > input.length) return ans;
        
        PriorityQueue<Integer> pq = new PriorityQueue<>(k);
        for (int i = 0; i < input.length; i++) {
            pq.add(input[i]);
        }
        
        for(int i =0 ; i < k; i++) {
            ans.add(pq.poll());
        }
        
        return ans;
    }
}
```