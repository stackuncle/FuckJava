# 题目描述
n皇后问题是将n个皇后放置在n*n的棋盘上，皇后彼此之间不能相互攻击。

给定一个整数n，返回所有不同的n皇后问题的解决方案。

每个解决方案包含一个明确的n皇后放置布局，其中“Q”和“.”分别表示一个女王和一个空位置。

```java
public class Solution {
    /*
     * @param n: The number of queens
     * @return: All distinct solutions
     */
     
    public static List<List<String>> ans = new ArrayList<List<String>>();
    public static int[] path = new int[100];
    public static boolean[] row = new boolean[100];
    public static boolean[] lineL = new boolean[100];
    public static boolean[] lineR = new boolean[100];
    
    public static void dfs(int idx, int n) {
        if(idx >= n) {
            // record
            List<String> tmp = new ArrayList<String>();
            for(int i=0; i<n; i++) {
                String s = "";
                for(int j=0; j<n; j++) {
                    if(j == path[i]) {
                        s += "Q";
                    } else {
                        s += ".";
                    }
                }
                tmp.add(s);
            }
            
            ans.add(tmp);
            return;
        }
        
        // 一列上最多只有一个皇后, 以idx为col的搜索次序
        for(int i=0; i<n; i++) {
            if(row[i] || lineL[idx+i] || lineR[(idx-i+n-1)]) continue;
            
            row[i] = true;
            lineL[idx + i] = true;
            lineR[(idx-i+n-1)] = true;
            
            path[idx] = i;
            dfs(idx+1, n);
            
            row[i] = false;
            lineL[idx + i] = false;
            lineR[(idx-i+n-1)] = false;
        }
    }
    
    public List<List<String>> solveNQueens(int n) {
        ans.clear();
        dfs(0, n);
        return ans;
    }
}
```