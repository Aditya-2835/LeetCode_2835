# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        grp_prev=head
        grp_size=2

        while grp_prev.next:
            curr=grp_prev.next
            count=0
            while curr and count<grp_size:
                curr=curr.next
                count+=1

            if count%2==0:
                curr=grp_prev.next
                prev=None
                for i in range(count):
                    nex=curr.next
                    curr.next=prev
                    prev=curr
                    curr=nex

                tail=grp_prev.next
                grp_prev.next=prev
                tail.next=curr
                grp_prev=tail
            else:
                for _ in range(count):
                    grp_prev=grp_prev.next

            grp_size+=1

        return head