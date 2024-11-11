# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head    
        temp=head
        arr=[]
        while temp:
            arr.append(temp.val)
            temp=temp.next
        arr.sort()
        temp=head
        for i in range(len(arr)):
            temp.val=arr[i]
            temp=temp.next
        return head           

        