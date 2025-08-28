#https://leetcode.com/problems/symmetric-tree/?envType=problem-list-v2&envId=breadth-first-search
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def isSymmetric( root: TreeNode) -> bool:
    def dfs(p: TreeNode|None, q: TreeNode|None) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return dfs(p.left, q.right) and dfs(p.right, q.left)
    def bfs(p: TreeNode|None, q: TreeNode|None) -> bool:
        dq = deque([(p,q)])
        while dq:
            node1, node2 = dq.popleft()

            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            dq.append((node1.left, node2.right))
            dq.append((node1.right, node2.left))
        return True
    return bfs(root.left, root.right)



node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(2)
node.left.left = TreeNode(3)
node.left.right = TreeNode(4)
node.right.left = TreeNode(4)
node.right.right = TreeNode(3)
node.left.left.left = TreeNode(5)
print(isSymmetric(node))
        