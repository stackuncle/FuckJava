# 题目
> 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

# 思路1

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
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if(l1 == null) return l2;
        if(l2 == null) return l1;

        if(l1.val <= l2.val) {
            l1.next = mergeTwoLists(l1.next, l2);
            return l1;
        } else {
            l2.next = mergeTwoLists(l2.next, l1);
            return l2;
        }
    }
    
    public ListNode mergeKLists(ListNode[] lists) {
        if(lists == null || lists.length == 0) return null;
        
        ListNode ans = lists[0];
        for(int i = 1; i < lists.length; i++) {
            ans = mergeTwoLists(ans, lists[i]);
        }
        return ans;
    }
}
```

# 思路2

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
    public static ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null) return l2;
        if (l2 == null) return l1;
        
        ListNode res = null;
        if(l1.val < l2.val){
            res = l1;
            res.next = mergeTwoLists(l1.next, l2);
        } else {
            res = l2;
            res.next = mergeTwoLists(l1, l2.next);
        }
         
        return res;
    }
    
    public static ListNode solve(int low, int high, ListNode[] lists){
        if (low < high){
            int mid = (low + high)/2;
            ListNode a = solve(low, mid, lists);
            ListNode b = solve(mid+1, high, lists);
            
            return mergeTwoLists(a, b);
        }
        
        return lists[low];
    }
    
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null) return null;
        if (lists.length <= 0) return null;
        
        return solve(0, lists.length-1, lists);
    }
}

```