class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        #nums = [1,2,3,4]
        #k = 5

        nums.sort()
        i = 0
        size = len(nums)
        j = len(nums) - 1 
        count = 0
        
        while(i < j):
            my_sum = nums[i] + nums[j] 
            if my_sum == k:
                count+=1
                i+=1
                j-=1
            elif my_sum > k:
                j-=1
            elif my_sum < k:
                i+=1

        return count
            
#time complexity: O(nlogn) because of sorting
#space complexity: O(1) because we are not using any extra space
#explaination: we are using two pointers to find the pairs that sum up to k.
#  We sort the array first and then use two pointers to find the pairs. If the sum of the two pointers 
# is equal to k, we increment the count and move both pointers. If the sum is greater than k, we move 
# the right pointer to the left. If the sum is less than k, we move the left pointer to the right. 
# We continue this process until the two pointers meet.
