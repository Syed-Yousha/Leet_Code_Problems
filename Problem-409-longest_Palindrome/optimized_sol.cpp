class Solution {
public:
    int longestPalindrome(string s) {
        unordered_set<char> st;
        int length = 0;

        for (char c : s) {
            if (st.count(c)) {
                length += 2;  // make a pair
                st.erase(c);
            } else {
                st.insert(c);
            }
        }

        // If any odd remains, we can place one in the center
        return !st.empty() ? length + 1 : length;
    }
};
