class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        n = len(senate)
        R = deque()
        D = deque()

        for i in range(n): 
            if senate[i] == "R":
                R.append(i)
            else:
                D.append(i)
        
        while D and R:
            r = R.popleft()
            d = D.popleft()


            if d < r:
                D.append(d+n)
            else:
                R.append(r+n)
        
        return "Radiant" if R else "Dire"


# time complexity: O(n)
# space complexity: O(n)
# optimal approach using queue data structure to simulate the banning process