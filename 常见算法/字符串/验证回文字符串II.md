> 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

```java
class Solution {
    public boolean validPalindrome(String s) {
        int len = s.length();
        int i = 0;
        int j = len -1;
        char a[] = s.toCharArray();
        while(i <= j) {
            if(a[i] != a[j]) {
                return isPalindrome(a, i, j-1) || isPalindrome(a, i+1, j);
            }
            i++;
            j--;
        }
        return true;
        
    }
    
    
    public boolean isPalindrome(char a[], int i, int j) {
        while(i < j) {
            if(a[i] != a[j]) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
}
```