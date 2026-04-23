class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowers = 0
        
        if len(flowerbed) > 1:

            if flowerbed[0] == 0 and flowerbed[1]==0:
                flowerbed[0] = 1
                flowers += 1

            for i in range(1, len(flowerbed)-1):
                if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowers += 1
                    flowerbed[i] = 1
                
            if flowerbed[-1] == 0 and flowerbed[-2]==0:
                flowerbed[-1] = 1
                flowers += 1

        else:
            if len(flowerbed) == 0:
                if n == 0:
                    return True
                else:
                    return False
            else:
                if flowerbed[0] == 0 and n == 1:
                    return True
                elif flowerbed[0] == 1 and n == 0:
                    return True
                elif flowerbed[0] == 0 and n == 0:
                    return True
                else:
                    return False
        
        if flowers >= n:
            return True 
        else:
            return False
        
        
        
# time complexity: O(n)
# space complexity: O(1)
# Problem in solution: to many edge cases, and the code is not clean.  