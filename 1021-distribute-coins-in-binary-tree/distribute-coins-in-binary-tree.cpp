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
    int moves=0;
    int distributeCoins(TreeNode* root,bool first=true) {
        if(root->left!=nullptr){
            root->val+=distributeCoins(root->left,false);

        } 
        if(root->right!=nullptr){
            root->val+=distributeCoins(root->right,false);
        } 
        if(root->right==nullptr and root->left==nullptr){
            moves+=abs(root->val-1); 
            return root->val-1;// transfer extra coins to root or take 1 if zero coinsf
        }
        if(first) return moves;
        else {
            moves+=abs(root->val-1);
            return root->val-1;}
    }   
};