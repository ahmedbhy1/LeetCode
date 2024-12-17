# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        sums=[]
        def dfs(root: Optional[TreeNode]) -> int:
            if root == None :
                return 0
            print(root.val)
            l = dfs(root.left)
            r = dfs(root.right)
            somme =  root.val + l + r 
            sums.append(somme)
            return somme
        dfs(root)

        counter = Counter(sums)
        maxx_count = counter.most_common(1)[0][1]
        l = [items for items,count in counter.items() if count==maxx_count]
        
        return l