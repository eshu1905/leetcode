# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        if not head:
            return None
        temp1=head
        temp2=head
        while  temp2 and temp2.next:
            temp1=temp1.next
            temp2=temp2.next.next
        return temp1   
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        