class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1 

# time complexity: O(n)
# space complexity: O(1)
# The idea is to use two pointers, one for the current position of the non-zero element and the other 
# for the current position of the zero element. We iterate through the array and whenever we find a non-zero
#  element, we swap it with the zero element at the current position of the non-zero pointer. This way,
#  we move all the non-zero elements to the left and all the zero elements to the right.