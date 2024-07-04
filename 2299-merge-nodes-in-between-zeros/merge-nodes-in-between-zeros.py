# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sums=[]
        temp=0
        current=head.next
        while current:
            if current.val == 0:
                sums.append(temp)
                temp=0
            else:
                temp+=current.val
            current=current.next
        head=ListNode(sums[0])
        current = head  

        for num in sums[1:]:
            current.next=ListNode(num)
            current=current.next
        return head
