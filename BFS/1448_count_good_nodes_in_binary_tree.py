# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def goodNodes(self, root: TreeNode) -> int:
    def dfs(p, max_value):
        if not p:
            return 0
        good = 1 if p.val >= max_value else 0
        curr_max = max(p.val, max_value)
        return good + dfs(p.left, curr_max) + dfs(p.right, curr_max)
    return dfs(root, root.val) if root else 0
    