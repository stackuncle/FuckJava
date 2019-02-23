# 题目描述
> 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

```
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = dict()
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
                
        vals = sorted(d.values())
        kth = vals[-k]
        return [k for k,v in d.items() if d[k]>=kth]
        
```
