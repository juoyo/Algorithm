# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
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
    def travel(self):
        if not self:
            exit(0)
        print("遍历：")
        p = self.head
        while p:
            print(p.val)
            p = p.next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        new_list = ListNode(0)
        pre = new_list
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next
        if l1 is not None:
            pre.next = l1
        else:
            pre.next = l2
        return new_list.next
data1 = [1, 2, 4]
data2 = [1, 3, 4]
L1 = LinkList()
L1.initList(data1)
L1.travel()
L2 = LinkList()
L2.initList(data2)
L2.travel()

s = Solution()
print(s.mergeTwoLists(L1, L2))