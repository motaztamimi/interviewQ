# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
def invertTree(self, root: TreeNode):
    #DFS
    if not root:
        return None
    root.right, root.left = root.left, root.right
    self.invertTree(root.right)
    self.invertTree(root.left)
    
    return root 

    #BFS
    if not root:
        return None
    dq = deque([root])

    while dq:
        node = dq.popleft()
        if not node:
            continue
        node.left, node.right = node.right, node.left

        dq.append(node.left)
        dq.append(node.right)
    return root

            