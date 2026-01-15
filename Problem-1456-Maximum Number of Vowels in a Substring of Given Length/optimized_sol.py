class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e' , 'i', 'o', 'u'}

        max_sub = 0
        cur_count = 0

        for idx in range(len(s)):
            if s[idx] in vowels:
                cur_count += 1
            
            if idx >= k - 1:
                max_sub = max(max_sub, cur_count)

                if s[idx - k + 1] in vowels:
                    cur_count -= 1
        
        return max_sub

#time complexity: O(n)
#space complexity: O(1)
#more elegant solution compared to my_sol.py