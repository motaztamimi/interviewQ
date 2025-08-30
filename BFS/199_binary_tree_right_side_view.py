# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque 
def rightSideView(self, root: TreeNode) -> int:
    if not root:
        return []

    dq = deque([root])
    right_view = []
    while dq:

        level = []
        for _ in range(len(dq)):
            node = dq.popleft()
            level.append(node)

            if node.right:
                dq.append(node.right)
            if node.left:
                dq.append(node.left)
        right_view.append(level[0].val)
    return right_view