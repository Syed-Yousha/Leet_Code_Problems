class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        window = set()
        l = 0

        for r in range(len(nums)):

            if nums[r] in window:
                return True

            window.add(nums[r])

            if abs(r - l) >= k:
                window.remove(nums[l])
                l += 1

        

        return False         



# Time Complexity: O(n)
# Space Complexity: O(k)
