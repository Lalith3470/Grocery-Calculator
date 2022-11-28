import tkinter

import client


class Shop:
    def __init__(self, master):
        # build the gui

        self.client = client.Client()
        self.prices = self.client.get_prices()
        print(self.prices)

        # add the apple widgets
        self.apple_img = tkinter.PhotoImage(file='res/apple.png')
        self.apple_info = tkinter.StringVar()
        self.apple_info.set('Apples %.2fRs' % (self.prices['apple']))
        self.apple_label = tkinter.Label(textvariable=self.apple_info, image=self.apple_img,
                                         width=250, height=250, compound=tkinter.TOP)
        self.apple_label.config(font=("console", 18, 'bold'))
        self.apple_label.grid(row=0, column=1)
        self.apple_label.configure(background='white')
        self.apple_spin = tkinter.Spinbox(from_=0, to=100, font=("console", 20, 'bold'), width=5, state='readonly')
        self.apple_spin.grid(row=1, column=1)

        # add the banana widgets
        self.banana_img = tkinter.PhotoImage(file='res/banana.png')
        self.banana_info = tkinter.StringVar()
        self.banana_info.set('Banana %.2fRs' % (self.prices['banana']))
        self.banana_label = tkinter.Label(textvariable=self.banana_info, image=self.banana_img,
                                          width=250, height=250, compound=tkinter.TOP)
        self.banana_label.config(font=("console", 18, 'bold'))
        self.banana_label.grid(row=0, column=2)
        self.banana_label.configure(background='white')
        self.banana_spin = tkinter.Spinbox(from_=0, to=100, font=("console", 20, 'bold'), width=5, state='readonly')
        self.banana_spin.grid(row=1, column=2)

        # add the orange widgets
        self.orange_img = tkinter.PhotoImage(file='res/orange.png')
        self.orange_info = tkinter.StringVar()
        self.orange_info.set('Orange %.2fRs' % (self.prices['orange']))
        self.orange_label = tkinter.Label(textvariable=self.orange_info, image=self.orange_img,
                                          width=250, height=250, compound=tkinter.TOP)
        self.orange_label.config(font=("console", 18, 'bold'))
        self.orange_label.grid(row=0, column=3)
        self.orange_label.configure(background='white')
        self.orange_spin = tkinter.Spinbox(from_=0, to=100, font=("console", 20, 'bold'), width=5, state='readonly')
        self.orange_spin.grid(row=1, column=3)

        # add the strawberry widgets
        self.strb_img = tkinter.PhotoImage(file='res/strawberry.png')
        self.strb_info = tkinter.StringVar()
        self.strb_info.set('Strawberry %.2fRs' % (self.prices['strawberry']))
        self.strb_label = tkinter.Label(textvariable=self.strb_info, image=self.strb_img, width=250,
                                        height=250, compound=tkinter.TOP)
        self.strb_label.config(font=("console", 18, 'bold'))
        self.strb_label.grid(row=0, column=4)
        self.strb_label.configure(background='white')
        self.strb_spin = tkinter.Spinbox(from_=0, to=100, font=("console", 20, 'bold'), width=5, state='readonly')
        self.strb_spin.grid(row=1, column=4)

        # add total cost label
        self.total_cost = tkinter.StringVar()
        self.total_cost.set("Total Cost is 0Rs")
        self.total_cost_widget = tkinter.Label(textvariable=self.total_cost, font=("console", 20, 'bold'))
        self.total_cost_widget.configure(background='white')
        self.total_cost_widget.grid(row=3, column=3)

        # add the checkout button
        self.check_out = tkinter.Button(text="checkout", command=self.checkout, font=("console", 20, 'bold'))
        self.check_out.grid(row=3, columns=2)

    def checkout(self):
        # get the purchased list
        purchased = dict()
        purchased['apple'] = int(self.apple_spin.get())
        purchased['orange'] = int(self.orange_spin.get())
        purchased['banana'] = int(self.banana_spin.get())
        purchased['strawberry'] = int(self.strb_spin.get())
        # get total
        cost = self.client.get_cash(purchased)
        print("cost is")
        print(cost)
        self.total_cost.set("Total Cost is %.2fRs" % cost)


root = tkinter.Tk()
root.minsize(320, 240)
root.configure(background='white')
root.grid_rowconfigure(2, minsize=100)
root.grid_rowconfigure(4, minsize=100)

obj = Shop(root)
root.mainloop()
