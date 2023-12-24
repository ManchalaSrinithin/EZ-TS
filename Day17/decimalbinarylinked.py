# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
            str1=''
            temp=head
            while temp!=None:
                str1+=str(temp.val)
                temp=temp.next
            return (int(str1,2))
