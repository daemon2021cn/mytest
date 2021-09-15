from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2

        #if not (l1 and l2):
        #    return l1 or l2

        #l_node = ListNode()
        #l3 = l_node
        #while l1 and l2:
        #    if l1.val < l2.val:
        #        l3.val = l1.val
        #        l1 = l1.next
        #    else:
        #        l3.val = l2.val
        #        l2 = l2.next
        #    if l1 and l2:
        #        l3.next = ListNode()
        #        l3 = l3.next
        #if l1 or l2:
        #    l3.next = l1 or l2
        #return l_node

def print_node(node):
    print(node.val)
    if node.next is not None:
        print_node(node.next)

newClass = Solution()

num1 = [1,2,4]
num2 = [1,3,4]

def add_node(num1):
    node1 = ListNode(num1.pop(0))
    if num1:
        node1.next = add_node(num1)
    return node1

node_1 = add_node(num1) if num1 else []

node_2 = add_node(num2) if num2 else []

result = newClass.mergeTwoLists(node_1, node_2)
print_node(result)
