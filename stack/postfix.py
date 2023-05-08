class Stack:
    def __init__(self):
        self.items = [];
        
    def pop(self):
        try:
            return self.items.pop();
        except:
            print("stack is empty");
    
    def push(self, val):
            self.items.append(val);
        
    def top(self):
        try:
            return self.items[-1];
        except:
            print("stack is empty");
    
    def __len__(self):
        return len(self.items);
            
            
outstack = [];
opstack = Stack();
userInput = input();

for token in userInput:
    if token in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] :
        outstack.append(token);
    elif token == '(': 
        opstack.push(token);
    elif token == ')':
            while str(opstack.top()) != '(' and len(opstack)!= 0:
                    outstack.append(opstack.pop());
            opstack.pop();
    elif token in ['*', '/', '-', '+']:
        if token== '+' or token == '-':
            while len(opstack) != 0 and opstack.top() != '(':
                outstack.append(opstack.pop());
        opstack.push(token);
        

while len(opstack)!= 0 :
    outstack.append(opstack.pop());

s = Stack()
for token in outstack : 
    if token in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        s.push(token);
    if token in ['/', '*', '+', '-']:
        a = s.pop();
        b = s.pop();
        if token == '/':
            s.push(int(b)/ int(a));
        elif token == '*':
            s.push(int(b) * int(a));
        elif token == '-':
            s.push(int(b)-int(a));
        else :
            s.push(int(b)+int(a));

print(s.pop());