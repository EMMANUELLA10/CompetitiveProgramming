class ListNode(object):
    def __init__(self, val=0, next=None):
        self.head = None
        self.val = val
        self.next = next

class Solution(object):
    
    def mergeTwoLists(self, list1, list2):
        
        mergedlist = ListNode(0)

        current1 = list1
        current2 = list2

        temp = mergedlist 
        if not list1:
            return list2
        elif not list2:
            return list1

        while current1 is not None and current2 is not None:
            if current1.val < current2.val:
                temp.next=current1
                temp = temp.next
                current1 = current1.next

            else:
                temp.next = current2
                temp = temp.next
                current2 = current2.next

        while current1 is not None:
                temp.next = current1
                temp = temp.next
                current1 = current1.next

        while current2 is not None:
                temp = current2
                temp = temp.next
                current2 = current2.next

        return mergedlist.next
