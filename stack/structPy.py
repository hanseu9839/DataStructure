class Stack:
    def __init__(self):
        self.items = [];
    
    def push(self, val):
        return  self.items.append(val);
    
    def pop(self):
        try:
            return self.items.pop();
        except IndexError:
            print("Stack is empty");
            return False;
    
    def top(self):
        try:
            return self.items[-1];
        except IndexError:
            print("Stack is empty");
            return False;
            
    def __len__(self):
        return len(self.items);

def bracketCorrect(userInput) :
    for i in range(len(userInput)):
        if userInput[i] == '(':
            s.push(userInput[i]);
        elif userInput[i] == ')':
            try :
                s.pop();
            except IndexError:
                return False;
    if len(s) > 0 :
        return False;
    return True;

userInput = input();
s = Stack();
print(bracketCorrect(userInput));
