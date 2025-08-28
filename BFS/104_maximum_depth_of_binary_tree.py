from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepthBFS(self, root: TreeNode) -> int:
        #BFS approach
        if not root:
            return 0
        dq = deque([root])
        levels = 0

        while dq:

            for _ in range(len(dq)):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            levels+=1
        return levels


def maxDepthDFS(root: TreeNode) -> int:
    #DFS approach 
    def dfs(p, level):
        if not p:
            return level
        return max(dfs(p.left, level+1) , dfs(p.right, level+1)) 

    if not root:
        return 0
    return dfs(root,0)