from typing import List
from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # Count rows as tuples
        row_count = Counter(tuple(row) for row in grid)
        
        # Count columns as tuples
        col_count = Counter(tuple(col) for col in zip(*grid))
        
        # Count matching row-column pairs
        return sum(row_count[row] * col_count[row] for row in row_count)

# Time Complexity: O(n^2)
# Space Complexity: O(n)
# using hash maps to store counts of rows and columns