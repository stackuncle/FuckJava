# 题目描述
> 给定一棵二叉搜索树，请找出其中的第k小的结点。

> 例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。


```java
/*
public class TreeNode {
    int val = 0;
    TreeNode left = null;
    TreeNode right = null;

    public TreeNode(int val) {
        this.val = val;

    }

}
*/
public class Solution {
    public static int K = 0;
    public TreeNode inOrder(TreeNode node) {
        TreeNode target = null;
        if (node.left != null) {
            target = inOrder(node.left);
        }
        
        if (target == null) {
            if (K == 1) {
                target = node;
                return target;
            }
            K --;
        }
        
        if (target == null && node.right != null) {
            target = inOrder(node.right);
        }
        return target;
    }
    
    TreeNode KthNode(TreeNode pRoot, int k)
    {
        K = k;
        if (pRoot == null || K <= 0) return null;
        return inOrder(pRoot);
    }

}
```