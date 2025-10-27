class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0] * (len(nums)+1)
        for i in range(len(nums)):
            self.prefix[i+1] = self.prefix[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
            return self.prefix[right+1] - self.prefix[left]
                  


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

#this is the most optimal solution using prefix sum 
#time complexity O(1) for sumRange and O(n) for initialization
#space complexity O(n) for prefix array each query takes O(1) time
#over O(n) space for prefix sum array and time complexity O(n+q) where q is number of queries and n is length of nums array