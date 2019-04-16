# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        l=1
        h=2
        list = []
        result = []
        while l<h:
            cursum = (l+h)*(h-l+1)/2
            #print(l, h, cursum)
            if cursum == tsum:
                for i in range(l, h+1, 1):
                    list.append(i)
                result.extend([list])
                list = []
                l = l+1
            elif cursum < tsum:
                h = h+1
            else:
                l = l+1
        return result

s = Solution()
print(s.FindContinuousSequence(100))


