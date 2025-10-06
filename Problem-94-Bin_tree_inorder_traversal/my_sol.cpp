/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> output;
        if (!root) return output;  // base case

        vector<int> leftPart = inorderTraversal(root->left);
        output.insert(output.end(), leftPart.begin(), leftPart.end());

        output.push_back(root->val);

        vector<int> rightPart = inorderTraversal(root->right);
        output.insert(output.end(), rightPart.begin(), rightPart.end());

        return output;
    }
};


// Time Complexity: O(n)

// Space Complexity: O(n)
