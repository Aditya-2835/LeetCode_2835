# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left==right:
            return head

        dummy=ListNode(0,head)
        before=dummy

        for i in range(left-1):
            before=before.next

        curr=before.next
        prev=None
        
        for i in range(right-left+1):
            nex=curr.next
            curr.next=prev
            prev=curr
            curr=nex

        before.next.next=curr
        before.next=prev

        return dummy.next