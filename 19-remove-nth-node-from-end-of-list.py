from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def nodeRemove(head):
            if not head:
                return head, 0
            head.next, count = nodeRemove(head.next)
            return (head, head.next)[count+1==n], count+1
        return nodeRemove(head)[0]


        # count = 0

        # def nodeCount(head_cur, count):
        #     if head_cur is not None:
        #         _, count = nodeCount(head_cur.next, count)
        #         count += 1

        #         if count-1 == n:
        #             head_cur.next = head_cur.next.next if head_cur.next.next else None
        #         return head_cur, count
        #     else:
        #         return None, count

        # head, count = nodeCount(head, count)

        # if count == n:
        #     head = head.next

        # return head

