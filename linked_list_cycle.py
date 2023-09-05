class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nexts=[]
        current=head

        while current:
            if current.next not in nexts:
                nexts.append(current.next)
            else:
                return True
            current=current.next