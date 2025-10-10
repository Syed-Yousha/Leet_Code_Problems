class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int size = nums.size();

        for (int i = 0; i < size; i++) {
            if (nums[i] == target) {
                return i;
            }

            if (i + 1 < size && nums[i+1] > target) {
                return i + 1;
            }

            if (target < nums[0]) {
                return 0;
            }
        }

        return size;
    }
};

// Time: O(n)
// Space: O(1)