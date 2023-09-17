# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head: Optional[ListNode], end: Optional[ListNode])-> Optional[ListNode]:
        p = end
        curr =  head
        while curr and curr.next and curr!=end:
            temp = curr.next
            curr.next = p
            p = curr
            curr = temp
        if curr!= end and curr:
            curr.next = p
            p = curr
        return head, p
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = k
        curr = head
        dummy = ListNode()
        prev = None
        first = False
        headNode = None
        prevCurrHead = None
        while curr:
            n = k
            currHead = curr
            while curr and n:
                prev = curr
                curr = curr.next
                n -=1
            if not n:
                if prevCurrHead:
                    prevCurrHead.next = prev
                currHead, p = self.reverse(currHead, curr)
                if not first:
                    headNode = p
                    first = True
                prevCurrHead = currHead
        return headNode