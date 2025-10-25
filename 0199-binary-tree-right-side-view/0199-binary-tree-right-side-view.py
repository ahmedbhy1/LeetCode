# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        L = []
        
        def dfs(root: Optional[TreeNode],deapth=2,penality = 0):

            if root == None :
                return
            L.append((deapth,penality,root.val))
            dfs(root.left, deapth + 1, penality + 2 ** (20-deapth) )
            dfs(root.right, deapth + 1, penality)
        
        
        dfs(root)
        L.sort()
        print(L)
        I = []
        depth = set()
        for i in L:
            if i[0] in depth:
                continue
            depth.add(i[0])
            I.append(i[2])
        return I