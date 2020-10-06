# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root,val):
        if not root:
            return
        if val < root.val:
            if root.left:
                self.inorder(root.left,val)
            else:
                root.left = TreeNode(val=val)
        else:
            if root.right:
                self.inorder(root.right,val)
            else:
                root.right = TreeNode(val=val)
        
        
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        temp = root
        
        if not temp:
            root = TreeNode(val=val)
            
        self.inorder(temp,val)
        return root
        
        
