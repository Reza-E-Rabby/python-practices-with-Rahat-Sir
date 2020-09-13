from Calculator_Helper import text_Helper


class Calculator:
    def __init__(self, number1: int, number2: int):
        self.number1 = number1
        self.number2 = number2

    def add_Numbers(self):
        # return self.number1 + self.number2
        return f'The Addition{text_Helper(self.number1, self.number2)} {self.number1 + self.number2}'

    def sub_Numbers(self):
        # return self.number1 - self.number2
        return f'The Subtraction{text_Helper(self.number1, self.number2)} {self.number1 - self.number2}'


if __name__ == '__main__':
    input1 = input('Insert Number 1: ')
    input2 = input('Insert Number 2: ')
    calculator = Calculator(number1=int(input1), number2=int(input2))
    print(f'{calculator.add_Numbers()}')
    print(f'{calculator.sub_Numbers()}')
