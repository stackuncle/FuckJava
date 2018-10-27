```java
public class Solution {
    public int reverse(int x) {
        if (x == 0) return 0;
        if (x < 0) return -reverse(-x);
        
        int res = 0;
        while (x > 0) {
            int left = x % 10;
            res = res * 10 + left;
            x = (x - left) / 10;
        }
        
        return res;
    }
}
```