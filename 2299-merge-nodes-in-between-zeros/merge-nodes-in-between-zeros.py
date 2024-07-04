# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        next_ptr=head
        current_ptr=head
        sum=0
        while next_ptr:
            if next_ptr.val == 0:
                current_ptr.val=sum
                # prevent overflow//null
                current_ptr.next=next_ptr.next
                current_ptr=current_ptr.next
                next_ptr=current_ptr
                sum=0
            else:
                sum+=next_ptr.val
                next_ptr=next_ptr.next
        return head.next


        # sums=[]
        # temp=0
        # current=head.next
        # while current:
        #     if current.val == 0:
        #         sums.append(temp)
        #         temp=0
        #     else:
        #         temp+=current.val
        #     current=current.next
        # head=ListNode(sums[0])
        # current = head  

        # for num in sums[1:]:
        #     current.next=ListNode(num)
        #     current=current.next
        # return head
