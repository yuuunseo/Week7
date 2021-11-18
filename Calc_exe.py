class plus:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        result = num1 + num2
        print(num1, '+', num2, '은', result, '입니다.')

class minus:
    def __init__(self, num1, num2):
        result = num1 - num2
        print(num1, '-', num2, '은', result, '입니다.')

class multi:
    def __init__(self, num1, num2):
        result = num1 * num2
        print(num1, '*', num2, '은', result, '입니다.')

class div:
    def __init__(self, num1, num2):
        result = num1 / num2
        print(num1, '/', num2, '은', result, '입니다.')


