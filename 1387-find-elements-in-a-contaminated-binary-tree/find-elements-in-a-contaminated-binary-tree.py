# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.rootnode=root
        self.myset=set()
        self.rootnode.val=0
        queue=deque()
        queue.append(root)
        while queue:
            cur=queue.popleft()
            self.myset.add(cur.val)
            if cur.left is not None:
                cur.left.val=2*cur.val+1
                queue.append(cur.left)
            if cur.right is not None:
                cur.right.val=2*cur.val+2
                queue.append(cur.right)
            

    def find(self, target: int) -> bool:
        return (target in self.myset)


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)