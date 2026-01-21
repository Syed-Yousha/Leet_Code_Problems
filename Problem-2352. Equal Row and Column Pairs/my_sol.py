class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        count = 0
        transpose = [[0] * n for _ in range(n)]
        for i in range(n): 
            for j in range(n):
                
                transpose[i][j] = grid[j][i]

        for i in range(n): 
            for j in range(n):
                if grid[i] == transpose[j]:
                    count += 1

        return count 


        

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
# brute force approach to compare each row with each column after transposing the matrix
