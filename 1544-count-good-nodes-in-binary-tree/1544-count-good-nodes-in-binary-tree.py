# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    nb_good = 0
    def goodNodes(self, root: TreeNode, maxx=-999999999) -> int:
        if root == None:
            return 0


        if root.val >= maxx :
            self.nb_good += 1
            maxx = root.val

        l = self.goodNodes(root.left,maxx)
        r = self.goodNodes(root.right,maxx)
        
        return self.nb_good