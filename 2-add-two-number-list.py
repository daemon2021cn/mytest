from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        carry = 0
        l3 = result

        while l1 or l2 or carry:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next

            if val > 9:
                l3.val = val%10
                carry = 1
            else:
                l3.val = val
                carry = 0

            if l1 or l2 or carry:
                l3.next = ListNode()
                l3 = l3.next

        return result

#class Solution:
#    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#        num_sum = 0
#        node = l1
#        i = 0
#        while node:
#            num_sum += node.val * (10**i)
#            node = node.next
#            i+=1
#
#        node = l2
#        i = 0
#        while node:
#            num_sum += node.val * (10**i)
#            node = node.next
#            i+=1
#
#        def add_node(num, node=None):
#            node = ListNode()
#            node.val = num%10
#            num = num//10
#            if num>0:
#                node.next = add_node(num, node.next)
#            return node
#
#        node = add_node(num_sum)
#
#        return node

def print_node(node):
    print(node.val)
    if node.next is not None:
        print_node(node.next)

newClass = Solution()

num1 = [2,4,3]
num2 = [5,6,4]

def add_node(num1):
    node1 = ListNode(num1.pop(0))
    if num1:
        node1.next = add_node(num1)
    return node1

node_1 = add_node(num1)

node_2 = add_node(num2)

result = newClass.addTwoNumbers(node_1, node_2)
print_node(result)
