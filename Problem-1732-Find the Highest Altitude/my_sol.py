class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        alt = []
 
        alt.append(0)
        for i in range(1, n+1):
            alt.append(alt[i-1] + gain[i-1])
            
        return max(alt)       

# Time Complexity: O(n)
# Space Complexity: O(n)

        