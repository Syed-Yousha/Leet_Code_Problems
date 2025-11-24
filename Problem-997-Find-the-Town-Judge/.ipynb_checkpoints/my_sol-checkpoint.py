import numpy as np

class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        
        size = len(trust)
        
        for i in range(1, size):
            if trust[i][1] != trust[i-1][1] :
                if trust[i][0] != trust[i][0]:
                    return -1
        return trust[0][1]


obj = Solution()
obj.findJudge(2, [[1,2]])
