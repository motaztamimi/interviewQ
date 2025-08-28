#https://leetcode.com/problems/same-tree/description/?envType=problem-list-v2&envId=breadth-first-search

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
def isSameTreeBfs(p: TreeNode| None, q: TreeNode|None)-> bool:
    # BFS approach
    dq = deque([(p, q)])
    while dq:
        node1, node2 = dq.popleft()
        if not node1 and not node2:
            continue
        if not node1 or not node2:
            return False
        if node1.val != node2.val:
            return False
        dq.append((node1.left, node2.left))
        dq.append((node1.right, node2.right))
    return True

def isSameTreeDfs(p: TreeNode| None, q: TreeNode|None)-> bool:
    # DFS approach
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return isSameTreeDfs(p.left, q.left) and isSameTreeDfs(p.right, q.right)