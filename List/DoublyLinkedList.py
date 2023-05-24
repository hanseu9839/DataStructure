class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = self
        self.prev = self 
        
class DoublyLinked:
    def __init__(self):
        self.head = Node()
        self.size = 0
        
    def __iter__(self):
        n = self.head
        
        while n != None:
            yield n
            n = n.next
            
    def __len__(self):
        return self.size
    
    def splice(self, a, b, x):
        ap = a.prev , bn = b.next , xn = x.next 
        ap.next = bn
        bn.prev = ap
        x.next = a
        a.prev = x
        b.next = xn
        xn.prev = b
        
    def moveAfter(self,a,x):
        self.splice(a, a, x)
        
    def moveBefore(self,a,x):
        self.splice(a, a, x.prev)
        
    def insertAfter(self, x, key):
        self.moveAfter(Node(key),x)
    
    def insertBefore(self, x, key):
        self.moveBefore(Node(key), x)
        
    def pushFront(self, key):
        self.insertAfter(self.head,key) 
    
    def pushBack(self, key):
        self.insertBefore(self.head, key)
           
    dL = DoublyLinked()
    dL.pushFront(8)
    dL.pushFront(5)
    dL.pushFront(-1)
    iter(dL)
    
        
        