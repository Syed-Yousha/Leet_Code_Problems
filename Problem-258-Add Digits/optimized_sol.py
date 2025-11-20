class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + (num - 1) % 9
#Time Complexity: O(1)
#Space Complexity: O(1)