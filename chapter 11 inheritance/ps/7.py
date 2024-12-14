class vector:

    def __init__(self, l1):
        self.l1 = l1
    
    def __len__(self):
        return len(self.l1)
    
a = vector([5,7,6])

print(len(a))

