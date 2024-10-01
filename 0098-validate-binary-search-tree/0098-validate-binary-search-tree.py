# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode], minn = -9999999999999, maxx=9999999999999) -> bool:
        if root == None :
            return True
        
        if root.val <= minn or root.val >= maxx :
            return False
        
        l = self.isValidBST(root.left, minn = minn ,maxx = root.val)
        r = self.isValidBST(root.right, minn = root.val ,maxx = maxx)

        return l and r

        

        