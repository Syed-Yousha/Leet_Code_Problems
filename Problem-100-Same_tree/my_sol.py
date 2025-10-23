from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            node1 = q1.popleft()
            node2 = q2.popleft()

            # If one is None and other not
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False

            # Check value
            if node1.val != node2.val:
                return False

            # Add children to queues
            q1.append(node1.left)
            q1.append(node1.right)
            q2.append(node2.left)
            q2.append(node2.right)

        return not q1 and not q2



# time and space complexity: O(n)