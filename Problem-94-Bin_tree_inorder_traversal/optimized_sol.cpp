class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> output;
        TreeNode* curr = root;

        while (curr != nullptr) {
            if (curr->left == nullptr) {
                output.push_back(curr->val);
                curr = curr->right;
            } 
            else {
                TreeNode* pre = curr->left;
                while (pre->right && pre->right != curr) {
                    pre = pre->right;
                }

                if (pre->right == nullptr) {
                    pre->right = curr;  // make a thread
                    curr = curr->left;
                } else {
                    pre->right = nullptr;  // remove thread
                    output.push_back(curr->val);
                    curr = curr->right;
                }
            }
        }

        return output;
    }
};



// Time Complexity: O(n)

// Space Complexity: O(1)
