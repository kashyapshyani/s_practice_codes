class NumString:

    def __init__(self, value):
        self.value = str(value)

    def __int__(self):
        return int(self.value)

    def __str__(self):
        return self.value

    def __add__(self, other):
        return int(self) + other

    def __iadd__(self, other):
        self.value = self + other
        return self.value




some_num1 = NumString(10)
num=10
print(num.__add__(5) )
some_num1 += 9
print(some_num1)