"""
4.              PREDICT AND VERIFY 
                ******************
    * Create a diamond-shaped inheritance structure with four classes.
    * Before running the program, write down what you believe the MRO will be.
    * Then print the actual MRO and compare it with your prediction.
"""

class A:
    def __init__(self):
        super().__init__()
        print(f'In class A.__init__')

class B(A):
    def __init__(self):
        super().__init__()
        print(f'In class B.__init__')

class C(A):
    def __init__(self):
        super().__init__()
        print(f'In class C.__init__')

class D(B, C):
    def __init__(self):
        super().__init__()
        print(f'In class D.__init__')

obj = D()
print(D.mro())