class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowers = 0
        
        # Agar start mein hi n = 0 hai, toh seedha True return kardo
        if n == 0:
            return True
            
        for i in range(len(flowerbed)):
            # Hum sirf tab check karenge jab current spot khali ho
            if flowerbed[i] == 0:
                
                # Check left: Ya toh array ka start ho (i == 0) YA left wala spot khali ho
                empty_left = (i == 0) or (flowerbed[i - 1] == 0)
                
                # Check right: Ya toh array ka end ho YA right wala spot khali ho
                empty_right = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                
                # Agar dono conditions meet ho rahi hain toh flower plant kar do
                if empty_left and empty_right:
                    flowerbed[i] = 1  # Array ko update zaroor karna hai
                    flowers += 1
                    
                    # Early Exit: Agar target pura ho gaya toh mazeed loop chalane ki zaroorat nahi
                    if flowers >= n:
                        return True
                        
        # Agar pura loop chalne ke baad bhi target pura nahi hua
        return False
    

# time complexity: O(n)
# space complexity: O(1)
# what changed? Code is cleaner, less edge cases, and early exit condition added.