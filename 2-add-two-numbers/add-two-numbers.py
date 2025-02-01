# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def recurse(self,l1,l2,l3,c):
        if l1 is None and l2 is None and c==1:
            node=ListNode(1)
            return node
        if l1 is None and l2 is None and c==0:
            return None
        elif l1 is None:
            sum=l2.val+c
            if sum>9:
                c=1
                sum-=10
            else:
                c=0
            node=ListNode(sum)
            node.next=self.recurse(None,l2.next,node,c)
        elif l2 is None:
            sum=l1.val+c
            if sum>9:
                c=1
                sum-=10
            else:
                c=0
            node=ListNode(sum)
            node.next=self.recurse(l1.next,None,node,c)
        else:       
            sum=l1.val+l2.val+c
            if sum>9:
                c=1
                sum-=10
            else:
                c=0
            node=ListNode(sum)
            node.next=self.recurse(l1.next,l2.next,node,c)
        return node
        

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root=self.recurse(l1,l2,None,0)
        return root

        