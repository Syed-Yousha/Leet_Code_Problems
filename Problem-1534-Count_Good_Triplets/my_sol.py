class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        
        tri = 0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if abs(arr[i] - arr[j]) > a:
                        continue
                for k in range(j+1,len(arr)):
                    
                    if abs(arr[j] - arr[k]) > b:
                        continue
                    if abs(arr[i] - arr[k]) > c:
                        continue
                    
                    tri += 1

        return tri

                    

                

#time complexity: O(n^3) worst case, else O(n^2)
#space complexity: O(1)