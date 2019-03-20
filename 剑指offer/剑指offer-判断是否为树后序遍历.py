# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) == 0:
            return False
        if len(sequence) == 1:
            return True
        return self.judge(sequence, 0, len(sequence) - 1)

    def judge(self, s, start, end):
        if start >= end:
            return True
        i = start
        while s[i] < s[end]:  # 左子树小于根继续后移，大于根则为右子树
            i = i + 1
        for j in range(i, end):  # 左子树start->i-1，右子树i->end-1，根end
            if s[j] < s[end]:
                return False
        return self.judge(s, start, i - 1) and self.judge(s, i, end - 1)






