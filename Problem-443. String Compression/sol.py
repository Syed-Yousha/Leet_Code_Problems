class Solution:
    def compress(self, chars: List[str]) -> int:
        insert = 0
        i = 0
        while i < len(chars):
            group = 1
            while (group + i) < len(chars)  and chars[group+i] == chars[i]:
                group+=1

            chars[insert] = chars[i]
            insert += 1
            if group > 1:
                string = str(group)
                chars[insert:insert+len(string)] = list(string)
                insert += len(string)

            i+= group
        return insert
    

# time complexity: O(n)
# space complexity: O(1)
# Data structure: two pointers, string manipulation
# Explaination: We use two pointers, one to read the characters and another to write the compressed string.
#   We count the occurrences of each character and write the character followed by its count (if greater than 1) 
#   to the array. 
#   Finally, we return the length of the compressed string.