# 题目描述
> 小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!

# 输出描述
> 输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序

```java
import java.util.ArrayList;
public class Solution {
    public ArrayList<ArrayList<Integer> > FindContinuousSequence(int sum) {
        ArrayList<ArrayList<Integer> > ans = new ArrayList<ArrayList<Integer>>();
        int currSum = 0;
        boolean v[] = new boolean[sum+1];
        for (int i = 1, j = 1; i <= sum && j <= sum; ) {
            
            if (currSum == sum) {
                if (i-j >= 1) {
                    ArrayList<Integer> tmp = new ArrayList<>();
                    for(int k = j; k<=i; k++) {
                        if (v[k]) {
                            tmp.add(k);
                        }
                    }
                    ans.add(tmp);
                }
                currSum -= j;
                v[j] = false;
                j ++;
            } else if (currSum < sum) {
                currSum += i;
                v[i] = true;
                i ++;
            } else {
                currSum -= j;
                v[j] = false;
                j ++;
            }
        }
        
        return ans;
    }
}
```