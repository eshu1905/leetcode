# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        if n==1 and not head or not head.next:
            return None
        temp=head
        i=0
        while temp:
            i+=1
            temp=temp.next
        if i==n:
            newhead=head.next
            return newhead
        val=i-n
        temp=head
        while temp:
            val-=1
            if val==0:
                break
            temp=temp.next
        if temp:     
            temp.next=temp.next.next
            return head    

            

        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        