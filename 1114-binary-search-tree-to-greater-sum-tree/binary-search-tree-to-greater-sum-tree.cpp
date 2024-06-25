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
    unsigned int sum = 0;
    TreeNode* bstToGst(TreeNode* root) {
        if(root->right!=nullptr){
            bstToGst(root->right);
        }

        root->val+=sum;
        sum=root->val;
        if(root->left!=nullptr){
            bstToGst(root->left);
        }
        return root;
    }
};