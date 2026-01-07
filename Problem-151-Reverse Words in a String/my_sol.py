class Solution:
    def reverseWords(self, s: str) -> str:
        sent = []
        word = []
        
        for c in s:
            
            if c == " ":
                if word:
                    sent.append("".join(word))
                    word = []
            else: 
                word.append(c)

        if word:
            sent.append("".join(word))

        sent.reverse()
        result = " ".join(sent)
        return result
        

          

#time complexity: O(n)
#space complexity: O(n)