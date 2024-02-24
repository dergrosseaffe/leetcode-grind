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
    vector<int> rightSideView(TreeNode* root) {
        if (root == nullptr) return {};

        std::queue<TreeNode*> q;
        q.push(root);
        std::vector<int> view;

        while (!q.empty()) {
            size_t levelSize = q.size();

            for (size_t i = 0; i < levelSize; i++) {
                auto node = q.front();
                q.pop();

                // last element of current level: add it to the view list
                if (i == levelSize - 1)
                    view.push_back(node->val);

                if (node->left != nullptr) q.push(node->left);
                if (node->right != nullptr) q.push(node->right);
            }
        }

        return view;
    }
};
