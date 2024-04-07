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
    int max_sum = INT_MIN;

    int maxGain(TreeNode* node) {
        if (node == nullptr)
            return 0;

        auto left = max(0, maxGain(node->left));
        auto right = max(0, maxGain(node->right));

        auto path_with_node = node->val + left + right;
        max_sum = max(max_sum, path_with_node);

        return node->val + max(left, right);
    }

    int maxPathSum(TreeNode* root) {
        maxGain(root);
        return max_sum;
    }
};
