# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ans = []
        parent = {}
        q = deque()
        visited = {}

        q.append(root)
        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()

                if node.left:
                    parent[node.left.val] = node
                    q.append(node.left)
                if node.right:
                    parent[node.right.val] = node
                    q.append(node.right)
        
        q.append(target)
        while k > 0 and q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                visited[node.val] = 1

                if node.left and node.left.val not in visited:
                    q.append(node.left)
                if node.right and node.right.val not in visited:
                    q.append(node.right)

                if node.val in parent and parent[node.val].val not in visited:
                    q.append(parent[node.val])
            k-=1
        
        while q:
            ans.append(q.popleft().val)

        return ans
