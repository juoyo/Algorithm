# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys

sys.setrecursionlimit(1000000)


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:  # 两树有一空，则返回false
            return False
        # 返回2是否是1，1的左子树，1的右子树的子结构
        return self.isSubtree(pRoot1, pRoot2) or self.isSubtree(pRoot1.left, pRoot2) or self.isSubtree(pRoot1.right,
                                                                                                       pRoot2)

    def isSubtree(self, A, B):
        if not B:  # B遍历完均匹配，则B是A的子结构
            return True
        if not A:  # A比B先遍历完，则B不是A的子结构
            return False
        if A.val != B.val:  # A。B有一个未匹配，则B不是A的子结构
            return False
        # 根已匹配，继续匹配两树的左右子树
        return self.isSubtree(A.left, B.left) and self.isSubtree(A.right, B.right)

