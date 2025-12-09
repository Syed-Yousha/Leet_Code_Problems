# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = [] #2d list
        path = []

        def traverse(node):
            if not node:
                return 

            path.append(str(node.val))

            if not node.left and not node.right:
                res.append('->'.join(path))
                path.pop()
                return

            traverse(node.left)
            traverse(node.right)
            path.pop()

        traverse(root)
        return res


            


# Time: O(N)
# Space: O(H)
# this is the optimal solution