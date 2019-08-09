# 题目描述

给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

```java
class Solution {
    public int jump(int[] nums) {
        if(nums == null || nums.length <= 1) return 0;
        
        int N = nums.length;
        int ans = 0;
        int curr = 0;
        int last = 0;
        
        for(int i = 0; i < N; i++) {
            curr = Math.max(curr, i + nums[i]);
            if(i == last) {
                last = curr;
                ans++;
                if (curr >= N - 1) break;
            }
        }
        return ans;
    }
}
```