# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        if head.next is None and n==1:
            head=None
            return head
        temp=head
        c=0    
        while temp:
            temp=temp.next
            c+=1
        res=c-n
        if res==0:
            head=head.next
            return head
        temp=head
        while temp:
            res-=1
            if res==0:
                temp.next=temp.next.next
            temp=temp.next
        return head            
        