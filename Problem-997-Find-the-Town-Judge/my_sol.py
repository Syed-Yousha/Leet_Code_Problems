class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        
        score = [0] * (n + 1)
        
        for a, b in trust:
            score[a] -= 1
            score[b] += 1

        for i in range(1, n+1):
            if score[i] == n-1:
                return i

        return -1
            


#time complexity: O(n + m) where n is the number of people and m is the length of trust list
#space complexity: O(n) for the score list