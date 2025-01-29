# Static method and class method
class Calculator:
    calculation_type = "Arithiemtic Operations"
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # def __str__(self):
    #     return f" The Sum is: {self.a + self.b} "
    @staticmethod
    def add(a, b):
        return a + b
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
    
