from tkinter import Tk, N, S, E, W, StringVar
from tkinter import ttk
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


root = Tk()


@dataclass
class Calculator:

    def __init__(self) -> None:
        self.state = InitialState()
        self.text = StringVar()

    def on_input(self, input):
        self.state = self.state.on_input(input)
        self.text.set(str(self.state))


calculator = Calculator()

text = StringVar()

content = ttk.Frame(root, padding=(5, 5, 5, 5))

field = ttk.Entry(content, textvariable=calculator.text)
button_0 = ttk.Button(
    content, text='0', command=lambda: calculator.on_input(0))
button_1 = ttk.Button(
    content, text='1', command=lambda: calculator.on_input(1))
button_2 = ttk.Button(
    content, text='2', command=lambda: calculator.on_input(2))
button_3 = ttk.Button(
    content, text='3', command=lambda: calculator.on_input(3))
button_4 = ttk.Button(
    content, text='4', command=lambda: calculator.on_input(4))
button_5 = ttk.Button(
    content, text='5', command=lambda: calculator.on_input(5))
button_6 = ttk.Button(
    content, text='6', command=lambda: calculator.on_input(6))
button_7 = ttk.Button(
    content, text='7', command=lambda: calculator.on_input(7))
button_8 = ttk.Button(
    content, text='8', command=lambda: calculator.on_input(8))
button_9 = ttk.Button(
    content, text='9', command=lambda: calculator.on_input(9))
button_clear = ttk.Button(
    content, text='C', command=lambda: calculator.on_input('C'))
button_all_clear = ttk.Button(
    content, text='AC', command=lambda: calculator.on_input('AC'))
button_comma = ttk.Button(
    content, text='.', command=lambda: calculator.on_input('.'))
button_plus_minus = ttk.Button(
    content, text='+/-', command=lambda: calculator.on_input('+/-'))
button_plus = ttk.Button(
    content, text='+', command=lambda: calculator.on_input('+'))
button_minus = ttk.Button(
    content, text='-', command=lambda: calculator.on_input('-'))
button_mult = ttk.Button(
    content, text='*', command=lambda: calculator.on_input('*'))
button_div = ttk.Button(
    content, text='/', command=lambda: calculator.on_input('/'))
button_equal = ttk.Button(
    content, text='=', command=lambda: calculator.on_input('='))

content.grid(column=0, row=0, sticky=(N, S, E, W))

field.grid(column=0, row=0, columnspan=5, sticky=(N, S, E, W))

button_8.grid(column=0, row=1, sticky=(N, S, E, W))
button_7.grid(column=1, row=1, sticky=(N, S, E, W))
button_9.grid(column=2, row=1, sticky=(N, S, E, W))

button_4.grid(column=0, row=2, sticky=(N, S, E, W))
button_5.grid(column=1, row=2, sticky=(N, S, E, W))
button_6.grid(column=2, row=2, sticky=(N, S, E, W))

button_1.grid(column=0, row=3, sticky=(N, S, E, W))
button_2.grid(column=1, row=3, sticky=(N, S, E, W))
button_3.grid(column=2, row=3, sticky=(N, S, E, W))

button_plus_minus.grid(column=0, row=4, sticky=(N, S, E, W))
button_0.grid(column=1, row=4, sticky=(N, S, E, W))
button_comma.grid(column=2, row=4, sticky=(N, S, E, W))

button_clear.grid(column=3, row=1, sticky=(N, S, E, W))
button_all_clear.grid(column=4, row=1, sticky=(N, S, E, W))

button_plus.grid(column=3, row=2, sticky=(N, S, E, W))
button_minus.grid(column=4, row=2, sticky=(N, S, E, W))
button_mult.grid(column=3, row=3, sticky=(N, S, E, W))
button_div.grid(column=4, row=3, sticky=(N, S, E, W))
button_equal.grid(column=3, row=4, columnspan=2, sticky=(N, S, E, W))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=1)
content.columnconfigure(1, weight=1)
content.columnconfigure(2, weight=1)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(0, weight=1)
content.rowconfigure(1, weight=1)
content.rowconfigure(2, weight=1)
content.rowconfigure(3, weight=1)
content.rowconfigure(4, weight=1)

root.mainloop()
