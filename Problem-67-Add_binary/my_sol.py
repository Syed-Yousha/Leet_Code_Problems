class Solution:
    def addBinary(self, a: str, b: str) -> str:
        val_a = 0
        i = 0
        for c in reversed(a):
            if c == "1":
                val_a += 1 << i
            i += 1

        val_b = 0
        i = 0
        for c in reversed(b):
            if c == "1":
                val_b += 1 << i
            i += 1
        
        total = val_a + val_b
        res = ""

        while total > 0:
            remainder = total % 2
            res = str(remainder) + res
            total = total // 2

        return res if res else "0"



# time complexity: O(n)
# space complexity: O(n)