# 题目描述
> 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

```java
public class Solution {
    public int JumpFloor(int target) {
        int a = 0, b = 1, c;
        for(int i = 1; i <= target; i++) {
            c = a + b;
            a = b;
            b = c;
        }
        
        return b;
    }
}
```

# 题目描述
> 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

```java
public class Solution {
    public int JumpFloorII(int target) {
        return 1 << (target - 1);
    }
}
```