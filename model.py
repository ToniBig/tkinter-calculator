from abc import ABC, abstractmethod
from dataclasses import dataclass


def switch_sign(value):
    if value[0] == '-':
        value = value[1:]
    else:
        value = '-' + value
    return value


class State(ABC):

    @abstractmethod
    def on_input(self, input) -> "State":
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class BinaryOperandState(State):

    def __init__(self, unary_operand_state, value_state) -> None:
        super().__init__()
        self.unary_operand_state = unary_operand_state
        self.value_state = value_state

    def eval(self):
        return str(self.unary_operand_state.eval(self.value_state.value))

    def __str__(self) -> str:
        return str(self.value_state)

    def on_input(self, input) -> "State":
        match input:
            case 'AC':
                return InitialState()
            case 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | '+/-' | '.':
                self.value_state.on_input(input)
                return self
            case '+' | '-' | '*' | '/':
                return UnaryOperandState(input, self.eval())
            case '=':
                return ValueState(self.eval())


class UnaryOperandState(State):

    def __init__(self, operator, operand_1) -> None:
        super().__init__()
        self.operator = operator
        self.operand = operand_1

    def __str__(self) -> str:
        return str(self.operand)

    def eval(self, input) -> str:
        return str(eval(self.operand+self.operator+str(input)))

    def on_input(self, input) -> "State":
        match input:
            case 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9:
                return BinaryOperandState(self, ValueState(input))
            case 'AC':
                return InitialState()
            case '+/-':
                self.operand = switch_sign(self.operand)
                return self
            case '.':
                return ValueState(self.eval(0))
            case '+' | '-' | '*' | '/':
                return UnaryOperandState(input, self.value)
            case '=':
                return ValueState(self.eval(self.operand))


class ValueState(State):

    def __init__(self, value) -> None:
        super().__init__()
        self.value = str(value)

    def on_input(self, input) -> "State":
        match input:
            case 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9:
                self.value += str(input)
                return self
            case 'C':
                self.value = self.value[:-1]
                return self
            case 'AC':
                return InitialState()
            case '+/-':
                if self.value[0] == '-':
                    self.value = self.value[1:]
                else:
                    self.value = '-' + self.value
                return self
            case '.':
                if '.' not in self.value:
                    self.value += '.'
                return self
            case '+' | '-' | '*' | '/':
                return UnaryOperandState(input, self.value)

    def __str__(self) -> str:
        return str(self.value)


class InitialState(State):

    def on_input(self, input):
        match input:
            case 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9:
                return ValueState(input)
        return self

    def __str__(self) -> str:
        return '0.0'


@dataclass
class Calculator:

    def __init__(self, text) -> None:
        self.state = InitialState()
        self.text = text

    def on_input(self, input):
        self.state = self.state.on_input(input)
        self.text.set(str(self.state))
        

def main():
    pass


if __name__ == '__main__':
    main()