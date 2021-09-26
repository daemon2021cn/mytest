from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        def swapNodes(head):
            if not head or not head.next:
                return head

            head_pre, head_pre_2next = head, head.next.next
            head = head.next
            head.next, head.next.next = head_pre, head_pre_2next

            head.next.next = swapNodes(head.next.next)
            return head

        return swapNodes(head)
