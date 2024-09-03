class arithmetic:

    def __init__(self, a,b):
        self.a = a
        self.b = b

    def sum (self):
        return self.a+self.b

    def sub (self):
        return self.a - self.b

    def mod(self):
        return self.a % self.b

numbers = arithmetic(3,5)
print(numbers.mod())
