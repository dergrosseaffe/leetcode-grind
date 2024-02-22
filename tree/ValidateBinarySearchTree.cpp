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
    bool isBSTUtil(TreeNode* node, long min, long max) {
      if (node == nullptr)
          return true;

      // false if this node violates the min/max constraint
      if (node->val <= min || node->val >= max)
          return false;

      // otherwise check the subtrees recursively,
      // tightening the min or max constraint
      return
        isBSTUtil(node->left, min, node->val) &&
        isBSTUtil(node->right, node->val, max);
    }

    bool isValidBST(TreeNode* root) {
        return isBSTUtil(root, LONG_MIN, LONG_MAX);
    }
};
