from model import Calculator

from tkinter import Tk, N, S, E, W, StringVar
from tkinter import ttk


class CalculatorApp():

    def key_pressed(self, event):
        print(event.keysym)
        match event.keysym:
            case 'BackSpace':
                self.calculator.on_input('C')
            case 'Escape':
                self.calculator.on_input('AC')
            case 'Return':
                self.calculator.on_input('=')
            case 'plus':
                self.calculator.on_input('+')
            case 'minus':
                self.calculator.on_input('-')
            case 'slash':
                self.calculator.on_input('/')
            case 'asterisk':
                self.calculator.on_input('*')
        self.calculator.on_input(event.keysym)

    def add_button(self, key, column, row, columnspan=1):
        button = ttk.Button(
            self.content, text=key,
            command=lambda: self.calculator.on_input(key))
        button.grid(column=column, row=row, sticky=(
            N, S, E, W), columnspan=columnspan)

    def __init__(self) -> None:

        # root widget with global key binding, to consume keyboard input
        self.root = Tk()
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.bind('<Key>', self.key_pressed)

        self.text = StringVar()
        self.calculator = Calculator(self.text)

        self.content = ttk.Frame(self.root, padding=(5, 5, 5, 5))
        self.content.grid(column=0, row=0, sticky=(N, S, E, W))
        for i in range(5):
            self.content.columnconfigure(i, weight=1)
            self.content.rowconfigure(i, weight=1)

        field = ttk.Entry(self.content, state="readonly",
                          textvariable=self.text)
        field.grid(column=0, row=0, columnspan=5, sticky=(N, S, E, W))

        # number buttons
        self.add_button('0', 1, 4)
        self.add_button('1', 0, 3)
        self.add_button('2', 1, 3)
        self.add_button('3', 2, 3)
        self.add_button('4', 0, 2)
        self.add_button('5', 1, 2)
        self.add_button('6', 2, 2)
        self.add_button('7', 0, 1)
        self.add_button('8', 1, 1)
        self.add_button('9', 2, 1)

        # function buttons
        self.add_button('+/-', 0, 4)
        self.add_button('.', 2, 4)
        self.add_button('C', 3, 1)
        self.add_button('AC', 4, 1)
        self.add_button('+', 3, 2)
        self.add_button('-', 4, 2)
        self.add_button('*', 3, 3)
        self.add_button('/', 4, 3)
        self.add_button('=', 3, 4, 2)

    def run(self):
        self.root.mainloop()
