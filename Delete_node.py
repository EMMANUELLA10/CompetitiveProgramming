class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        nxt=node.next
        if node.next.next:
            node.next=node.next.next
        else:
            node.next=None

        node.val=nxt.val