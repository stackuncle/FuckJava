# 描述

> 给定一个整数序列，找到最长上升子序列（LIS），返回LIS的长度。

```java
public class Solution {
    /*
     * @param nums: An integer array
     * @return: The length of LIS (longest increasing subsequence)
     */
    public int longestIncreasingSubsequence(int[] nums) {
        // write your code here
        int N = nums.length;
        int[] dp = new int[N];
        int ans = 0;
        
        for(int i=0; i<N; ++i) {
            dp[i] = 1;
            for(int j=0; j<i; ++j) {
                if(nums[i]>nums[j] && dp[j]+1 > dp[i]) {
                    dp[i] = dp[j] +1;
                }
            }
            
            ans = Math.max(ans, dp[i]);
        }
        
        return ans;
    }
}
```