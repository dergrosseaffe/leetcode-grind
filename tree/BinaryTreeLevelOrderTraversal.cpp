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
#include <queue>

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        if (root == nullptr) return {};

        std::queue<TreeNode*> q;
        q.push(root);
        std::vector<std::vector<int>> order;
        while (!q.empty()) {
            std::vector<int> level;

            size_t levelSize = q.size();
            for (size_t i = 0; i < levelSize; i++) {
                auto node = q.front();
                q.pop();
                level.push_back(node->val);

                if (node->left != nullptr)  q.push(node->left);
                if (node->right != nullptr) q.push(node->right);
            }

            order.push_back(level);
        }

        return order;
    }
};
