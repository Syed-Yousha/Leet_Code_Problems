class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i = m - 1;      // nums1 ka last valid index
        int j = n - 1;      // nums2 ka last index
        int k = m + n - 1;  // nums1 ka total last index

        while (i >= 0 && j >= 0) {
            if (nums1[i] > nums2[j]) {
                nums1[k--] = nums1[i--];
            } else {
                nums1[k--] = nums2[j--];
            }
        }

        // Agar nums2 ke elements bache ho
        while (j >= 0) {
            nums1[k--] = nums2[j--];
        }
    }
};


//time complexity O(m+n)
//Space complexity O(1)