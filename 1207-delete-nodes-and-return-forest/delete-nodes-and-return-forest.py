# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,to_delete,forest):
        if root is None:
            return forest
        left=self.helper(root.left,to_delete,forest)
        if left is None:
            root.left=None
        right=self.helper(root.right,to_delete,forest)
        if right is None:
            root.right=None
        if root.val in to_delete:
            if root.left is not None:
                forest.append(root.left)
            if root.right is not None:
                forest.append(root.right)
            return None
        return forest

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        list=[]
        s=set(to_delete)
        if root.val not in to_delete:
            list.append(root)
        self.helper(root,s,list)
        return list

