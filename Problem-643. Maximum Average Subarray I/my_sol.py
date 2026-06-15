class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #nums = [1,12,-5,-6,50,3]
        #k=4
        curr_sum = sum(nums[:k])
        my_max = curr_sum 
        
        for i in range(k, len(nums)):
            curr_sum = curr_sum - nums[i - k] + nums[i]

            if curr_sum > my_max:
                my_max = curr_sum  

        return my_max/k

        

#time complexity: O(n)
#space complexity: O(1)
#explaination: We use a sliding window approach to calculate the sum of each subarray of size k. 
# We initialize the current sum with the sum of the first k elements and then iterate through the array,
# updating the current sum by subtracting the element that is sliding out of the window and adding the
# new element that is sliding in. We keep track of the maximum sum encountered and return it divided by
# k to get the maximum average.