def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        temp=head
        while temp:
            while temp.next and temp.val==temp.next.val:
                temp.next=temp.next.next
            temp=temp.next
        return head
