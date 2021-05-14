# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 头节点可能被删除
        p = ListNode(0, head)
        point = p
        index = head
        for i in range(n):
            index = index.next
        while index:
            point = point.next
            index = index.next
        point.next = point.next.next
        
        return p.next
