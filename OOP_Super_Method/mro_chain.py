class A:
    def __init__(self) -> None:
        print("In Class A")
        super().__init__()

class B(A):
    def __init__(self) -> None:
        print("In Class B")
        super().__init__()

class X:
    def __init__(self) -> None:
        print("In Class X")
        super().__init__()

class Forward(B, X):
    def __init__(self) -> None:
        print("In Class Forward")
        super().__init__()

class Backward(X, B):
    def __init__(self) -> None:
        print("In Class Backward")
        super().__init__()

# Forward -> B -> A (no parent so go to next class) -> X
# THe order of inheritance changes what methods get called in what order.
obj = Forward()
