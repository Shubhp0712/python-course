class TwoDvector:
    
    def __init__(self,i,j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The vectors are {self.i}i + {self.j}j")


class ThreeDvector(TwoDvector):
    
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k

    def show(self):
        print(f"The vectors are {self.i}i + {self.j}j + {self.k}k")

v1 = TwoDvector(5,7)
v1.show()

v2 = ThreeDvector(2,8,1)
v2.show()