class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        merge = ""
        for char1, char2 in zip(word1, word2):
            merge += char1
            merge += char2 

        merge += word1[len(word2):]
        merge += word2[len(word1):]
            
        return merge

# time complexty: O(n)