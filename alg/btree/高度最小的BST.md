# 题目描述
> 对于一个元素各不相同且按升序排列的有序序列，请编写一个算法，创建一棵高度最小的二叉查找树。

> 给定一个有序序列int[] vals,请返回创建的二叉查找树的高度。

```java
import java.util.*;

public class MinimalBST {
    public TreeNode buildTree(int []vals, int i, int j) {
        if(i > j) return null;
        int mid = (i + j)/2;
        TreeNode node = new TreeNode(vals[mid]);
        node.left = buildTree(vals, i, mid - 1);
        node.right = buildTree(vals, mid + 1, j);
        
        return node;
    }
    
    public int getHeight(TreeNode node) {
        if(node == null) return 0;
        return Math.max(getHeight(node.left), getHeight(node.right)) + 1;
    }
    
    public int buildMinimalBST(int[] vals) {
        // write code here
        if(vals == null || vals.length == 0) return 0;
        TreeNode root = buildTree(vals, 0, vals.length -1);
        return getHeight(root);
    }
}

```