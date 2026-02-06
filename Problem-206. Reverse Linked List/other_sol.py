class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None:
            return head

        new_head = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return new_head

# Time Complexity: O(n)
# Space Complexity: O(n) due to recursive stack space
