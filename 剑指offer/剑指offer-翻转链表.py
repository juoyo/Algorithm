# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None
class LinkList:
    def __init__(self):
        self.head = None
    def initList(self, data): #data为列表
        self.head = ListNode(data[0])
        p = self.head
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        list = []
        while pHead:
            list.append(pHead)
            pHead = pHead.next
        return list[::-1]

data = [1,2,3,4,5]
linklist = LinkList()
linklist.initList(data)
print(linklist.head.val)
print(linklist.head.next)
s = Solution()
print(s.ReverseList(linklist.head))