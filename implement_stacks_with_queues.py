class ListNode():
    def __init__(self, val = 0, next = None):
        self.val = val 
        #self.head = None
        self.next = next

class MyStack():
    def __init__(self):
        self.head = None 

    def push(self, x: int) -> None:
        new_node = x
        current = self.head
        if not self.head:
            self.head = new_node
        else:
            current = self.head
        
            while current.next:
                current = current.next

            current.next = new_node

    def pop(self) -> int:
        if not self.head:
            return 

        if self.head == val:
            self.head = self.head.next

            return self.head.val

    def top(self) -> int:
        self.head = current
        current = current.next
        if not self.head:
            return current.next.val
        

    def empty(self) -> bool:
        if self.head:
            return False
        else:
            return True
