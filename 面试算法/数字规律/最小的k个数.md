# 题目描述
> 输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。


## 思路1： 利用快排partition
代码略。

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