# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        arr=[]
        while(temp):
            arr.append(temp.val)
            temp=temp.next
        temp=head   
        while(temp):
            temp.val=arr.pop()
            temp=temp.next
        temp1=head
        return temp1

        