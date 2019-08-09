# 题目描述
> 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

## 示例:
> 输入: "25525511135"

> 输出: ["255.255.11.135", "255.255.111.35"]

```java
class Solution {
    LinkedList<String> path = new LinkedList<>();
    List<String> ans = new ArrayList<>();
    HashSet<String> set = new HashSet<>();
    
    public boolean isValid(String str) {
        if(str.charAt(0) == '0' && str.length() > 1) return false;
        
        int val = Integer.valueOf(str);
        return val >=0 && val <= 255;
    }
    
    public void search(String s, int idx) {
        if(path.size() > 4) return;
        
        if(idx == s.length()) {
            if(path.size() != 4) return;
            
            StringBuilder sb = new StringBuilder();
            int i = 0;
            for(String str: path) {
                sb.insert(0, str);
                if(i < 3) {
                    sb.insert(0, ".");
                }
                i++;
            }
            String ip = sb.toString();
            if(set.contains(ip)) return;
            set.add(ip);
            ans.add(ip);
            return;
        }
        
        for(int i=idx+1; i<=idx+3 && i<=s.length(); i++) {
            String sub = s.substring(idx, i);
            if(isValid(sub)) {
                path.push(sub);
                search(s, i);
                path.pop();
            }
        }
    }
    
    public List<String> restoreIpAddresses(String s) {
        ans.clear();
        path.clear();
        set.clear();
        search(s, 0);
        return ans;
    }
}
```