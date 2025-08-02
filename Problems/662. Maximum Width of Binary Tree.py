# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        di = defaultdict(list)
        self.res = 0 

        def dfs(root,level,column):
            if root:
                di[level].append(column)
                width = di[level][-1] - di[level][0]
                self.res = max(self.res,width)
                dfs(root.left,level+1,column*2)
                dfs(root.right,level+1,column*2+1)

        dfs(root,0,0)
        return self.res+1
        
