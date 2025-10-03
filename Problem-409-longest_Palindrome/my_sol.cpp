class Solution {
public:
    int longestPalindrome(string s) {
        unordered_map<char, int> freq;
        for (char w : s) {
            freq[w]++;
        }

        int length = 0;
        bool hasOdd = false;

        for (auto p : freq) {
            if (p.second % 2 == 0) {
                length += p.second;      // even counts use fully
            } else {
                length += p.second - 1;  // odd counts → take even part
                hasOdd = true;           // at least one odd exists
            }
        }

        if (hasOdd) length++;  // center me ek odd allow hai
        return length;
    }
};
