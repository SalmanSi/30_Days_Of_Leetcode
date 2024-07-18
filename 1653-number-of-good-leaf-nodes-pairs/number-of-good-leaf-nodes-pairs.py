# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def countPairs(self, root: TreeNode, distance: int) -> int:
        count=0
        def dfs(root,distance):
            nonlocal count
            if not root.left and not root.right:
                return [1]
            left_list=[]
            right_list=[]
            if root.left is not None:
                left_list=dfs(root.left,distance)
            if root.right is not None:
                right_list=dfs(root.right,distance)
            
            for i in left_list:
                for j in right_list:
                    if i+j<=distance:
                        count+=1
            return [x+1 for x in left_list+right_list]
        ans=dfs(root,distance)
        print(ans)
        print(count)
        return count