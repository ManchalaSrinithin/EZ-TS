class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        left=dummy
        right=head
        while right and right.next:
            left=left.next
            right=right.next.next
        left.next=left.next.next
        return dummy.next
