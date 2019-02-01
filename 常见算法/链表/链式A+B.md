# 题目描述
> 有两个用链表表示的整数，每个结点包含一个数位。这些数位是反向存放的，也就是个位排在链表的首部。编写函数对这两个整数求和，并用链表形式返回结果。
 
> 给定两个链表ListNode* A，ListNode* B，请返回A+B的结果(ListNode*)。

> 例子： {1,2,3},{3,2,1} 返回：{4,4,4}

```java
import java.util.*;
/*
public class ListNode {
    int val;
    ListNode next = null;

    ListNode(int val) {
        this.val = val;
    }
}*/
public class Plus {
    public ListNode plusAB(ListNode a, ListNode b) {
        // write code here
        if (a == null) return b;
        if (b == null) return a;
        
        ListNode node = new ListNode(-1);
        ListNode res = node;
        int next = 0;
        while (a != null || b != null) {
            int curr = 0;
            if (a == null) {
                curr = next + b.val;
                b = b.next;
            } else if (b == null) {
                curr = next + a.val;
                a = a.next;
            } else {
                curr = next + a.val + b.val;
                a = a.next;
                b = b.next;
            }
            
            next = curr >= 10 ? 1 : 0;
            curr = curr % 10;
            node.next = new ListNode(curr);
            node = node.next;
        }
        
        if (next > 0) {
            node.next = new ListNode(next);
        }
        return res.next;
    }
}
```