class Node:
    def __init__(self,key=None):
        self.key = key 
        self.next = None;
    def __len__(self):
        return str(self.key)
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    def pushFront(self,key):
        new_node = Node(key)
        new_node.next = L.head;
        L.head = new_node
        self.size+=1
    def pushBack(self,key):
        v = Node(key)
        if len(self)==0 :
            self.head = v
        else :
            tail = self.head
            while tail.next != None:
                tail = tail.next
            tail.next = v
        self.size = 0
    def popFront(self):
        if len(self) == 0 :
            return None
        else :
            x = self.head
            key  = x.key
            self.head = x.next
            self.size -= 1
            del x
            return key
    def popBack(self):
        if len(self) == 0 :
            return None
        else :
            tail = self.head
            prev = None
            while tail != None:
                prev = tail
                tail = prev.next
            if len(self) == 0 :
                return None
            else :
                prev.next = None
                key = tail.key
                self.size -= 1
                del tail
                return key
    def search(self,key):
        if len(self) == 0:
            return None
        v = self.head
        while v != None:
            if key == v.key :
                return v
            v = v.next
        return None
    def __iter__(self):
        v = self.head
        while v != None :
            yield v
            v = v.next     
L = SinglyLinkedList()
L.pushFront(-1)
L.pushFront(9)
L.pushFront(3)
while L.head != None:
    print(L.head.key)
    L.head = L.head.next

for x in L:
    print(x.key)