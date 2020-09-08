# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

    
class Solution:
    def solve(self,root,s,total):
        if not root:
            s = s[:-1]
            return
        s += str(root.val)

        if not root.left and not root.right:
            total[0] += int(s,2)
            s = s[:-1]
            return
        self.solve(root.left,s,total)
        self.solve(root.right,s,total)
    
    def sumRootToLeaf(self, root: TreeNode) -> int:
        s = ''
        total = [0]
        self.solve(root,s,total)
        
        return total[0]
        
        
