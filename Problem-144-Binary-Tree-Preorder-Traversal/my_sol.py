class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        stack = [root] 
        output = []

        while stack:
            node = stack.pop() # get the last node added to the stack
            output.append(node.val) 

            if node.right: # push right child first so that left child is processed first
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return output

#time complexity: O(n)
#Space complexity: O(n) in worst case (skewed tree)
# this is an optimal iterative solution for preorder traversal of a binary tree 