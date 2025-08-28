# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
    def same_tree(p,q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return same_tree(p.left, q.left) and same_tree(p.right, q.right)
    def dfs(p, q):
        if not p:
            return  False
        same = same_tree(p,q)
        if same:
            return True
        return dfs(p.left, q) or dfs(p.right,q)
    result = dfs(root, subRoot)
    return result

