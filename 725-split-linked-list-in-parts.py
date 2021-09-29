from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        count, num = 0, 0
        ret = []

        def addPart(head_cur, k, count, ret):
            if head_cur:
                count += 1
                num, ret = addPart(head_cur.next, k, count, ret)

                if num == 0:
                    head_cur.next = None
                    if count > 0:
                        num = count//(k-len(ret))

                if num-1 == 0:
                    ret.append(head_cur)
                num -= 1
            else:
                tmp = k - count
                num = 1 if tmp>0 else count//(k-len(ret))
                while tmp>0:
                    ret.append([])
                    tmp -= 1

            return num, ret

        _, ret = addPart(head, k, count, ret)

        return ret[::-1]


