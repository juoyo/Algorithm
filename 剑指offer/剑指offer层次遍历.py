# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        list = []  # 存储层次遍历结果
        queue = []
        queue.append(root)
        while len(queue):
            p = queue.pop(0)  # 队列中弹出队首
            list.append(p.val)  # 队首节点值存入输入列表
            if p.left:  # 出队结点左孩子不空，左孩子入队
                queue.append(p.left)
            if p.right:
                queue.append(p.right)
        return list








