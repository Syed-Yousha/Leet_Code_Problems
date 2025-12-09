# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        res = []

        def dfs(node, path):
            # Build the current path string
            if path:
                path += "->" + str(node.val)
            else:
                path = str(node.val)

            # If leaf node, save path
            if not node.left and not node.right:
                res.append(path)
                return

            # Recurse on children
            if node.left:
                dfs(node.left, path)
            if node.right:
                dfs(node.right, path)

        dfs(root, "")
        return res
    
# Time: O(N)

# Space: O(H + L * H)
# H for recursion stack
# L * H for storing all root-to-leaf paths in res
