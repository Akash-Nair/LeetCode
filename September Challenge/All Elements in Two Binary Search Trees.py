# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from sortedcontainers import SortedList
class Solution:
    def inorder(self,root,ans):
        if root == None:
            return
        self.inorder(root.left,ans)
        ans.add(root.val)
        self.inorder(root.right,ans)
        
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        ans = SortedList()
        self.inorder(root1,ans)
        self.inorder(root2,ans)
        return ans
        
        
