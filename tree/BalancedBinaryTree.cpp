#include <iostream>
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
    int checkDepth(TreeNode *root) {
        if (root == nullptr)
            return 0;

        int leftDepth = checkDepth(root->left);
        if (leftDepth == -1) return -1;

        int rightDepth = checkDepth(root->right);
        if (rightDepth == -1) return -1;

        if (std::abs(leftDepth - rightDepth) > 1) return -1;

        return 1 + std::max(leftDepth, rightDepth);
    }

    bool isBalanced(TreeNode* root) {
        return checkDepth(root) != -1;
    }
};
