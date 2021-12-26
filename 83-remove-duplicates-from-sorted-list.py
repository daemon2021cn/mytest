# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        node_cur = head
        while node_cur.next:
            if node_cur.val == node_cur.next.val:
                node_cur.next = node_cur.next.next
            else:
                node_cur = node_cur.next

        return head 

