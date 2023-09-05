
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        slow = fast = head
        while fast:
            fast = fast.next
            if fast and fast.next:
                fast = fast.next
                slow = slow.next
        
        
        prev = slow
        ptr = prev.next
        prev.next = None
        while prev != None and ptr != None:
            _next = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = _next
        head_2 = prev
        
        
        left = head
        right = head_2
        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True