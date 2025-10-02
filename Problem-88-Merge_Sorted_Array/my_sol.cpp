class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        
        int i = 0; 
        int j = 0;
        vector<int> arr(m+n);
        int x = 0;

        while (i < m || j < n) {
            if (i < m && (j >= n || nums1[i] < nums2[j])) {
                arr[x++] = nums1[i++];
            } else {
                arr[x++] = nums2[j++];
            }
        }

        for(int k = 0; k < m+n; k++) {
            nums1[k] = arr[k];
        }
    }
};


//time complexity O(m+n)
//Space complexity O(m+n)