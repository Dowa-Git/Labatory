class TestClass:
    def __init__(self):
        self.a = 0
        self.b = 1
        self.c = 2
    def SetA(self, Input):
        self.a = Input
    
    def SetB(self, Input):
        self.b = Input

    def SetC(self, Input):
        self.c = Input

    def PrintA(self):
        print(f'{self} a = {self.a}')

    def PrintB(self):
        print(f'{self} b = {self.b}')
    
    def PrintC(self):
        print(f'{self} c = {self.c}')

    def PrintAll(self):
        print(f'{self} All Variable :: a = {self.a}, b = {self.b}, c = {self.c}')
    

ClassRef = TestClass()
ClassRef2 = TestClass()
TestVar = 'Hello This is TestVar'