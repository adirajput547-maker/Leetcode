# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        count=0
        curr=head
        while curr:
            count+=1
            curr=curr.next
        if k>=count:
            k=k%count
        if k==0:
            return head
        n=count-k-1
        ptr1,ptr2,ptr3=head,head,head
        for i in range(n):
            ptr1=ptr1.next
            ptr2=ptr2.next
        ptr2=ptr2.next
        ptr1.next=None
        head=ptr2
        while ptr2.next:
            ptr2=ptr2.next
        ptr2.next=ptr3
        return head