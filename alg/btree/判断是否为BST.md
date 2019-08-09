> 请实现一个函数，检查一棵二叉树是否为二叉查找树。
  
> 给定树的根结点指针TreeNode* root，请返回一个bool，代表该树是否为二叉查找树。


```java
import java.util.*;

/*
public class TreeNode {
    int val = 0;
    TreeNode left = null;
    TreeNode right = null;
    public TreeNode(int val) {
        this.val = val;
    }
}*/
public class Checker {
    private TreeNode last;
    
    public boolean checkBST(TreeNode root) {
        // write code here
        if(root == null) return true;
        boolean l  = checkBST(root.left);
        if(!l) return false;
        if(last != null) {
            if(last.val > root.val) return false;
        }
        last = root;
        boolean r = checkBST(root.right);
        if(!r) return false;
        return true;
    }
}
```