class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
       self.head = None
       self.sz = 0
    def get(self, index: int) -> int:
        if index<0 or index>=self.sz:
            return -1
        idx = 0
        current = self.head
        while current != None and idx!=index:
            current = current.next
            idx+=1
        return (current.val)

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)
        
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.sz,val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index>self.sz:
            return
        current = self.head
        newNode = ListNode(val)
        if index==0:
            newNode.next = current
            self.head = newNode
        else:
            idx = 0
            while(idx!=index-1):
                current = current.next
                idx+=1
            newNode.next = current.next
            current.next = newNode
        self.sz+=1


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.sz:
            return
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            idx = 0
            while(idx < index-1):
                current = current.next
                idx+=1
            current.next = current.next.next
        self.sz-=1

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)