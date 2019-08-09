# 题目描述
> 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

```
class Solution {
    public void swap(int[] nums, int x, int y) {
        int tmp = nums[x];
        nums[x] = nums[y];
        nums[y] = tmp;
    }
    
    public int partition(int[] nums, int l, int r) {
        int p = nums[l];
        while(l < r) {
            while(l<r && nums[r] < p) r--;
            if(l<r) swap(nums, l, r);
            while(l<r && nums[l] >= p) l++;
            if(l<r) swap(nums, l, r);
        }
        return l;
    }
    
    public int findKthLargest(int[] nums, int k) {
        int start = 0;
        int end = nums.length-1;
        int p = partition(nums, start, end);
        // int x = nums.length - k;
        while(p != k-1) {
            if(p > k-1) {
                end = p-1;
                p = partition(nums, start, end);
            } else {
                start = p+1;
                p = partition(nums, start, end);
            }
        }
        return nums[p];
    }
}
```
