class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        ptr_s, ptr_t = 0
        while ptr_s < len(s) and ptr_t < len(t):
            if s[ptr_s] == t[ptr_t]:
                ptr_s += 1
            ptr_t += 1
        return ptr_s == len(s)

# Time: O(n)
# Space: O(1)
# explaination: We use two pointers to iterate through both strings s and t. The pointer ptr_s is used to track the
# current character in s, while ptr_t is used to track the current character in t. We iterate through t, and whenever
# we find a character in t that matches the current character in s (pointed by ptr_s), we move the ptr_s to the next 
# character in s. If at the end of the iteration, ptr_s has reached the length of s, it means all characters of s were 
# found in t in order, so we return True. Otherwise, we return False.