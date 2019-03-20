# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        length = len(array)
        for i in range(0, len(array)):
            if array[i] % 2 == 1:
                i = i + 1
            else:  # 第一个偶数
                for j in range(i + 1, len(array)):
                    if array[j] % 2 == 0:
                        j = j + 1
                    else:  # 第一个奇数
                        x = array[j]
                        for k in range(j, i, -1):
                            array[k] = array[k - 1]
                        array[i] = x
                        break
        return array

s = Solution()
list = s.reOrderArray([1,2,3,4,5,6,7])
print(list)




