from abc import ABC, abstractmethod
from numpy import double

class Expression(ABC):
    @abstractmethod
    def calc(self) -> double:
        pass

class Num(Expression):
    def __init__(self, value):
        self.value = value

    def calc(self) -> double:
        return double(self.value)

class BinExp(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Plus(BinExp):
    def calc(self) -> double:
        return self.left.calc() + self.right.calc()

class Minus(BinExp):
    def calc(self) -> double:
        return self.left.calc() - self.right.calc()

class Mul(BinExp):
    def calc(self) -> double:
        return self.left.calc() * self.right.calc()

class Div(BinExp):
    def calc(self) -> double:
        return self.left.calc() / self.right.calc()

def parse_num(s, pos):
    num_str = ''
    while pos < len(s) and (s[pos].isdigit() or s[pos] == '.'):
        num_str += s[pos]
        pos += 1
    return Num(float(num_str)), pos

def parse_factor(s, pos):
    if s[pos] == '(':
        pos += 1
        exp, pos = parse_expression(s, pos)
        if s[pos] == ')':
            pos += 1
            return exp, pos
        else:
            raise ValueError("Expected closing parenthesis")
    elif s[pos] == '-':
        pos += 1
        num, pos = parse_num(s, pos)
        return Minus(Num(0), num), pos
    elif s[pos].isdigit():
        return parse_num(s, pos)
    else:
        raise ValueError("Unexpected token")
def parse_term(s, pos):
    left, pos = parse_factor(s, pos)
    while pos < len(s) and (s[pos] == '*' or s[pos] == '/'):
        op = s[pos]
        pos += 1
        right, pos = parse_factor(s, pos)
        if op == '*':
            left = Mul(left, right)
        else:
            left = Div(left, right)
    return left, pos

def parse_expression(s, pos):
    left, pos = parse_term(s, pos)
    while pos < len(s) and (s[pos] == '+' or s[pos] == '-'):
        op = s[pos]
        pos += 1
        right, pos = parse_term(s, pos)
        if op == '+':
            left = Plus(left, right)
        else:
            left = Minus(left, right)
    return left, pos

def parser(expression) -> double:
    result, _ = parse_expression(expression, 0)
    return result.calc()
