# 题目描述
> 输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。


```java
import java.util.ArrayList;
public class Solution {
    public int binarySearch(int []a, int target) {
        int l = 0, r = a.length - 1;
        while(l <= r) {
            int mid = (l + r) /2;
            if (a[mid] == target) {
                return mid;
            } else if(a[mid] < target) {
                l = mid + 1;
            } else {
                r = mid -1;
            }
        }
        
        return -1;
    }
    
    public ArrayList<Integer> FindNumbersWithSum(int [] array,int sum) {
        ArrayList<Integer> ans = new ArrayList<>();
        
        int first = 0, second = array.length;
        for (int i = 0; i < array.length/2; i++) {
            int t = sum - array[i];
            int idx = binarySearch(array, t);
            if (idx == -1) {
                continue;
            } else {
                ans.add(array[i]);
                ans.add(t);
                break;
            }
        }
        
        return ans;
    }
}
```