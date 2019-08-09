# 题目描述
> 给定一个可包含重复数字的序列，返回所有不重复的全排列。

```java
class Solution {
    public static List<List<Integer>> ans = new ArrayList<List<Integer>>();
    public static int []path = new int[100];
    public static boolean []visit = new boolean[100];
    public static HashSet<String> set = new HashSet();
    
    public void solve(int idx, int[] nums){
        if (idx >= nums.length){
            List<Integer> tmp = new ArrayList<Integer>();
            StringBuffer sb = new StringBuffer();
            for (int i=0; i<nums.length; i++){
                tmp.add(nums[path[i]]);
                sb.append(nums[path[i]]);
            }
            
            if(!set.contains(sb.toString())) {
                ans.add(tmp);
                set.add(sb.toString());
            }
            return;
        }
        
        for (int i = 0; i<nums.length; i++){
            if (visit[i] == false){
                path[idx] = i;
                visit[i] = true;
                solve(idx+1, nums);
                visit[i] = false;
            }
        }
    }

    public List<List<Integer>> permuteUnique(int[] nums) {
        ans.clear();
        set.clear();
        // Arrays.sort(nums);
        solve(0, nums);
        return ans;
    }
}
```