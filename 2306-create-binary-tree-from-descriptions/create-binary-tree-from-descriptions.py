# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        dict={}
        child_set=set()
        root=None

        for parent, child,isLeft in descriptions:
            if parent not in dict:
                dict[parent]=TreeNode(parent)
            if child not in dict:
                dict[child]=TreeNode(child)
            if isLeft:
                dict[parent].left=dict[child]
            else:
                dict[parent].right=dict[child]
            child_set.add(child)


        for parent, child,isLeft in descriptions:
            if parent not in child_set:
                return dict[parent]            
        