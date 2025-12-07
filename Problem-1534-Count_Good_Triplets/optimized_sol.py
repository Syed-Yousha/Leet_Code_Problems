class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        tri = 0
        
        # Precompute all pair differences
        diff = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                diff[i][j] = abs(arr[i] - arr[j])
        
        for i in range(n):
            for j in range(i+1, n):
                if diff[i][j] > a:
                    continue
                
                for k in range(j+1, n):
                    if diff[j][k] > b or diff[i][k] > c:
                        continue
                    tri += 1
        
        return tri
    
#time complexity: O(n^3) can be also considered O(n^2) due to early continues
#space complexity: O(n^2)