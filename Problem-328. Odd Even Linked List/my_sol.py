# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        odd = []
        even = []
        count = 1
        tmp = head

        while tmp:

            if count%2 != 0:
                odd.append(tmp.val)
            else:
                even.append(tmp.val)
            
            tmp = tmp.next
            count += 1
        
        
        tmp = head
        for item in odd:
            tmp.val = item 
            tmp = tmp.next
        
        for item in even:
            tmp.val = item 
            tmp = tmp.next
        
        return head

        
# Time Complexity: O(n)
# Space Complexity: O(n)
# in this solution I am using two extra lists to store the odd and even values, which is not optimal.
#  The space complexity is O(n) because of the extra space used for the lists.