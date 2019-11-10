from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tkinter import *
import os

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.extension = ['jpg', 'png', 'jpeg']
        self.total_price = 0
        self.master = master
        self.window_settings()
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        self.menu01 = Button(self, text="페페로니 피자\n가격: 10000", command=lambda:self.menu_button_cmd('10000'))
        self.menu01.pack(side="left")

        self.menu02 = Button(self, text="치즈 피자\n가격: 10000", command=lambda:self.menu_button_cmd('10000'))
        self.menu02.pack(side="left")

        self.menu03 = Button(self, text="포테이토 피자\n가격: 11000", command=lambda:self.menu_button_cmd('11000'))
        self.menu03.pack(side="left")

        self.menu04 = Button(self, text="불고기 피자\n가격: 11000", command=lambda:self.menu_button_cmd('11000'))
        self.menu04.pack(side="left")

        self.menu05 = Button(self, text="치즈 오븐 스파게티\n가격: 5000", command=lambda:self.menu_button_cmd('5000'))
        self.menu05.pack(side="left")

        self.price_entry = Entry(self, width=20)
        self.price_entry.pack(side="left")

        self.quit = Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def window_settings(self):
        self.master.title("test")
        self.master.geometry("800x400+400+240")
        self.master.resizable(False, False)

    def menu_button_cmd(self, value):
        print(value)
        int_value = int(value)
        self.total_price += int_value
        self.price_entry.delete(0, 'end')
        self.price_entry.insert(0, self.total_price)
        return

    def read_image(self):

        return

        
def main():
    root = Tk()
    app = Application(master=root)
    app.mainloop()


if __name__ == '__main__':
    main()