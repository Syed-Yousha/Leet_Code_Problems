class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')

        for item in nums:

            if item <= first:
                first = item
            elif item <= second:
                second = item
            else:
                    return True
            
        
        return False
            


# Time complexity: O(n)
# Space complexity: O(1)
# Approach: Greedy
# This is the optimal approach.