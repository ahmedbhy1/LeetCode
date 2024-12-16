# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        d = dict()
        np = dict()
    
        def dfs(node: TreeNode,i : int):
            if node == None:
                return
            np[node.val] = i 
            test = False
            if (node.left):
                d[node.left.val] = node.val
                test = True
                dfs(node.left,i+1)
            if (node.right != None):
                d[node.right.val] = node.val
                test = True
                dfs(node.right,i+1)
            if (test == False):
                return

        dfs(root,0)
        
        i = np[p.val]
        j = np[q.val]

        a = p.val
        b = q.val
        
        while i>=0 and j>=0:
            if (i==j):
                if (a == b): 
                    tr = TreeNode(a)
                    return tr
                i-=1
                j-=1
                a = d[a]
                b = d[b] 
                continue
            if (i<j):
                j-=1
                b = d[b]
                continue
            if (i>j):
                i-=1
                a = d[a]
                continue