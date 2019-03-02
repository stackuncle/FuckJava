# 题目描述
> 求两个数组的交集。数组可能存在重复数字。

```python
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d1 = dict()
        for n in nums1:
            d1[n] = d1.get(n, 0) + 1
        
        d2 = dict()
        for n in nums2:
            d2[n] = d2.get(n, 0) + 1
            
        ans = []
        for k in d1.keys():
            if k in d2:
                for x in range(min(d1[k], d2[k])):
                    ans.append(k)
        return ans
```