class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        l=1
        while current:
            l+=1
            current=current.next
        mid=ceil(l/2)
        current=head
        x=1
        while current:
            if x==mid:
                break
            x+=1
            current=current.next
        return current