from collections import deque

class Queue:
    def __init__(self):
       self.deque = deque();
       
        
    def Inqueue(self, val):
        self.deque.append(val);
    
    def Dequeue(self):
        if len(self.deque) == 0:
            print("stack is empty");
            return None;
        else :
            return self.deque.popleft();
    def __len__(self):
        return len(self.deque);
    
def JosePhus(n,k):
    q = Queue();
    for i in range(n):
       q.Inqueue(i+1);
    kill = 0;   
    while len(q) > 1:
        if kill!=k:
            x=q.Dequeue();    
            q.Inqueue(x);
            kill+=1;
        else :
            q.Dequeue();
            kill=0;
    print(q.Dequeue());         

JosePhus(9,3);
