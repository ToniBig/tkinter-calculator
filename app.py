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

    def __init__(self) -> None:

        self.root = Tk()
        self.text = StringVar()

        self.calculator = Calculator(self.text)

        content = ttk.Frame(self.root, padding=(5, 5, 5, 5))

        field = ttk.Entry(content, state="readonly", textvariable=self.text)
        self.root.bind('<Key>', self.key_pressed)

        button_0 = ttk.Button(
            content, text='0', command=lambda: self.calculator.on_input('0'))

        button_1 = ttk.Button(
            content, text='1', command=lambda: self.calculator.on_input('1'))
        button_1.grid(column=0, row=3, sticky=(N, S, E, W))

        button_2 = ttk.Button(
            content, text='2', command=lambda: self.calculator.on_input('2'))
        button_3 = ttk.Button(
            content, text='3', command=lambda: self.calculator.on_input('3'))
        button_4 = ttk.Button(
            content, text='4', command=lambda: self.calculator.on_input('4'))
        button_5 = ttk.Button(
            content, text='5', command=lambda: self.calculator.on_input('5'))
        button_6 = ttk.Button(
            content, text='6', command=lambda: self.calculator.on_input('6'))
        button_7 = ttk.Button(
            content, text='7', command=lambda: self.calculator.on_input('7'))
        button_8 = ttk.Button(
            content, text='8', command=lambda: self.calculator.on_input('8'))
        button_9 = ttk.Button(
            content, text='9', command=lambda: self.calculator.on_input('9'))
        button_clear = ttk.Button(
            content, text='C', command=lambda: self.calculator.on_input('C'))
        button_all_clear = ttk.Button(
            content, text='AC', command=lambda: self.calculator.on_input('AC'))
        button_comma = ttk.Button(
            content, text='.', command=lambda: self.calculator.on_input('.'))
        button_plus_minus = ttk.Button(
            content, text='+/-', command=lambda: self.calculator.on_input('+/-'))
        button_plus = ttk.Button(
            content, text='+', command=lambda: self.calculator.on_input('+'))
        button_minus = ttk.Button(
            content, text='-', command=lambda: self.calculator.on_input('-'))
        button_mult = ttk.Button(
            content, text='*', command=lambda: self.calculator.on_input('*'))
        button_div = ttk.Button(
            content, text='/', command=lambda: self.calculator.on_input('/'))
        button_equal = ttk.Button(
            content, text='=', command=lambda: self.calculator.on_input('='))

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

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
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

    def run(self):
        self.root.mainloop()
