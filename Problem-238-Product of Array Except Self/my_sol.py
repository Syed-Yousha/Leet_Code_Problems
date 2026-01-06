class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)

        left = [1] * size
        for i in range(1, size):
                left[i] = left[i-1] * nums[i-1]

        right = [1] * size
        for i in range(size - 2, -1, -1):
                right[i] = right[i+1] * nums[i+1]


        output = [1] * size 
        for i in range(size):
            output =  left[i] * right[i]
        
        return output


# Time Complexity: O(N)
# Space Complexity: O(N)