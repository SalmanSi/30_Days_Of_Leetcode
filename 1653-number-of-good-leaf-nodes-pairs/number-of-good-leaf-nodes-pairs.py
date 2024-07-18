# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root,distance):
        if not root.left and not root.right:
            return [1]
        left_list=[]
        right_list=[]
        if root.left is not None:
            left_list=self.dfs(root.left,distance)
        if root.right is not None:
            right_list=self.dfs(root.right,distance)
        
        left_list.sort()
        right_list.sort()
        flag=False
        for i in left_list:
            for j in right_list:
                if i+j>distance:
                    flag=True
                    break
                self.count+=1

        return [x+1 for x in left_list+right_list]
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.count=0
        
        self.dfs(root,distance)

        return self.count