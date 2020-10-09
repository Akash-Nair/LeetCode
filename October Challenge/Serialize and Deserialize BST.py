# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:         
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ''
        
        q = deque()
        s = []
        q.append(root)
        
        while q:
            node = q.popleft()
            if node != 'null':
                s.append(str(node.val))
                if node.left:
                    q.append(node.left)
                else:
                    q.append('null')
                
                if node.right:
                    q.append(node.right)
                else:
                    q.append('null')
            else:
                s.append('null')
        #print(s)
        return str(s)
            
                
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return []
        
        visited = [0]*len(data)
        data = eval(data)
        
        for i in range(len(data)-1,-1,-1):
            if data[i] != 'null':
                data = data[:i+1]
                break 
        #print(data)
        
        q = deque()
        i = 0
        root = TreeNode(data[i])
        q.append(root)
        
        while q:
            node = q.popleft()
            try:
                node.left = TreeNode(data[2*i+1])
                q.append(node.left)
            except:
                pass
            
            try:
                node.right = TreeNode(data[2*i+2])
                q.append(node.right)
            except:
                pass
            i += 1
                        
        return root
        
            
        
        
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
