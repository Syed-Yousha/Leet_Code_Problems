class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e', 'i', 'o', 'u']
        C_Vowels = [v.upper() for v in vowels]
        id_vow = []
        new_word = []
        for ch in s:
            if ch in vowels or ch in C_Vowels:
                id_vow.append(ch)


        for ch in s:
            if ch in vowels or ch in C_Vowels:
                new_word.append(id_vow.pop())
            else:
                new_word.append(ch)

        return "".join(new_word)
            


# time complexity: O(n)
# space complexity: O(n)
# Here we are using the concept of stack to store the vowels and then
#  pop them out in reverse order while constructing the new string.