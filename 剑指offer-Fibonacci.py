# -*- coding:utf-8 -*-
import time
class Solution:
    def Fibonacci(self, n):
        # write code here
        list = []
        list.extend([0, 1, 1])
        for i in range(3, 40):
            list.append(list[i-1] + list[i-2])
        return list[n]
starttime = time.time()
s = Solution()
endtime = time.time()
print(s.Fibonacci(39))
print(endtime-starttime)







