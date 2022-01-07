# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:  
        if not p and not q:
            return True
        
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

        ## DFS
        #stack = [(p, q)]

        #while stack:
        #    p, q = stack.pop()

        #    if not p and not q:
        #        continue
        #    elif None in [p, q]:
        #        return False
        #    else:
        #        if p.val != q.val:
        #            return False
        #        stack.append((p.right, q.right))
        #        stack.append((p.left, q.left))

        #    return True

        ## BFS
        #queue = [(p, q)]

        #while queue:
        #    p, q = queue.pop(0)

        #    if not p and not q:
        #        continue
        #    elif None in [p, q]:
        #        return False
        #    else:
        #        if p.val != q.val:
        #            return False
        #        queue.append((p.left, q.left))
        #        queue.append((p.right, q.right))

        #    return True


