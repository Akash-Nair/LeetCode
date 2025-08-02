# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        in_map = {}
        for i in range(len(inorder)):
            in_map[inorder[i]] = i

        def create(pre_start,pre_end,in_start,in_end):
            if pre_start > pre_end:
                return None
            
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            in_index = in_map[root_val]

            left_size = in_index - in_start

            root.left = create(pre_start+1,pre_start+left_size,in_start,in_index-1)
            root.right = create(pre_start+left_size+1,pre_end,in_index+1,in_end)
            return root
        return create(0,len(preorder)-1,0,len(inorder)-1)
