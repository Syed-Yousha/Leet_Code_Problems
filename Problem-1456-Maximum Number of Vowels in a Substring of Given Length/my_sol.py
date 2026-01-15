class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 0
        right = k-1
        n = len(s) 
        vowel = 0
        maximum = - 9999

        i = left
        while i <= right:
            if s[i] in ['a', 'e', 'i', 'o', 'u']:  
                vowel = vowel + 1
            i += 1

        maximum = max(maximum, vowel)

        left += 1
        right += 1

        while right < n:
            if s[left-1] in ['a', 'e', 'i', 'o', 'u']:  
                vowel -= 1
            if  s[right] in ['a', 'e', 'i', 'o', 'u']:  
                vowel += 1
            
            maximum = max(maximum, vowel)

            left += 1
            right += 1
        

        return maximum


#time complexity: O(n)
#space complexity: O(1)