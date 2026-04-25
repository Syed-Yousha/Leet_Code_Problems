class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] not in vowels:
                left += 1
            elif s[right] not in vowels:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return ''.join(s)
    

# time complexity: O(n)
# space complexity: O(n)
# This solution uses the two-pointer technique to reverse the vowels in place.
#  We maintain two pointers, one starting from the beginning of the string and the other from the end.
#  We move the pointers towards each other until they meet, swapping the vowels when both pointers point to a vowel.