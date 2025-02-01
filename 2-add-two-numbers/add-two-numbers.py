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

        dummyNode=ListNode(0)
        curr=dummyNode
        c=0

        while l1  != None or l2  != None or c!=0:
            l1Val=l1.val if l1 else 0
            l2Val=l2.val if l2 else 0
            sum=l1Val+l2Val+c
            c=sum//10
            node= ListNode(sum%10)
            curr.next=node
            curr=node
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return dummyNode.next

            

        