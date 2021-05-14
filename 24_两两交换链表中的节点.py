# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        dummy = ListNode()
        dummy.next = head
        temp = dummy
        while temp.next and temp.next.next:
            p = temp.next
            q = p.next
            temp.next = q
            p.next = q.next
            q.next = p
            temp = p
        return dummy.next