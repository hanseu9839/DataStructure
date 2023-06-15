class hash:
    def __init__(self):
        self.h = []
        self.m = 10
    
    def hashFunction(self,key):
        self.h[key%10].key = key
    
    def find_slot(self, key):
        i = self.hashFunction(key)
        start = i
        while (start!=i) and (self.h[i].key==key):
            i=(i+1)%self.m
            if i == start : return None
        return i;
    
    def set(self, key, value=None):
        i= self.find_slot(key)
        if i == None : return None
        