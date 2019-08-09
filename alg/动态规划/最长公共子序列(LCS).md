# 描述

> 给出两个字符串，找到最长公共子序列(LCS)，返回LCS的长度。

```java
public class Solution {
    /**
     * @param A: A string
     * @param B: A string
     * @return: The length of longest common subsequence of A and B
     */
    public int longestCommonSubsequence(String A, String B) {
        // write your code here
        if(A == null || B == null) return 0;
        int M = A.length();
        int N = B.length();
        int[][] dp = new int[M+1][N+1];
        
        for(int i = 0; i<M; i++) {
            for(int j = 0; j<N; j++) {
                if(A.charAt(i) == B.charAt(j)) {
                    dp[i+1][j+1] = dp[i][j] + 1;
                } else {
                    dp[i+1][j+1] = Math.max(dp[i+1][j], dp[i][j+1]);
                }
            }
        }
        
        return dp[M][N];
    }
}
```