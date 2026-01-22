class Solution:
    def removeStars(self, s: str) -> str:
        n = len(s)
        stack = []
        for ch in s:
            if ch != '*':
                stack.append(ch)
            else:
                stack.pop()
        
        return "".join(stack)
    
# time complexity: O(n)
# space complexity: O(n)
# optimal solution 