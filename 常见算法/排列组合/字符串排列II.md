# 题目描述
> 给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

> 换句话说，第一个字符串的排列之一是第二个字符串的子串。


```java
class Solution {
    public boolean check(String x, String y) {
        int[] count = new int[256];
        for(int i = 0; i < x.length(); i++) {
            count[x.charAt(i)] ++;
        }
        
        for(int i = 0; i < y.length(); i++) {
            if((--count[y.charAt(i)]) < 0) return false;
        }
        
        return true;
    }
    public boolean checkInclusion(String s1, String s2) {
        if(s2 == null) return false;
        if(s2.length() < s1.length()) return false;
        
        int len1 = s1.length();
        for(int i = 0; i <= s2.length() - len1; i++) {
            String curr = s2.substring(i, i+len1);
            if(check(curr, s1)) {
                return true;
            }
        }
        
        return false;
    }
}
```