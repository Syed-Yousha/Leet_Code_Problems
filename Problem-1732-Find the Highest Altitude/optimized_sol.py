class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current = 0
        maximum = 0

        for g in gain:
            current += g
            maximum = max(maximum, current)

        return maximum
    
# Time Complexity: O(n)
# Space Complexity: O(1)
