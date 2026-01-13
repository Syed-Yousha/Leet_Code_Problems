class Solution:
    def maxArea(self, height: List[int]) -> int:
        right = len(height) - 1
        sum = 0
        max = -99999
        left = 0
         
        while left < right:
            sum =  min(height[left], height[right]) * (right - left)
            if max < sum:
                max = sum
            
            if height[right] > height[left]:
                left = left + 1
            else:
                right = right - 1

        
        return max
                
#time complexity: O(n)
#space complexity: O(1)