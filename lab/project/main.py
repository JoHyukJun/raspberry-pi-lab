from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tkinter import *
from PIL import ImageTk
from PIL import Image
import os

from menu import Menu

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.total_price = 0
        self.current_menu = []
        self.current_menu_num = []
        self.current_menu_text = StringVar()
        self.master = master
        self.window_settings()

        #self.pack()
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        base_folder = os.path.dirname(__file__)
        image_path = os.path.join(base_folder, 'testimage.png')
        test = Image.open(image_path)
        test = test.resize((100, 100), Image.ANTIALIAS)
        print(image_path)
        pht = ImageTk.PhotoImage(test)

        # self.labeltest = Label(self, image=pht)
        # self.labeltest.image = pht
        # self.labeltest.grid()

        self.menu01 = Button(self, image=pht, compound=TOP, text="페페로니 피자\n가격: 10000", command=lambda:self.menu_button_cmd('10000', self.menu01['text']))
        self.menu01.config(width=130, height=130)
        self.menu01.image = pht

        self.menu02 = Button(self, text="치즈 피자\n가격: 10000", command=lambda:self.menu_button_cmd('10000', self.menu02['text']))
        self.menu02.config(width=15, height=10)

        self.menu03 = Button(self, text="포테이토 피자\n가격: 11000", command=lambda:self.menu_button_cmd('11000', self.menu03['text']))
        self.menu03.config(width=15, height=10)

        self.menu04 = Button(self, text="불고기 피자\n가격: 11000", command=lambda:self.menu_button_cmd('11000', self.menu04['text']))
        self.menu04.config(width=15, height=10)

        self.menu05 = Button(self, text="치즈오븐 스파게티\n가격: 5000", command=lambda:self.menu_button_cmd('5000', self.menu05['text']))
        self.menu05.config(width=15, height=10)

        self.menu06 = Button(self, text="콜라\n가격: 2000", command=lambda:self.menu_button_cmd('2000', self.menu06['text']))
        self.menu06.config(width=15, height=10)

        self.menu07 = Button(self, text="사이다\n가격: 2000", command=lambda:self.menu_button_cmd('2000', self.menu07['text']))
        self.menu07.config(width=15, height=10)

        self.menu08 = Button(self, text="환타\n가격: 2000", command=lambda:self.menu_button_cmd('2000', self.menu08['text']))
        self.menu08.config(width=15, height=10)


        self.current_menu_label = Label(self, textvariable=self.current_menu_text)
        self.current_menu_label.grid(row=0, column=5, rowspan=2, sticky='n')


        self.price_entry = Entry(self, width=20)
        self.price_entry.insert(0, "주문금액: 0")

        self.order_button = Button(self, text="주 문")
        self.order_button.config(width=15, height=5)

        self.refresh_botton = Button(self, text="초기화", command=lambda:self.refresh_button_cmd(''))
        self.refresh_botton.config(width=15, height=3)

        # layout settings.
        self.menu01.grid(row=0, column=1, padx=5, pady=5)
        self.menu02.grid(row=1, column=1, padx=5, pady=5)
        self.menu03.grid(row=0, column=2, padx=5, pady=5)
        self.menu04.grid(row=1, column=2, padx=5, pady=5)
        self.menu05.grid(row=0, column=3, padx=5, pady=5)
        self.menu06.grid(row=1, column=3, padx=5, pady=5)
        self.menu07.grid(row=0, column=4, padx=5, pady=5)
        self.menu08.grid(row=1, column=4, padx=5, pady=5)
        self.price_entry.grid(row=1, column=5, sticky='n')
        self.order_button.grid(row=1, column=5)
        self.refresh_botton.grid(row=2, column=5)

    def window_settings(self):
        self.master.title("test")
        self.master.geometry("800x400+400+240")
        self.master.resizable(False, False)

    def menu_button_cmd(self, value, text):
        print(value)
        print(text)

        temp_str = ""
        temp_cnt = 0
        int_value = int(value)
        self.total_price += int_value
        self.price_entry.delete(0, 'end')
        self.price_entry.insert(0, self.total_price)
        self.price_entry.insert(0, "주문금액: ")

        if any(text in s for s in self.current_menu):
            for idx, cur in enumerate(self.current_menu):
                if text in cur:
                    self.current_menu_num[idx] += 1
        else:
            self.current_menu.append(text)
            self.current_menu_num.append(1)

        print(self.current_menu)
        print(self.current_menu_num)

        for idx, val in enumerate(self.current_menu):
            temp_str += self.current_menu[idx] + " x " + str(self.current_menu_num[idx]) + "개\n"


        self.current_menu_text.set(temp_str)
        return

    def refresh_button_cmd(self, value):
        self.total_price = 0
        self.price_entry.delete(0, 'end')
        self.price_entry.insert(0, self.total_price)
        self.price_entry.insert(0, "주문금액: ")
        
        self.current_menu = []
        self.current_menu_num = []
        self.current_menu_text.set("")
        return
    
    def order_button_cmd(self, value):

        return

    def read_image(self):
        return


def main():
    root = Tk()
    app = Application(master=root)
    app.mainloop()



if __name__ == '__main__':
    main()

