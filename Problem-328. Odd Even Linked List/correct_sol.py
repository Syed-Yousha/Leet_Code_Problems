# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even
        while even and even.next:

            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = even_head
        return head

# Time Complexity: O(n)
# Space Complexity: O(1)
# in this solution I am using two pointers to keep track of the odd and even nodes,
#  which is optimal.