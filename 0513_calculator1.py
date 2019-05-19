# coding=utf-8
from tkinter import *


def frame(root, side):  # 创建条形框架
    w = Frame(root)
    w.pack(side=side, expand=YES, fill=BOTH)
    return w


def button(root, side, text, command=None):  # 创建按钮
    w = Button(root, text=text, command=command)
    w.pack(side=side, expand=YES, fill=BOTH)
    return w


class Calculator(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title('计算器')  # 表示顶层
        display = StringVar()
        Entry(self, textvariable=display).pack(side=TOP, expand=YES, fill=BOTH)

        for key in ('123', '456', '789', '-0.'):
            keyf = frame(self, TOP)
            for char in key:
                button(keyf, LEFT, char, lambda w=display, c=char: w.set(w.get() + c))

        opsf = frame(self, TOP)
        for char in '+*/=':
            if char == '=':
                btn = button(opsf, LEFT, char)
                btn.bind('<ButtonRelease -1>', lambda w=display, s=self: s.calc(w))
            else:
                btn = button(opsf, LEFT, char, lambda w=display, c=char: w.set(w.get() + c))

        clearf = frame(self, BOTTOM)
        button(clearf, LEFT, 'c', lambda w=display: w.set(''))

    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            print
            1


if __name__ == '__main__':
    Calculator().mainloop()
