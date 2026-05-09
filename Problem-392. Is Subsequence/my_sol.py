class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        t = t[::-1]
        s = list(s)
        
        for ch in t:
            if s and s[-1] == ch:
                s.pop()
            
        return not s
        

# Time: O(n)
# Space: O(1)
# explaination: We reverse the string t and iterate through it. If the last character of s matches the current 
# character in t, we pop it from s. If at the end of the iteration s is empty, it means all characters of s were 
# found in t in order, so we return True. Otherwise, we return False.