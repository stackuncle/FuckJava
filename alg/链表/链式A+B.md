# 题目描述
> 有两个用链表表示的整数，每个结点包含一个数位。这些数位是反向存放的，也就是个位排在链表的首部。编写函数对这两个整数求和，并用链表形式返回结果。
 
> 给定两个链表ListNode* A，ListNode* B，请返回A+B的结果(ListNode*)。

> 例子： {1,2,3},{3,2,1} 返回：{4,4,4}

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        if(l1 == null) return l2;
        if(l2 == null) return l1;
        
        ListNode p1 = l1;
        ListNode p2 = l2;
        ListNode ans = null, curr = null;
        int carry = 0;
        while(p1 != null && p2 != null) {
            int sum = p1.val + p2.val + carry;
            int val = sum%10;
            carry = (sum -val)/10;
            if(ans == null) {
                ans = curr = new ListNode(val);
            } else {
                curr.next = new ListNode(val);
                curr = curr.next;
            }
            p1 = p1.next;
            p2 = p2.next;
        }
        
        while(p1 != null) {
            int sum = p1.val + carry;
            int val = sum%10;
            carry = (sum -val)/10;
            curr.next = new ListNode(val);
            curr = curr.next;
            p1 = p1.next;
        }
        
        while(p2 != null) {
            int sum = p2.val + carry;
            int val = sum%10;
            carry = (sum -val)/10;
            curr.next = new ListNode(val);
            curr = curr.next;
            p2 = p2.next;
        }
        
        if(carry > 0) curr.next = new ListNode(carry);
        return ans;
    }
}
```