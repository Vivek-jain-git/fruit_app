from tkinter import *
from PIL import Image,ImageTk
from main_gui import main2
from tkinter import messagebox
class main:
    def __init__(self):
        self.root=Tk()
        self.main=main2()
        self.bcount=0
        self.acount=0
        self.ocount=0
        self.root.title('FRUIT APP')
        self.root.iconbitmap('Images/favicon.ico')
        self.root.geometry('{}x{}'.format(self.root.winfo_screenwidth(),self.root.winfo_screenheight()))
        self.root.configure(bg='#efedf1')
        self.main_screen()
        self.root.mainloop()
    def main_screen(self):
        self.clear()
        app_label=Label(self.root,text='FRUIT APP',bg='#efedf1',fg='black')
        app_label.configure(font=('Comic Sans MS',30,'bold underline'))
        app_label.pack(pady=(25,20))

        cart_button=Button(self.root,text='MY Cart',command=self.cart_)
        cart_button.configure(font=('Comic Sans MS',10,'bold'))
        cart_button.place(relx=1, x=-20, y=32, anchor=NE,width=80,height=40)
        self.a=(self.bcount == 0 and self.acount==0 and self.ocount==0)
        if self.a:
            self.cart_image("Images/0.png")
        elif self.bcount == 1 and self.acount==1 and self.ocount==1:
            self.cart_image("Images/3.png")
        elif (self.bcount == 1 and self.acount==1) or (self.acount==1 and self.ocount==1) or (self.ocount==1 and self.bcount==1):
            self.cart_image("Images/2.png")
        else:
            self.cart_image("Images/1.png")

    def cart_image(self,path):
        image1 = Image.open(path)
        img1 = ImageTk.PhotoImage(image1.resize((20, 20)))
        zero = Label(self.root, image=img1, bg='#efedf1')
        zero.photo = img1
        zero.place(x=1890, y=32)
        self.about_button_()

    def about_button_(self):
        about_button = Button(self.root, text='About',command=self.about_text)
        about_button.configure(font=('Comic Sans MS', 10, 'bold'))
        about_button.place(x=20, y=32, anchor=NW, width=80, height=40)
        self.main_contents()
    def main_contents(self):
        canvas=Canvas(bg='#efedf1',width=900,height=800,highlightbackground='black',highlightthickness=5)
        canvas.place(x=510,y=150)
        self.banana_()
    def banana_(self):
        path1 = "Images/banana.png"
        image1=Image.open(path1)
        img1 = ImageTk.PhotoImage(image1.resize((200,200)))
        banana = Label(self.root, image=img1,bg='#efedf1')
        banana.photo = img1
        banana.place(x=600,y=170)

        banana_quan = Label(self.root, text='Quantity (KG)     :', bg='#efedf1', fg='black')
        banana_quan.configure(font=('Comic Sans MS', 15))
        banana_quan.place(x=900,y=220)

        banana_price = Label(self.root, text='Price (per KG)     :', bg='#efedf1', fg='black')
        banana_price.configure(font=('Comic Sans MS', 15))
        banana_price.place(x=900, y=280)

        self.quan_b = Label(self.root, text=self.main.b_quan, bg='#efedf1', fg='black')
        self.quan_b.configure(font=('Comic Sans MS', 15))
        self.quan_b.place(x=1100, y=220)

        price_b = Label(self.root, text=self.main.b_price, bg='#efedf1', fg='black')
        price_b.configure(font=('Comic Sans MS', 15))
        price_b.place(x=1100, y=280)

        banana_button = Button(self.root, text='Buy', width=15, height=1, command=self.banana_buy)
        banana_button.configure(font=('Comic Sans MS', 10))
        banana_button.place(x=1200, y=245)

        self.apple_()


    def apple_(self):
        path2 = "Images/apple.png"
        image2 = Image.open(path2)
        img2 = ImageTk.PhotoImage(image2.resize((200, 200)))
        apple = Label(self.root, image=img2, bg='#efedf1')
        apple.photo = img2
        apple.place(x=600, y=450)

        apple_quan = Label(self.root, text='Quantity (KG)     :', bg='#efedf1', fg='black')
        apple_quan.configure(font=('Comic Sans MS', 15))
        apple_quan.place(x=900, y=500)

        apple_price = Label(self.root, text='Price (per KG)     :', bg='#efedf1', fg='black')
        apple_price.configure(font=('Comic Sans MS', 15))
        apple_price.place(x=900, y=560)

        apple_button = Button(self.root, text='Buy', width=15, height=1,command=self.apple_buy)
        apple_button.configure(font=('Comic Sans MS', 10))
        apple_button.place(x=1200, y=530)

        quan_a = Label(self.root, text=self.main.a_quan, bg='#efedf1', fg='black')
        quan_a.configure(font=('Comic Sans MS', 15))
        quan_a.place(x=1100, y=500)

        price_a = Label(self.root, text=self.main.a_price, bg='#efedf1', fg='black')
        price_a.configure(font=('Comic Sans MS', 15))
        price_a.place(x=1100, y=560)
        self.orange_()

    def orange_(self):
        path3 = "Images/orange.png"
        image3 = Image.open(path3)
        img3 = ImageTk.PhotoImage(image3.resize((200, 200)))
        orange = Label(self.root, image=img3, bg='#efedf1')
        orange.photo = img3
        orange.place(x=600, y=730)

        orange_quan = Label(self.root, text='Quantity (KG)     :', bg='#efedf1', fg='black')
        orange_quan.configure(font=('Comic Sans MS', 15))
        orange_quan.place(x=900, y=760)

        orange_price = Label(self.root, text='Price (per KG)     :', bg='#efedf1', fg='black')
        orange_price.configure(font=('Comic Sans MS', 15))
        orange_price.place(x=900, y=820)

        orange_button = Button(self.root, text='Buy', width=15, height=1,command=self.orange_buy)
        orange_button.configure(font=('Comic Sans MS', 10))
        orange_button.place(x=1200, y=780)

        quan_o = Label(self.root, text=self.main.o_quan, bg='#efedf1', fg='black')
        quan_o.configure(font=('Comic Sans MS', 15))
        quan_o.place(x=1100, y=760)

        price_o = Label(self.root, text=self.main.o_price, bg='#efedf1', fg='black')
        price_o.configure(font=('Comic Sans MS', 15))
        price_o.place(x=1100, y=820)

    def error_handling(self,fruit,quan_value,yes=1):
        response = self.main.after_display(fruit,quan_value,yes)
        if response==-1:
            messagebox.showerror('Error','Please enter integer quantity')
        if response == 0:
            messagebox.showerror('Error', 'PLease enter positive quantity')
        elif response == 1:
            messagebox.showerror('Error', 'Please enter more quantity')
        elif response == 2:
            messagebox.showerror('Error', "Please enter quantity lesser than the stock quantity")
        elif response == 3:
            messagebox.showerror('Error', "The stock for the particular fruit has been sold . Please buy another fruit")
        elif response == 4:
            if fruit=='banana':
                res = messagebox.askquestion('Confirm','The total price of your purchase is {} \nDo you really want to buy ?'.format(int(quan_value) * self.main.b_price))
                if res == 'yes':
                    self.quan_b['text'] = self.main.b_quan
                    messagebox.showinfo('Congrats', 'Added to Cart ! \nCheck out now to proceed to payment')
                    self.bcount=1
                    self.purbquan=self.main.b_quan+self.main.quan
                    self.main_screen()
                else:
                    response2=self.main.after_display('banana',self.enter_quan.get(),0)
                    if response2==5:
                        self.quan_b['text']=self.main.b_quan
                        self.banana_buy()
            elif fruit=='apple':
                res = messagebox.askquestion('Confirm','The total price of your purchase is {} \n Do you really want to buy ?'.format(int(quan_value) * self.main.a_price))
                if res == 'yes':
                    self.quan_a['text'] = self.main.a_quan
                    messagebox.showinfo('Congrats', 'Added to Cart ! \nCheck out now to proceed to payment')
                    self.acount = 1
                    self.puraquan=self.main.a_quan+self.main.quan
                    self.main_screen()
                else:
                    response2 = self.main.after_display('apple', self.enter_quan2.get(), 0)
                    if response2 == 5:
                        self.quan_a['text'] = self.main.a_quan
                        self.apple_buy()
            else:
                res = messagebox.askquestion('Confirm','The total price of your purchase is {} \n Do you really want to buy ?'.format(int(quan_value) * self.main.o_price))
                if res == 'yes':
                    self.quan_o['text'] = self.main.o_quan
                    messagebox.showinfo('Congrats', 'Added to Cart ! \nCheck out now to proceed to payment')
                    self.ocount = 1
                    self.puroquan=self.main.o_quan+self.main.quan
                    self.main_screen()
                else:
                    response2 = self.main.after_display('orange', self.enter_quan3.get(), 0)
                    if response2 == 5:
                        self.quan_o['text'] = self.main.o_quan
                        self.orange_buy()

    def banana_buy(self):
        if (self.main.o_quan==0 and self.main.a_quan==0 and self.main.b_quan== 0):
            res = messagebox.askquestion('Confirm','All the quantity of all fruits have been sold \nPlease check your cart')
            if res == 'yes':
                self.cart_()
            else:
                self.main_screen()
        elif self.main.b_quan==0:
            messagebox.showerror('Error','Please purchase some other fruit \nThe stock for this fruit is over')
        else:
            canvas = Canvas(bg='#efedf1', width=900, height=800, highlightbackground='black', highlightthickness=5)
            canvas.place(x=510, y=150)
            path1 = "Images/banana.png"
            image1 = Image.open(path1)
            img1 = ImageTk.PhotoImage(image1.resize((200, 200)))
            banana = Label(self.root, image=img1, bg='#efedf1')
            banana.photo = img1
            banana.place(x=600, y=170)

            banana_quan = Label(self.root, text='Quantity (KG)     :', bg='#efedf1', fg='black')
            banana_quan.configure(font=('Comic Sans MS', 15))
            banana_quan.place(x=900, y=220)

            banana_price = Label(self.root, text='Price (per KG)     :', bg='#efedf1', fg='black')
            banana_price.configure(font=('Comic Sans MS', 15))
            banana_price.place(x=900, y=280)

            label1 = Label(self.root, text='Enter Quantity ', bg='#efedf1', fg='black')
            label1.configure(font=('Comic Sans MS', 15))
            label1.place(x=900,y=330)

            self.quan_b = Label(self.root, text=self.main.b_quan, bg='#efedf1', fg='black')
            self.quan_b.configure(font=('Comic Sans MS', 15))
            self.quan_b.place(x=1100, y=220)

            price_b = Label(self.root, text=self.main.b_price, bg='#efedf1', fg='black')
            price_b.configure(font=('Comic Sans MS', 15))
            price_b.place(x=1100, y=280)

            self.enter_quan = Entry(self.root, width=20)
            self.enter_quan.configure(font=('Comic Sans MS', 10))
            self.enter_quan.place(x=900, y=380)

            banana_button=Button(self.root,text='Add to cart',width=15,height=1,command=self.banana_error_handling)
            banana_button.configure(font=('Comic Sans MS', 10))
            banana_button.place(x=1200,y=245)

            back_main_button = Button(self.root, text='<- Back',width=15,height=1,command=self.main_screen)
            back_main_button.configure(font=('Comic Sans MS', 10))
            back_main_button.place(x=1200,y=280)

    def banana_error_handling(self):
        quan_value=self.enter_quan.get()
        fruit='banana'
        self.error_handling(fruit,quan_value)

    def apple_buy(self):
        if (self.main.o_quan==0 and self.main.a_quan==0 and self.main.b_quan == 0):
            res = messagebox.askquestion('Confirm','All the quantity of all fruits have been sold \nPlease check your cart')
            if res == 'yes':
                self.cart_()
            else:
                self.main_screen()
        elif self.main.a_quan==0:
            messagebox.showerror('Error','Please purchase some other fruit \nThe stock for this fruit is over')
        else:
            canvas = Canvas(bg='#efedf1', width=900, height=800, highlightbackground='black', highlightthickness=5)
            canvas.place(x=510, y=150)
            path2 = "Images/apple.png"
            image2 = Image.open(path2)
            img2 = ImageTk.PhotoImage(image2.resize((200, 200)))
            apple = Label(self.root, image=img2, bg='#efedf1')
            apple.photo = img2
            apple.place(x=600, y=200)

            apple_quan = Label(self.root, text='Quantity (KG)     :', bg='#efedf1', fg='black')
            apple_quan.configure(font=('Comic Sans MS', 15))
            apple_quan.place(x=900, y=220)

            apple_price = Label(self.root, text='Price (per KG)     :', bg='#efedf1', fg='black')
            apple_price.configure(font=('Comic Sans MS', 15))
            apple_price.place(x=900, y=280)

            label1 = Label(self.root, text='Enter Quantity ', bg='#efedf1', fg='black')
            label1.configure(font=('Comic Sans MS', 15))
            label1.place(x=900, y=330)

            self.enter_quan2 = Entry(self.root, width=20)
            self.enter_quan2.configure(font=('Comic Sans MS', 10))
            self.enter_quan2.place(x=900, y=380)

            self.quan_a = Label(self.root, text=self.main.a_quan, bg='#efedf1', fg='black')
            self.quan_a.configure(font=('Comic Sans MS', 15))
            self.quan_a.place(x=1100, y=220)

            price_a = Label(self.root, text=self.main.a_price, bg='#efedf1', fg='black')
            price_a.configure(font=('Comic Sans MS', 15))
            price_a.place(x=1100, y=280)

            apple_button = Button(self.root, text='Add to cart', width=15, height=1,command=self.apple_error_handling)
            apple_button.configure(font=('Comic Sans MS', 10))
            apple_button.place(x=1200, y=245)

            back_main_button = Button(self.root, text='<- Back', width=15, height=1, command=self.main_screen)
            back_main_button.configure(font=('Comic Sans MS', 10))
            back_main_button.place(x=1200, y=280)

    def apple_error_handling(self):
        quan_value = self.enter_quan2.get()
        fruit = 'apple'
        self.error_handling(fruit, quan_value)


    def orange_buy(self):
        if (self.main.o_quan==0 and self.main.a_quan==0 and self.main.b_quan == 0):
            res = messagebox.askquestion('Confirm','All the quantity of all fruits have been sold \nPlease check your cart')
            if res == 'yes':
                self.cart_()
            else:
                self.main_screen()
        elif self.main.o_quan==0:
            messagebox.showerror('Error','Please purchase some other fruit \nThe stock for this fruit is over')
        else:
            canvas = Canvas(bg='#efedf1', width=900, height=800, highlightbackground='black', highlightthickness=5)
            canvas.place(x=510, y=150)
            path3 = "Images/orange.png"
            image3 = Image.open(path3)
            img3 = ImageTk.PhotoImage(image3.resize((200, 200)))
            orange = Label(self.root, image=img3, bg='#efedf1')
            orange.photo = img3
            orange.place(x=600, y=200)

            orange_quan = Label(self.root, text='Quantity (KG)     :', bg='#efedf1', fg='black')
            orange_quan.configure(font=('Comic Sans MS', 15))
            orange_quan.place(x=900, y=220)

            orange_price = Label(self.root, text='Price (per KG)     :', bg='#efedf1', fg='black')
            orange_price.configure(font=('Comic Sans MS', 15))
            orange_price.place(x=900, y=280)

            label1 = Label(self.root, text='Enter Quantity ', bg='#efedf1', fg='black')
            label1.configure(font=('Comic Sans MS', 15))
            label1.place(x=900, y=330)

            self.enter_quan3 = Entry(self.root, width=20)
            self.enter_quan3.configure(font=('Comic Sans MS', 10))
            self.enter_quan3.place(x=900, y=380)

            self.quan_o = Label(self.root, text=self.main.o_quan, bg='#efedf1', fg='black')
            self.quan_o.configure(font=('Comic Sans MS', 15))
            self.quan_o.place(x=1100, y=220)

            price_o = Label(self.root, text=self.main.o_price, bg='#efedf1', fg='black')
            price_o.configure(font=('Comic Sans MS', 15))
            price_o.place(x=1100, y=280)

            orange_button = Button(self.root, text='Add to cart', width=15, height=1,command=self.orange_error_handling)
            orange_button.configure(font=('Comic Sans MS', 10))
            orange_button.place(x=1200, y=245)

            back_main_button = Button(self.root, text='<- Back', width=15, height=1, command=self.main_screen)
            back_main_button.configure(font=('Comic Sans MS', 10))
            back_main_button.place(x=1200, y=280)

    def orange_error_handling(self):
        quan_value = self.enter_quan3.get()
        fruit = 'orange'
        self.error_handling(fruit, quan_value)

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
        for j in self.root.place_slaves():
            j.destroy()
    def about_text(self):
        self.clear()
        back_button = Button(self.root, text='<- Back', command=self.main_screen)
        back_button.configure(font=('Comic Sans MS', 10, 'bold'))
        back_button.place(x=20, y=32, anchor=NW, width=80, height=40)

        about = Label(self.root, text='About', bg='#efedf1', fg='black')
        about.configure(font=('Comic Sans MS', 30, 'bold underline'))
        about.pack(pady=(25, 20))

        bg_path = "Images/fruit_background.png"
        fruit_bg = Image.open(bg_path)
        img3 = ImageTk.PhotoImage(fruit_bg)
        bg = Label(self.root, image=img3, bg='#efedf1')
        bg.photo = img3
        bg.pack()
        with open('about_text','r') as f:
            txt=f.read()
        txt=txt
        info=Label(self.root,text=txt,width=44)
        info.configure(font=('Comic Sans MS', 12, 'bold'),bg='#efedf1',fg='black')
        info.place(x=50,y=170)

    def errorpur(self,no,name,cvv):
        if (no=='' and name=='' and cvv=='') or (no=='' and name=='') or (name=='' or cvv=='') or (cvv=='' or name==''):
            return 0
        if len(no)==12:
            for i in no:
                if i.isdigit():
                    pass
                else:
                    return 1
        else:
            return 1
        for j in name:
            if j.isalpha() or j.isspace():
                pass
            else:
                return 2
        if len(cvv)==3:
            for k in cvv:
                if k.isdigit():
                    pass
                else:
                    return 3
        else:
            return 3

    def bill_label_card(self):

        details = Label(self.root, text='ENTER DETAILS', bg='#efedf1', fg='black')
        details.configure(font=('Comic Sans MS', 15,'bold underline'))
        details.place(x=1270, y=200)

        cardno = Label(self.root, text='CARD NO', bg='#efedf1', fg='black')
        cardno.configure(font=('Comic Sans MS', 15,'bold underline'))
        cardno.place(x=1300, y=280)

        name = Label(self.root, text='CARDHOLDER NAME:', bg='#efedf1', fg='black')
        name.configure(font=('Comic Sans MS', 15,'bold underline'))
        name.place(x=1240, y=380)

        cvv = Label(self.root, text='CVV', bg='#efedf1', fg='black')
        cvv.configure(font=('Comic Sans MS', 15,'bold underline'))
        cvv.place(x=1330, y=480)
    def cashbao(self):
        canvas = Canvas(bg='#efedf1', width=800, height=800, highlightbackground='black', highlightthickness=5)
        canvas.place(x=310, y=150)
        canvas = Canvas(bg='#efedf1', width=300, height=800, highlightbackground='black', highlightthickness=5)
        canvas.place(x=1200, y=150)
        path1 = "Images/banana.png"
        image1 = Image.open(path1)
        img1 = ImageTk.PhotoImage(image1.resize((200, 200)))
        banana = Label(self.root, image=img1, bg='#efedf1')
        banana.photo = img1
        banana.place(x=400, y=200)

        banana_quan = Label(self.root, text='Quantity (KG)     :', bg='#efedf1', fg='black')
        banana_quan.configure(font=('Comic Sans MS', 15))
        banana_quan.place(x=700, y=220)

        banana_price = Label(self.root, text='Price (per KG)    :', bg='#efedf1', fg='black')
        banana_price.configure(font=('Comic Sans MS', 15))
        banana_price.place(x=700, y=280)

        self.purquanb = Label(self.root, text=self.main.purbquan, bg='#efedf1', fg='black')
        self.purquanb.configure(font=('Comic Sans MS', 15))
        self.purquanb.place(x=900, y=220)

        price_b = Label(self.root, text=self.main.b_price, bg='#efedf1', fg='black')
        price_b.configure(font=('Comic Sans MS', 15))
        price_b.place(x=900, y=280)

        price_total = Label(self.root, text='Total                  :', bg='#efedf1', fg='black')
        price_total.configure(font=('Comic Sans MS', 15))
        price_total.place(x=700, y=340)

        total_price_b = Label(self.root, text=price_b['text'] * self.purquanb['text'], bg='#efedf1', fg='black')
        total_price_b.configure(font=('Comic Sans MS', 15))
        total_price_b.place(x=900, y=340)

        path2 = "Images/apple.png"
        image2 = Image.open(path2)
        img2 = ImageTk.PhotoImage(image2.resize((200, 200)))
        apple = Label(self.root, image=img2, bg='#efedf1')
        apple.photo = img2
        apple.place(x=400, y=450)

        apple_quan = Label(self.root, text='Quantity (KG)     :', bg='#efedf1', fg='black')
        apple_quan.configure(font=('Comic Sans MS', 15))
        apple_quan.place(x=700, y=500)

        apple_price = Label(self.root, text='Price (per KG)     :', bg='#efedf1', fg='black')
        apple_price.configure(font=('Comic Sans MS', 15))
        apple_price.place(x=700, y=560)

        self.purquana = Label(self.root, text=self.main.puraquan, bg='#efedf1', fg='black')
        self.purquana.configure(font=('Comic Sans MS', 15))
        self.purquana.place(x=900, y=500)

        price_a = Label(self.root, text=self.main.a_price, bg='#efedf1', fg='black')
        price_a.configure(font=('Comic Sans MS', 15))
        price_a.place(x=900, y=560)

        price_total = Label(self.root, text='Total                  :', bg='#efedf1', fg='black')
        price_total.configure(font=('Comic Sans MS', 15))
        price_total.place(x=700, y=620)

        total_price_a = Label(self.root, text=price_a['text'] * self.purquana['text'], bg='#efedf1', fg='black')
        total_price_a.configure(font=('Comic Sans MS', 15))
        total_price_a.place(x=900, y=620)

        path3 = "Images/orange.png"
        image3 = Image.open(path3)
        img3 = ImageTk.PhotoImage(image3.resize((200, 200)))
        orange = Label(self.root, image=img3, bg='#efedf1')
        orange.photo = img3
        orange.place(x=400, y=730)

        orange_quan = Label(self.root, text='Quantity (KG)     :', bg='#efedf1', fg='black')
        orange_quan.configure(font=('Comic Sans MS', 15))
        orange_quan.place(x=700, y=760)

        orange_price = Label(self.root, text='Price (per KG)     :', bg='#efedf1', fg='black')
        orange_price.configure(font=('Comic Sans MS', 15))
        orange_price.place(x=700, y=820)

        self.purquano = Label(self.root, text=self.main.puroquan, bg='#efedf1', fg='black')
        self.purquano.configure(font=('Comic Sans MS', 15))
        self.purquano.place(x=900, y=760)

        price_o = Label(self.root, text=self.main.o_price, bg='#efedf1', fg='black')
        price_o.configure(font=('Comic Sans MS', 15))
        price_o.place(x=900, y=820)

        price_total = Label(self.root, text='Total                  :', bg='#efedf1', fg='black')
        price_total.configure(font=('Comic Sans MS', 15))
        price_total.place(x=700, y=880)

        total_price_o = Label(self.root, text=price_o['text'] * self.purquano['text'], bg='#efedf1', fg='black')
        total_price_o.configure(font=('Comic Sans MS', 15))
        total_price_o.place(x=900, y=880)

        choice = Label(self.root, text='Choose any one \ncombination \nto pay', bg='#efedf1', fg='black')
        choice.configure(font=('Comic Sans MS', 20,'bold underline'))
        choice.place(x=1250,y=200)

        self.l1=Label(self.root,bg='#efedf1')
        self.l1.place(x=12600,y=300)
        def selected():
            self.l1.config(text=v1.get())


        v1 = StringVar(self.root)

        # Dictionary to create multiple buttons
        values = {"{}".format(self.l[0]): "1",
                  "{}".format(self.l[1]): "2",
                  "{}".format(self.l[2]): "3",
                  "{}".format(self.l[3]): "4",
                  "{}".format(self.l[4]): "5"}

        # Loop is used to create multiple Radiobuttons
        # rather than creating each button separately
        x=1240
        y=350
        for (text, value) in values.items():
            r=Radiobutton(self.root, text=text, variable=v1,value=value,background="light blue",command=selected)
            r.configure(font=('Comic Sans MS',10,'bold'))
            r.place(x=x,y=y)
            y+=50


        purbaocash = Button(self.root, text='PURCHASE', width=20,command=self.purbaocash)
        purbaocash.configure(font=('Comic Sans MS', 10, 'bold'))
        purbaocash.place(x=1270, y=650)

    def purbaocash(self):
        if self.l1['text']=='':
            messagebox.showerror('Error','Please select any one of the above options')
        else:
            messagebox.showinfo('Success','Your payment has been successfully made \nYour items will be delivered soon !!')
            self.root.destroy()




    def cardbao(self):
        canvas = Canvas(bg='#efedf1', width=800, height=800, highlightbackground='black', highlightthickness=5)
        canvas.place(x=310, y=150)
        canvas = Canvas(bg='#efedf1', width=300, height=800, highlightbackground='black', highlightthickness=5)
        canvas.place(x=1200, y=150)
        path1 = "Images/banana.png"
        image1 = Image.open(path1)
        img1 = ImageTk.PhotoImage(image1.resize((200, 200)))
        banana = Label(self.root, image=img1, bg='#efedf1')
        banana.photo = img1
        banana.place(x=400, y=200)

        banana_quan = Label(self.root, text='Quantity (KG)     :', bg='#efedf1', fg='black')
        banana_quan.configure(font=('Comic Sans MS', 15))
        banana_quan.place(x=700, y=220)

        banana_price = Label(self.root, text='Price (per KG)    :', bg='#efedf1', fg='black')
        banana_price.configure(font=('Comic Sans MS', 15))
        banana_price.place(x=700, y=280)

        self.purquanb = Label(self.root, text=self.main.purbquan, bg='#efedf1', fg='black')
        self.purquanb.configure(font=('Comic Sans MS', 15))
        self.purquanb.place(x=900, y=220)

        price_b = Label(self.root, text=self.main.b_price, bg='#efedf1', fg='black')
        price_b.configure(font=('Comic Sans MS', 15))
        price_b.place(x=900, y=280)

        price_total = Label(self.root, text='Total                  :', bg='#efedf1', fg='black')
        price_total.configure(font=('Comic Sans MS', 15))
        price_total.place(x=700, y=340)

        total_price_b = Label(self.root, text=price_b['text'] * self.purquanb['text'], bg='#efedf1', fg='black')
        total_price_b.configure(font=('Comic Sans MS', 15))
        total_price_b.place(x=900, y=340)

        path2 = "Images/apple.png"
        image2 = Image.open(path2)
        img2 = ImageTk.PhotoImage(image2.resize((200, 200)))
        apple = Label(self.root, image=img2, bg='#efedf1')
        apple.photo = img2
        apple.place(x=400, y=450)

        apple_quan = Label(self.root, text='Quantity (KG)     :', bg='#efedf1', fg='black')
        apple_quan.configure(font=('Comic Sans MS', 15))
        apple_quan.place(x=700, y=500)

        apple_price = Label(self.root, text='Price (per KG)     :', bg='#efedf1', fg='black')
        apple_price.configure(font=('Comic Sans MS', 15))
        apple_price.place(x=700, y=560)

        self.purquana = Label(self.root, text=self.main.puraquan, bg='#efedf1', fg='black')
        self.purquana.configure(font=('Comic Sans MS', 15))
        self.purquana.place(x=900, y=500)

        price_a = Label(self.root, text=self.main.a_price, bg='#efedf1', fg='black')
        price_a.configure(font=('Comic Sans MS', 15))
        price_a.place(x=900, y=560)

        price_total = Label(self.root, text='Total                  :', bg='#efedf1', fg='black')
        price_total.configure(font=('Comic Sans MS', 15))
        price_total.place(x=700, y=620)

        total_price_a = Label(self.root, text=price_a['text'] * self.purquana['text'], bg='#efedf1', fg='black')
        total_price_a.configure(font=('Comic Sans MS', 15))
        total_price_a.place(x=900, y=620)

        path3 = "Images/orange.png"
        image3 = Image.open(path3)
        img3 = ImageTk.PhotoImage(image3.resize((200, 200)))
        orange = Label(self.root, image=img3, bg='#efedf1')
        orange.photo = img3
        orange.place(x=400, y=730)

        orange_quan = Label(self.root, text='Quantity (KG)     :', bg='#efedf1', fg='black')
        orange_quan.configure(font=('Comic Sans MS', 15))
        orange_quan.place(x=700, y=760)

        orange_price = Label(self.root, text='Price (per KG)     :', bg='#efedf1', fg='black')
        orange_price.configure(font=('Comic Sans MS', 15))
        orange_price.place(x=700, y=820)

        self.purquano = Label(self.root, text=self.main.puroquan, bg='#efedf1', fg='black')
        self.purquano.configure(font=('Comic Sans MS', 15))
        self.purquano.place(x=900, y=760)

        price_o = Label(self.root, text=self.main.o_price, bg='#efedf1', fg='black')
        price_o.configure(font=('Comic Sans MS', 15))
        price_o.place(x=900, y=820)

        price_total = Label(self.root, text='Total                  :', bg='#efedf1', fg='black')
        price_total.configure(font=('Comic Sans MS', 15))
        price_total.place(x=700, y=880)

        total_price_o = Label(self.root, text=price_o['text'] * self.purquano['text'], bg='#efedf1', fg='black')
        total_price_o.configure(font=('Comic Sans MS', 15))
        total_price_o.place(x=900, y=880)

        self.bill_label_card()

        self.cardnobao = Entry(self.root, width=20)
        self.cardnobao.configure(font=('Comic Sans MS', 10))
        self.cardnobao.place(x=1270, y=350)

        self.cardnamebao = Entry(self.root, width=20)
        self.cardnamebao.configure(font=('Comic Sans MS', 10))
        self.cardnamebao.place(x=1270, y=450)

        self.cvvbao = Entry(self.root, width=20)
        self.cvvbao.configure(font=('Comic Sans MS', 10))
        self.cvvbao.place(x=1270, y=550)

        purbao = Button(self.root, text='PURCHASE',width=20,command=self.baoerror)
        purbao.configure(font=('Comic Sans MS', 10, 'bold'))
        purbao.place(x=1270,y=650)

    def baoerror(self):
        response=self.errorpur(self.cardnobao.get(),self.cardnamebao.get(),self.cvvbao.get())
        if response==0:
            messagebox.showerror('Error','Please fill all the blanks')
        elif response==1:
            messagebox.showerror('Error','Please enter card number with only digits / Check if it is of length 12')
        elif response==2:
            messagebox.showerror('Error','Please enter string characters in your name')
        elif response==3:
            messagebox.showerror('Error','Please enter cvv number with only digits / Check if it is of length 3')
        else:
            messagebox.showinfo('Success !!', 'Your payment has been successfully made \nYour items will be delivered soon !!')
            self.root.destroy()


    def cashba(self):
        canvas = Canvas(bg='#efedf1', width=800, height=800, highlightbackground='black', highlightthickness=5)
        canvas.place(x=310, y=150)
        canvas = Canvas(bg='#efedf1', width=300, height=800, highlightbackground='black', highlightthickness=5)
        canvas.place(x=1200, y=150)
        path1 = "Images/banana.png"
        image1 = Image.open(path1)
        img1 = ImageTk.PhotoImage(image1.resize((200, 200)))
        banana = Label(self.root, image=img1, bg='#efedf1')
        banana.photo = img1
        banana.place(x=400, y=200)

        banana_quan = Label(self.root, text='Quantity (KG)     :', bg='#efedf1', fg='black')
        banana_quan.configure(font=('Comic Sans MS', 15))
        banana_quan.place(x=700, y=220)

        banana_price = Label(self.root, text='Price (per KG)    :', bg='#efedf1', fg='black')
        banana_price.configure(font=('Comic Sans MS', 15))
        banana_price.place(x=700, y=280)

        self.purquanb = Label(self.root, text=self.main.purbquan, bg='#efedf1', fg='black')
        self.purquanb.configure(font=('Comic Sans MS', 15))
        self.purquanb.place(x=900, y=220)

        price_b = Label(self.root, text=self.main.b_price, bg='#efedf1', fg='black')
        price_b.configure(font=('Comic Sans MS', 15))
        price_b.place(x=900, y=280)

        price_total = Label(self.root, text='Total                  :', bg='#efedf1', fg='black')
        price_total.configure(font=('Comic Sans MS', 15))
        price_total.place(x=700, y=340)

        total_price_b = Label(self.root, text=price_b['text'] * self.purquanb['text'], bg='#efedf1', fg='black')
        total_price_b.configure(font=('Comic Sans MS', 15))
        total_price_b.place(x=900, y=340)

        path2 = "Images/apple.png"
        image2 = Image.open(path2)
        img2 = ImageTk.PhotoImage(image2.resize((200, 200)))
        apple = Label(self.root, image=img2, bg='#efedf1')
        apple.photo = img2
        apple.place(x=400, y=470)

        apple_quan = Label(self.root, text='Quantity (KG)     :', bg='#efedf1', fg='black')
        apple_quan.configure(font=('Comic Sans MS', 15))
        apple_quan.place(x=700, y=500)

        apple_price = Label(self.root, text='Price (per KG)     :', bg='#efedf1', fg='black')
        apple_price.configure(font=('Comic Sans MS', 15))
        apple_price.place(x=700, y=560)

        self.purquana = Label(self.root, text=self.main.puraquan, bg='#efedf1', fg='black')
        self.purquana.configure(font=('Comic Sans MS', 15))
        self.purquana.place(x=900, y=500)

        price_a = Label(self.root, text=self.main.a_price, bg='#efedf1', fg='black')
        price_a.configure(font=('Comic Sans MS', 15))
        price_a.place(x=900, y=560)

        price_total = Label(self.root, text='Total                  :', bg='#efedf1', fg='black')
        price_total.configure(font=('Comic Sans MS', 15))
        price_total.place(x=700, y=620)

        total_price_a = Label(self.root, text=price_a['text'] * self.purquana['text'], bg='#efedf1', fg='black')
        total_price_a.configure(font=('Comic Sans MS', 15))
        total_price_a.place(x=900, y=620)

        choice = Label(self.root, text='Choose any one \ncombination \nto pay', bg='#efedf1', fg='black')
        choice.configure(font=('Comic Sans MS', 20, 'bold underline'))
        choice.place(x=1250, y=200)

        self.l2 = Label(self.root, bg='#efedf1')
        self.l2.place(x=12600, y=300)

        def selected():
            self.l2.config(text=v2.get())

        v2 = StringVar(self.root)

        # Dictionary to create multiple buttons
        values = {"{}".format(self.l[0]): "1",
                  "{}".format(self.l[1]): "2",
                  "{}".format(self.l[2]): "3",
                  "{}".format(self.l[3]): "4",
                  "{}".format(self.l[4]): "5"}

        # Loop is used to create multiple Radiobuttons
        # rather than creating each button separately
        x = 1240
        y = 350
        for (text, value) in values.items():
            r = Radiobutton(self.root, text=text, variable=v2, value=value, background="light blue", command=selected)
            r.configure(font=('Comic Sans MS', 10, 'bold'))
            r.place(x=x, y=y)
            y += 50

        purbacash = Button(self.root, text='PURCHASE', width=20, command=self.purbacash)
        purbacash.configure(font=('Comic Sans MS', 10, 'bold'))
        purbacash.place(x=1270, y=650)

    def purbacash(self):
        if self.l2['text'] == '':
            messagebox.showerror('Error', 'Please select any one of the above options')
        else:
            messagebox.showinfo('Success',
                                'Your payment has been successfully made \nYour items will be delivered soon !!')
            self.root.destroy()



    def cardba(self):
        canvas = Canvas(bg='#efedf1', width=800, height=800, highlightbackground='black', highlightthickness=5)
        canvas.place(x=310, y=150)
        canvas = Canvas(bg='#efedf1', width=300, height=800, highlightbackground='black', highlightthickness=5)
        canvas.place(x=1200, y=150)
        path1 = "Images/banana.png"
        image1 = Image.open(path1)
        img1 = ImageTk.PhotoImage(image1.resize((200, 200)))
        banana = Label(self.root, image=img1, bg='#efedf1')
        banana.photo = img1
        banana.place(x=400, y=200)

        banana_quan = Label(self.root, text='Quantity (KG)     :', bg='#efedf1', fg='black')
        banana_quan.configure(font=('Comic Sans MS', 15))
        banana_quan.place(x=700, y=220)

        banana_price = Label(self.root, text='Price (per KG)    :', bg='#efedf1', fg='black')
        banana_price.configure(font=('Comic Sans MS', 15))
        banana_price.place(x=700, y=280)

        self.purquanb = Label(self.root, text=self.main.purbquan, bg='#efedf1', fg='black')
        self.purquanb.configure(font=('Comic Sans MS', 15))
        self.purquanb.place(x=900, y=220)

        price_b = Label(self.root, text=self.main.b_price, bg='#efedf1', fg='black')
        price_b.configure(font=('Comic Sans MS', 15))
        price_b.place(x=900, y=280)

        price_total = Label(self.root, text='Total                  :', bg='#efedf1', fg='black')
        price_total.configure(font=('Comic Sans MS', 15))
        price_total.place(x=700, y=340)

        total_price_b = Label(self.root, text=price_b['text'] * self.purquanb['text'], bg='#efedf1', fg='black')
        total_price_b.configure(font=('Comic Sans MS', 15))
        total_price_b.place(x=900, y=340)

        path2 = "Images/apple.png"
        image2 = Image.open(path2)
        img2 = ImageTk.PhotoImage(image2.resize((200, 200)))
        apple = Label(self.root, image=img2, bg='#efedf1')
        apple.photo = img2
        apple.place(x=400, y=470)

        apple_quan = Label(self.root, text='Quantity (KG)     :', bg='#efedf1', fg='black')
        apple_quan.configure(font=('Comic Sans MS', 15))
        apple_quan.place(x=700, y=500)

        apple_price = Label(self.root, text='Price (per KG)     :', bg='#efedf1', fg='black')
        apple_price.configure(font=('Comic Sans MS', 15))
        apple_price.place(x=700, y=560)

        self.purquana = Label(self.root, text=self.main.puraquan, bg='#efedf1', fg='black')
        self.purquana.configure(font=('Comic Sans MS', 15))
        self.purquana.place(x=900, y=500)

        price_a = Label(self.root, text=self.main.a_price, bg='#efedf1', fg='black')
        price_a.configure(font=('Comic Sans MS', 15))
        price_a.place(x=900, y=560)

        price_total = Label(self.root, text='Total                  :', bg='#efedf1', fg='black')
        price_total.configure(font=('Comic Sans MS', 15))
        price_total.place(x=700, y=620)

        total_price_a = Label(self.root, text=price_a['text'] * self.purquana['text'], bg='#efedf1', fg='black')
        total_price_a.configure(font=('Comic Sans MS', 15))
        total_price_a.place(x=900, y=620)

        self.bill_label_card()

        self.cardnoba  = Entry(self.root, width=20)
        self.cardnoba .configure(font=('Comic Sans MS', 10))
        self.cardnoba .place(x=1270, y=350)

        self.cardnameba = Entry(self.root, width=20)
        self.cardnameba.configure(font=('Comic Sans MS', 10))
        self.cardnameba.place(x=1270, y=450)

        self.cvvba = Entry(self.root, width=20)
        self.cvvba.configure(font=('Comic Sans MS', 10))
        self.cvvba.place(x=1270, y=550)

        purba = Button(self.root, text='PURCHASE', width=20,command=self.baerror)
        purba.configure(font=('Comic Sans MS', 10, 'bold'))
        purba.place(x=1270, y=650)

    def baerror(self):
        response = self.errorpur(self.cardnoba.get(), self.cardnameba.get(), self.cvvba.get())
        if response==0:
            messagebox.showerror('Error','Please fill all the blanks')
        elif response == 1:
            messagebox.showerror('Error', 'Please enter card number with only digits / Check if it is of length 12')
        elif response == 2:
            messagebox.showerror('Error', 'Please enter string characters in your name')
        elif response == 3:
            messagebox.showerror('Error', 'Please enter cvv number with only digits / Check if it is of length 3')
        else:
            messagebox.showinfo('Success !!','Your payment has been successfully made \nYour items will be delivered soon !!')
            self.root.destroy()

    def cashao(self):
        canvas = Canvas(bg='#efedf1', width=800, height=800, highlightbackground='black', highlightthickness=5)
        canvas.place(x=310, y=150)
        canvas = Canvas(bg='#efedf1', width=300, height=800, highlightbackground='black', highlightthickness=5)
        canvas.place(x=1200, y=150)
        path2 = "Images/apple.png"
        image2 = Image.open(path2)
        img2 = ImageTk.PhotoImage(image2.resize((200, 200)))
        apple = Label(self.root, image=img2, bg='#efedf1')
        apple.photo = img2
        apple.place(x=400, y=200)

        apple_quan = Label(self.root, text='Quantity (KG)     :', bg='#efedf1', fg='black')
        apple_quan.configure(font=('Comic Sans MS', 15))
        apple_quan.place(x=700, y=220)

        apple_price = Label(self.root, text='Price (per KG)     :', bg='#efedf1', fg='black')
        apple_price.configure(font=('Comic Sans MS', 15))
        apple_price.place(x=700, y=280)

        self.purquana = Label(self.root, text=self.main.puraquan, bg='#efedf1', fg='black')
        self.purquana.configure(font=('Comic Sans MS', 15))
        self.purquana.place(x=900, y=220)

        price_a = Label(self.root, text=self.main.a_price, bg='#efedf1', fg='black')
        price_a.configure(font=('Comic Sans MS', 15))
        price_a.place(x=900, y=280)

        price_total = Label(self.root, text='Total                  :', bg='#efedf1', fg='black')
        price_total.configure(font=('Comic Sans MS', 15))
        price_total.place(x=700, y=340)

        total_price_a = Label(self.root, text=price_a['text'] * self.purquana['text'], bg='#efedf1', fg='black')
        total_price_a.configure(font=('Comic Sans MS', 15))
        total_price_a.place(x=900, y=340)

        path3 = "Images/orange.png"
        image3 = Image.open(path3)
        img3 = ImageTk.PhotoImage(image3.resize((200, 200)))
        orange = Label(self.root, image=img3, bg='#efedf1')
        orange.photo = img3
        orange.place(x=400, y=470)

        orange_quan = Label(self.root, text='Quantity (KG)     :', bg='#efedf1', fg='black')
        orange_quan.configure(font=('Comic Sans MS', 15))
        orange_quan.place(x=700, y=500)

        orange_price = Label(self.root, text='Price (per KG)     :', bg='#efedf1', fg='black')
        orange_price.configure(font=('Comic Sans MS', 15))
        orange_price.place(x=700, y=560)

        self.purquano = Label(self.root, text=self.main.puroquan, bg='#efedf1', fg='black')
        self.purquano.configure(font=('Comic Sans MS', 15))
        self.purquano.place(x=900, y=500)

        price_o = Label(self.root, text=self.main.o_price, bg='#efedf1', fg='black')
        price_o.configure(font=('Comic Sans MS', 15))
        price_o.place(x=900, y=560)

        price_total = Label(self.root, text='Total                  :', bg='#efedf1', fg='black')
        price_total.configure(font=('Comic Sans MS', 15))
        price_total.place(x=700, y=620)

        total_price_o = Label(self.root, text=price_o['text'] * self.purquano['text'], bg='#efedf1', fg='black')
        total_price_o.configure(font=('Comic Sans MS', 15))
        total_price_o.place(x=900, y=620)

        choice = Label(self.root, text='Choose any one \ncombination \nto pay', bg='#efedf1', fg='black')
        choice.configure(font=('Comic Sans MS', 20, 'bold underline'))
        choice.place(x=1250, y=200)

        self.l3 = Label(self.root, bg='#efedf1')
        self.l3.place(x=12600, y=300)

        def selected():
            self.l3.config(text=v3.get())

        v3 = StringVar(self.root)

        # Dictionary to create multiple buttons
        values = {"{}".format(self.l[0]): "1",
                  "{}".format(self.l[1]): "2",
                  "{}".format(self.l[2]): "3",
                  "{}".format(self.l[3]): "4",
                  "{}".format(self.l[4]): "5"}

        # Loop is used to create multiple Radiobuttons
        # rather than creating each button separately
        x = 1240
        y = 350
        for (text, value) in values.items():
            r = Radiobutton(self.root, text=text, variable=v3, value=value, background="light blue", command=selected)
            r.configure(font=('Comic Sans MS', 10, 'bold'))
            r.place(x=x, y=y)
            y += 50

        puraocash = Button(self.root, text='PURCHASE', width=20, command=self.puraocash)
        puraocash.configure(font=('Comic Sans MS', 10, 'bold'))
        puraocash.place(x=1270, y=650)

    def puraocash(self):
        if self.l3['text'] == '':
            messagebox.showerror('Error', 'Please select any one of the above options')
        else:
            messagebox.showinfo('Success',
                                'Your payment has been successfully made \nYour items will be delivered soon !!')
            self.root.destroy()

    def cardao(self):
        canvas = Canvas(bg='#efedf1', width=800, height=800, highlightbackground='black', highlightthickness=5)
        canvas.place(x=310, y=150)
        canvas = Canvas(bg='#efedf1', width=300, height=800, highlightbackground='black', highlightthickness=5)
        canvas.place(x=1200, y=150)
        path2 = "Images/apple.png"
        image2 = Image.open(path2)
        img2 = ImageTk.PhotoImage(image2.resize((200, 200)))
        apple = Label(self.root, image=img2, bg='#efedf1')
        apple.photo = img2
        apple.place(x=400, y=200)

        apple_quan = Label(self.root, text='Quantity (KG)     :', bg='#efedf1', fg='black')
        apple_quan.configure(font=('Comic Sans MS', 15))
        apple_quan.place(x=700, y=220)

        apple_price = Label(self.root, text='Price (per KG)     :', bg='#efedf1', fg='black')
        apple_price.configure(font=('Comic Sans MS', 15))
        apple_price.place(x=700, y=280)

        self.purquana = Label(self.root, text=self.main.puraquan, bg='#efedf1', fg='black')
        self.purquana.configure(font=('Comic Sans MS', 15))
        self.purquana.place(x=900, y=220)

        price_a = Label(self.root, text=self.main.a_price, bg='#efedf1', fg='black')
        price_a.configure(font=('Comic Sans MS', 15))
        price_a.place(x=900, y=280)

        price_total = Label(self.root, text='Total                  :', bg='#efedf1', fg='black')
        price_total.configure(font=('Comic Sans MS', 15))
        price_total.place(x=700, y=340)

        total_price_a = Label(self.root, text=price_a['text'] * self.purquana['text'], bg='#efedf1', fg='black')
        total_price_a.configure(font=('Comic Sans MS', 15))
        total_price_a.place(x=900, y=340)

        path3 = "Images/orange.png"
        image3 = Image.open(path3)
        img3 = ImageTk.PhotoImage(image3.resize((200, 200)))
        orange = Label(self.root, image=img3, bg='#efedf1')
        orange.photo = img3
        orange.place(x=400, y=470)

        orange_quan = Label(self.root, text='Quantity (KG)     :', bg='#efedf1', fg='black')
        orange_quan.configure(font=('Comic Sans MS', 15))
        orange_quan.place(x=700, y=500)

        orange_price = Label(self.root, text='Price (per KG)     :', bg='#efedf1', fg='black')
        orange_price.configure(font=('Comic Sans MS', 15))
        orange_price.place(x=700, y=560)

        self.purquano = Label(self.root, text=self.main.puroquan, bg='#efedf1', fg='black')
        self.purquano.configure(font=('Comic Sans MS', 15))
        self.purquano.place(x=900, y=500)

        price_o = Label(self.root, text=self.main.o_price, bg='#efedf1', fg='black')
        price_o.configure(font=('Comic Sans MS', 15))
        price_o.place(x=900, y=560)

        price_total = Label(self.root, text='Total                  :', bg='#efedf1', fg='black')
        price_total.configure(font=('Comic Sans MS', 15))
        price_total.place(x=700, y=620)

        total_price_o = Label(self.root, text=price_o['text'] * self.purquano['text'], bg='#efedf1', fg='black')
        total_price_o.configure(font=('Comic Sans MS', 15))
        total_price_o.place(x=900, y=620)

        self.bill_label_card()

        self.cardnoao = Entry(self.root, width=20)
        self.cardnoao.configure(font=('Comic Sans MS', 10))
        self.cardnoao.place(x=1270, y=350)

        self.cardnameao = Entry(self.root, width=20)
        self.cardnameao.configure(font=('Comic Sans MS', 10))
        self.cardnameao.place(x=1270, y=450)

        self.cvvao = Entry(self.root, width=20)
        self.cvvao.configure(font=('Comic Sans MS', 10))
        self.cvvao.place(x=1270, y=550)

        purao = Button(self.root, text='PURCHASE', width=20,command=self.aoerror)
        purao.configure(font=('Comic Sans MS', 10, 'bold'))
        purao.place(x=1270, y=650)

    def aoerror(self):
        response = self.errorpur(self.cardnoao.get(), self.cardnameao.get(), self.cvvao.get())
        if response==0:
            messagebox.showerror('Error','Please fill all the blanks')
        elif response == 1:
            messagebox.showerror('Error', 'Please enter card number with only digits / Check if it is of length 12')
        elif response == 2:
            messagebox.showerror('Error', 'Please enter string characters in your name')
        elif response == 3:
            messagebox.showerror('Error', 'Please enter cvv number with only digits / Check if it is of length 3')
        else:
            messagebox.showinfo('Success !!',
                                'Your payment has been successfully made \nYour items will be delivered soon !!')
            self.root.destroy()

    def cashob(self):
        canvas = Canvas(bg='#efedf1', width=800, height=800, highlightbackground='black', highlightthickness=5)
        canvas.place(x=310, y=150)
        canvas = Canvas(bg='#efedf1', width=300, height=800, highlightbackground='black', highlightthickness=5)
        canvas.place(x=1200, y=150)
        path1 = "Images/banana.png"
        image1 = Image.open(path1)
        img1 = ImageTk.PhotoImage(image1.resize((200, 200)))
        banana = Label(self.root, image=img1, bg='#efedf1')
        banana.photo = img1
        banana.place(x=400, y=200)

        banana_quan = Label(self.root, text='Quantity (KG)     :', bg='#efedf1', fg='black')
        banana_quan.configure(font=('Comic Sans MS', 15))
        banana_quan.place(x=700, y=220)

        banana_price = Label(self.root, text='Price (per KG)    :', bg='#efedf1', fg='black')
        banana_price.configure(font=('Comic Sans MS', 15))
        banana_price.place(x=700, y=280)

        self.purquanb = Label(self.root, text=self.main.purbquan, bg='#efedf1', fg='black')
        self.purquanb.configure(font=('Comic Sans MS', 15))
        self.purquanb.place(x=900, y=220)

        price_b = Label(self.root, text=self.main.b_price, bg='#efedf1', fg='black')
        price_b.configure(font=('Comic Sans MS', 15))
        price_b.place(x=900, y=280)

        price_total = Label(self.root, text='Total                  :', bg='#efedf1', fg='black')
        price_total.configure(font=('Comic Sans MS', 15))
        price_total.place(x=700, y=340)

        total_price_b = Label(self.root, text=price_b['text'] * self.purquanb['text'], bg='#efedf1', fg='black')
        total_price_b.configure(font=('Comic Sans MS', 15))
        total_price_b.place(x=900, y=340)

        path3 = "Images/orange.png"
        image3 = Image.open(path3)
        img3 = ImageTk.PhotoImage(image3.resize((200, 200)))
        orange = Label(self.root, image=img3, bg='#efedf1')
        orange.photo = img3
        orange.place(x=400, y=470)

        orange_quan = Label(self.root, text='Quantity (KG)     :', bg='#efedf1', fg='black')
        orange_quan.configure(font=('Comic Sans MS', 15))
        orange_quan.place(x=700, y=500)

        orange_price = Label(self.root, text='Price (per KG)     :', bg='#efedf1', fg='black')
        orange_price.configure(font=('Comic Sans MS', 15))
        orange_price.place(x=700, y=560)

        self.purquano = Label(self.root, text=self.main.puroquan, bg='#efedf1', fg='black')
        self.purquano.configure(font=('Comic Sans MS', 15))
        self.purquano.place(x=900, y=500)

        price_o = Label(self.root, text=self.main.o_price, bg='#efedf1', fg='black')
        price_o.configure(font=('Comic Sans MS', 15))
        price_o.place(x=900, y=560)

        price_total = Label(self.root, text='Total                  :', bg='#efedf1', fg='black')
        price_total.configure(font=('Comic Sans MS', 15))
        price_total.place(x=700, y=620)

        total_price_o = Label(self.root, text=price_o['text'] * self.purquano['text'], bg='#efedf1', fg='black')
        total_price_o.configure(font=('Comic Sans MS', 15))
        total_price_o.place(x=900, y=620)

        choice = Label(self.root, text='Choose any one \ncombination \nto pay', bg='#efedf1', fg='black')
        choice.configure(font=('Comic Sans MS', 20, 'bold underline'))
        choice.place(x=1250, y=200)

        self.l4 = Label(self.root, bg='#efedf1')
        self.l4.place(x=12600, y=300)

        def selected():
            self.l4.config(text=v4.get())

        v4 = StringVar(self.root)

        # Dictionary to create multiple buttons
        values = {"{}".format(self.l[0]): "1",
                  "{}".format(self.l[1]): "2",
                  "{}".format(self.l[2]): "3",
                  "{}".format(self.l[3]): "4",
                  "{}".format(self.l[4]): "5"}

        # Loop is used to create multiple Radiobuttons
        # rather than creating each button separately
        x = 1240
        y = 350
        for (text, value) in values.items():
            r = Radiobutton(self.root, text=text, variable=v4, value=value, background="light blue", command=selected)
            r.configure(font=('Comic Sans MS', 10, 'bold'))
            r.place(x=x, y=y)
            y += 50

        purobcash = Button(self.root, text='PURCHASE', width=20, command=self.purobcash)
        purobcash.configure(font=('Comic Sans MS', 10, 'bold'))
        purobcash.place(x=1270, y=650)

    def purobcash(self):
        if self.l4['text'] == '':
            messagebox.showerror('Error', 'Please select any one of the above options')
        else:
            messagebox.showinfo('Success',
                                'Your payment has been successfully made \nYour items will be delivered soon !!')
            self.root.destroy()




    def cardob(self):
        canvas = Canvas(bg='#efedf1', width=800, height=800, highlightbackground='black', highlightthickness=5)
        canvas.place(x=310, y=150)
        canvas = Canvas(bg='#efedf1', width=300, height=800, highlightbackground='black', highlightthickness=5)
        canvas.place(x=1200, y=150)
        path1 = "Images/banana.png"
        image1 = Image.open(path1)
        img1 = ImageTk.PhotoImage(image1.resize((200, 200)))
        banana = Label(self.root, image=img1, bg='#efedf1')
        banana.photo = img1
        banana.place(x=400, y=200)

        banana_quan = Label(self.root, text='Quantity (KG)     :', bg='#efedf1', fg='black')
        banana_quan.configure(font=('Comic Sans MS', 15))
        banana_quan.place(x=700, y=220)

        banana_price = Label(self.root, text='Price (per KG)    :', bg='#efedf1', fg='black')
        banana_price.configure(font=('Comic Sans MS', 15))
        banana_price.place(x=700, y=280)

        self.purquanb = Label(self.root, text=self.main.purbquan, bg='#efedf1', fg='black')
        self.purquanb.configure(font=('Comic Sans MS', 15))
        self.purquanb.place(x=900, y=220)

        price_b = Label(self.root, text=self.main.b_price, bg='#efedf1', fg='black')
        price_b.configure(font=('Comic Sans MS', 15))
        price_b.place(x=900, y=280)

        price_total = Label(self.root, text='Total                  :', bg='#efedf1', fg='black')
        price_total.configure(font=('Comic Sans MS', 15))
        price_total.place(x=700, y=340)

        total_price_b = Label(self.root, text=price_b['text'] * self.purquanb['text'], bg='#efedf1', fg='black')
        total_price_b.configure(font=('Comic Sans MS', 15))
        total_price_b.place(x=900, y=340)

        path3 = "Images/orange.png"
        image3 = Image.open(path3)
        img3 = ImageTk.PhotoImage(image3.resize((200, 200)))
        orange = Label(self.root, image=img3, bg='#efedf1')
        orange.photo = img3
        orange.place(x=400, y=470)

        orange_quan = Label(self.root, text='Quantity (KG)     :', bg='#efedf1', fg='black')
        orange_quan.configure(font=('Comic Sans MS', 15))
        orange_quan.place(x=700, y=500)

        orange_price = Label(self.root, text='Price (per KG)     :', bg='#efedf1', fg='black')
        orange_price.configure(font=('Comic Sans MS', 15))
        orange_price.place(x=700, y=560)

        self.purquano = Label(self.root, text=self.main.puroquan, bg='#efedf1', fg='black')
        self.purquano.configure(font=('Comic Sans MS', 15))
        self.purquano.place(x=900, y=500)

        price_o = Label(self.root, text=self.main.o_price, bg='#efedf1', fg='black')
        price_o.configure(font=('Comic Sans MS', 15))
        price_o.place(x=900, y=560)

        price_total = Label(self.root, text='Total                  :', bg='#efedf1', fg='black')
        price_total.configure(font=('Comic Sans MS', 15))
        price_total.place(x=700, y=620)

        total_price_o = Label(self.root, text=price_o['text'] * self.purquano['text'], bg='#efedf1', fg='black')
        total_price_o.configure(font=('Comic Sans MS', 15))
        total_price_o.place(x=900, y=620)

        self.bill_label_card()

        self.cardnoob = Entry(self.root, width=20)
        self.cardnoob.configure(font=('Comic Sans MS', 10))
        self.cardnoob.place(x=1270, y=350)

        self.cardnameob = Entry(self.root, width=20)
        self.cardnameob.configure(font=('Comic Sans MS', 10))
        self.cardnameob.place(x=1270, y=450)

        self.cvvob = Entry(self.root, width=20)
        self.cvvob.configure(font=('Comic Sans MS', 10))
        self.cvvob.place(x=1270, y=550)

        purob = Button(self.root, text='PURCHASE', width=20,command=self.oberror)
        purob.configure(font=('Comic Sans MS', 10, 'bold'))
        purob.place(x=1270, y=650)

    def oberror(self):
        response=self.errorpur(self.cardnoob.get(),self.cardnameob.get(),self.cvvob.get())
        if response==0:
            messagebox.showerror('Error','Please fill all the blanks')
        elif response==1:
            messagebox.showerror('Error','Please enter card number with only digits / Check if it is of length 12')
        elif response==2:
            messagebox.showerror('Error','Please enter string characters in your name')
        elif response==3:
            messagebox.showerror('Error','Please enter cvv number with only digits / Check if it is of length 3')
        else:
            messagebox.showinfo('Success !!', 'Your payment has been successfully made \nYour items will be delivered soon !!')
            self.root.destroy()


    def cashb(self):
        canvas = Canvas(bg='#efedf1', width=800, height=800, highlightbackground='black', highlightthickness=5)
        canvas.place(x=310, y=150)
        canvas = Canvas(bg='#efedf1', width=300, height=800, highlightbackground='black', highlightthickness=5)
        canvas.place(x=1200, y=150)
        path1 = "Images/banana.png"
        image1 = Image.open(path1)
        img1 = ImageTk.PhotoImage(image1.resize((200, 200)))
        banana = Label(self.root, image=img1, bg='#efedf1')
        banana.photo = img1
        banana.place(x=400, y=200)

        banana_quan = Label(self.root, text='Quantity (KG)     :', bg='#efedf1', fg='black')
        banana_quan.configure(font=('Comic Sans MS', 15))
        banana_quan.place(x=700, y=220)

        banana_price = Label(self.root, text='Price (per KG)    :', bg='#efedf1', fg='black')
        banana_price.configure(font=('Comic Sans MS', 15))
        banana_price.place(x=700, y=280)

        self.purquanb = Label(self.root, text=self.main.purbquan, bg='#efedf1', fg='black')
        self.purquanb.configure(font=('Comic Sans MS', 15))
        self.purquanb.place(x=900, y=220)

        price_b = Label(self.root, text=self.main.b_price, bg='#efedf1', fg='black')
        price_b.configure(font=('Comic Sans MS', 15))
        price_b.place(x=900, y=280)

        price_total = Label(self.root, text='Total                  :', bg='#efedf1', fg='black')
        price_total.configure(font=('Comic Sans MS', 15))
        price_total.place(x=700, y=340)

        total_price_b = Label(self.root, text=price_b['text'] * self.purquanb['text'], bg='#efedf1', fg='black')
        total_price_b.configure(font=('Comic Sans MS', 15))
        total_price_b.place(x=900, y=340)

        choice = Label(self.root, text='Choose any one \ncombination \nto pay', bg='#efedf1', fg='black')
        choice.configure(font=('Comic Sans MS', 20, 'bold underline'))
        choice.place(x=1250, y=200)

        self.l5 = Label(self.root, bg='#efedf1')
        self.l5.place(x=12600, y=300)

        def selected():
            self.l5.config(text=v5.get())

        v5 = StringVar(self.root)

        # Dictionary to create multiple buttons
        values = {"{}".format(self.l[0]): "1",
                  "{}".format(self.l[1]): "2",
                  "{}".format(self.l[2]): "3",
                  "{}".format(self.l[3]): "4",
                  "{}".format(self.l[4]): "5"}

        # Loop is used to create multiple Radiobuttons
        # rather than creating each button separately
        x = 1240
        y = 350
        for (text, value) in values.items():
            r = Radiobutton(self.root, text=text, variable=v5, value=value, background="light blue", command=selected)
            r.configure(font=('Comic Sans MS', 10, 'bold'))
            r.place(x=x, y=y)
            y += 50

        purbcash = Button(self.root, text='PURCHASE', width=20, command=self.purbcash)
        purbcash.configure(font=('Comic Sans MS', 10, 'bold'))
        purbcash.place(x=1270, y=650)

    def purbcash(self):
        if self.l5['text'] == '':
            messagebox.showerror('Error', 'Please select any one of the above options')
        else:
            messagebox.showinfo('Success',
                                'Your payment has been successfully made \nYour items will be delivered soon !!')
            self.root.destroy()

    def cardb(self):
        canvas = Canvas(bg='#efedf1', width=800, height=800, highlightbackground='black', highlightthickness=5)
        canvas.place(x=310, y=150)
        canvas = Canvas(bg='#efedf1', width=300, height=800, highlightbackground='black', highlightthickness=5)
        canvas.place(x=1200, y=150)
        path1 = "Images/banana.png"
        image1 = Image.open(path1)
        img1 = ImageTk.PhotoImage(image1.resize((200, 200)))
        banana = Label(self.root, image=img1, bg='#efedf1')
        banana.photo = img1
        banana.place(x=400, y=200)

        banana_quan = Label(self.root, text='Quantity (KG)     :', bg='#efedf1', fg='black')
        banana_quan.configure(font=('Comic Sans MS', 15))
        banana_quan.place(x=700, y=220)

        banana_price = Label(self.root, text='Price (per KG)    :', bg='#efedf1', fg='black')
        banana_price.configure(font=('Comic Sans MS', 15))
        banana_price.place(x=700, y=280)

        self.purquanb = Label(self.root, text=self.main.purbquan, bg='#efedf1', fg='black')
        self.purquanb.configure(font=('Comic Sans MS', 15))
        self.purquanb.place(x=900, y=220)

        price_b = Label(self.root, text=self.main.b_price, bg='#efedf1', fg='black')
        price_b.configure(font=('Comic Sans MS', 15))
        price_b.place(x=900, y=280)

        price_total = Label(self.root, text='Total                  :', bg='#efedf1', fg='black')
        price_total.configure(font=('Comic Sans MS', 15))
        price_total.place(x=700, y=340)

        total_price_b = Label(self.root, text=price_b['text'] * self.purquanb['text'], bg='#efedf1', fg='black')
        total_price_b.configure(font=('Comic Sans MS', 15))
        total_price_b.place(x=900, y=340)

        self.bill_label_card()

        self.cardnob = Entry(self.root, width=20)
        self.cardnob.configure(font=('Comic Sans MS', 10))
        self.cardnob.place(x=1270, y=350)

        self.cardnameb = Entry(self.root, width=20)
        self.cardnameb.configure(font=('Comic Sans MS', 10))
        self.cardnameb.place(x=1270, y=450)

        self.cvvb = Entry(self.root, width=20)
        self.cvvb.configure(font=('Comic Sans MS', 10))
        self.cvvb.place(x=1270, y=550)

        purb = Button(self.root, text='PURCHASE', width=20,command=self.berror)
        purb.configure(font=('Comic Sans MS', 10, 'bold'))
        purb.place(x=1270, y=650)

    def berror(self):
        response=self.errorpur(self.cardnob.get(),self.cardnameb.get(),self.cvvb.get())
        if response==0:
            messagebox.showerror('Error','Please fill all the blanks')
        elif response==1:
            messagebox.showerror('Error','Please enter card number with only digits / Check if it is of length 12')
        elif response==2:
            messagebox.showerror('Error','Please enter string characters in your name')
        elif response==3:
            messagebox.showerror('Error','Please enter cvv number with only digits / Check if it is of length 3')
        else:
            messagebox.showinfo('Success !!', 'Your payment has been successfully made \nYour items will be delivered soon !!')
            self.root.destroy()


    def casha(self):
        canvas = Canvas(bg='#efedf1', width=800, height=800, highlightbackground='black', highlightthickness=5)
        canvas.place(x=310, y=150)
        canvas = Canvas(bg='#efedf1', width=300, height=800, highlightbackground='black', highlightthickness=5)
        canvas.place(x=1200, y=150)
        path2 = "Images/apple.png"
        image2 = Image.open(path2)
        img2 = ImageTk.PhotoImage(image2.resize((200, 200)))
        apple = Label(self.root, image=img2, bg='#efedf1')
        apple.photo = img2
        apple.place(x=400, y=200)

        apple_quan = Label(self.root, text='Quantity (KG)     :', bg='#efedf1', fg='black')
        apple_quan.configure(font=('Comic Sans MS', 15))
        apple_quan.place(x=700, y=220)

        apple_price = Label(self.root, text='Price (per KG)     :', bg='#efedf1', fg='black')
        apple_price.configure(font=('Comic Sans MS', 15))
        apple_price.place(x=700, y=280)

        self.purquana = Label(self.root, text=self.main.puraquan, bg='#efedf1', fg='black')
        self.purquana.configure(font=('Comic Sans MS', 15))
        self.purquana.place(x=900, y=220)

        price_a = Label(self.root, text=self.main.a_price, bg='#efedf1', fg='black')
        price_a.configure(font=('Comic Sans MS', 15))
        price_a.place(x=900, y=280)

        price_total = Label(self.root, text='Total                  :', bg='#efedf1', fg='black')
        price_total.configure(font=('Comic Sans MS', 15))
        price_total.place(x=700, y=340)

        total_price_a = Label(self.root, text=price_a['text'] * self.purquana['text'], bg='#efedf1', fg='black')
        total_price_a.configure(font=('Comic Sans MS', 15))
        total_price_a.place(x=900, y=340)

        choice = Label(self.root, text='Choose any one \ncombination \nto pay', bg='#efedf1', fg='black')
        choice.configure(font=('Comic Sans MS', 20, 'bold underline'))
        choice.place(x=1250, y=200)

        self.l6 = Label(self.root, bg='#efedf1')
        self.l6.place(x=12600, y=300)

        def selected():
            self.l6.config(text=v6.get())

        v6 = StringVar(self.root)

        # Dictionary to create multiple buttons
        values = {"{}".format(self.l[0]): "1",
                  "{}".format(self.l[1]): "2",
                  "{}".format(self.l[2]): "3",
                  "{}".format(self.l[3]): "4",
                  "{}".format(self.l[4]): "5"}

        # Loop is used to create multiple Radiobuttons
        # rather than creating each button separately
        x = 1240
        y = 350
        for (text, value) in values.items():
            r = Radiobutton(self.root, text=text, variable=v6, value=value, background="light blue", command=selected)
            r.configure(font=('Comic Sans MS', 10, 'bold'))
            r.place(x=x, y=y)
            y += 50

        puracash = Button(self.root, text='PURCHASE', width=20, command=self.puracash)
        puracash.configure(font=('Comic Sans MS', 10, 'bold'))
        puracash.place(x=1270, y=650)

    def puracash(self):
        if self.l6['text'] == '':
            messagebox.showerror('Error', 'Please select any one of the above options')
        else:
            messagebox.showinfo('Success',
                                'Your payment has been successfully made \nYour items will be delivered soon !!')
            self.root.destroy()



    def carda(self):
        canvas = Canvas(bg='#efedf1', width=800, height=800, highlightbackground='black', highlightthickness=5)
        canvas.place(x=310, y=150)
        canvas = Canvas(bg='#efedf1', width=300, height=800, highlightbackground='black', highlightthickness=5)
        canvas.place(x=1200, y=150)
        path2 = "Images/apple.png"
        image2 = Image.open(path2)
        img2 = ImageTk.PhotoImage(image2.resize((200, 200)))
        apple = Label(self.root, image=img2, bg='#efedf1')
        apple.photo = img2
        apple.place(x=400, y=200)

        apple_quan = Label(self.root, text='Quantity (KG)     :', bg='#efedf1', fg='black')
        apple_quan.configure(font=('Comic Sans MS', 15))
        apple_quan.place(x=700, y=220)

        apple_price = Label(self.root, text='Price (per KG)     :', bg='#efedf1', fg='black')
        apple_price.configure(font=('Comic Sans MS', 15))
        apple_price.place(x=700, y=280)

        self.purquana = Label(self.root, text=self.main.puraquan, bg='#efedf1', fg='black')
        self.purquana.configure(font=('Comic Sans MS', 15))
        self.purquana.place(x=900, y=220)

        price_a = Label(self.root, text=self.main.a_price, bg='#efedf1', fg='black')
        price_a.configure(font=('Comic Sans MS', 15))
        price_a.place(x=900, y=280)

        price_total = Label(self.root, text='Total                  :', bg='#efedf1', fg='black')
        price_total.configure(font=('Comic Sans MS', 15))
        price_total.place(x=700, y=340)

        total_price_a = Label(self.root, text=price_a['text'] * self.purquana['text'], bg='#efedf1', fg='black')
        total_price_a.configure(font=('Comic Sans MS', 15))
        total_price_a.place(x=900, y=340)

        self.bill_label_card()

        self.cardnoa = Entry(self.root, width=20)
        self.cardnoa.configure(font=('Comic Sans MS', 10))
        self.cardnoa.place(x=1270, y=350)

        self.cardnamea = Entry(self.root, width=20)
        self.cardnamea.configure(font=('Comic Sans MS', 10))
        self.cardnamea.place(x=1270, y=450)

        self.cvva = Entry(self.root, width=20)
        self.cvva.configure(font=('Comic Sans MS', 10))
        self.cvva.place(x=1270, y=550)

        pura = Button(self.root, text='PURCHASE', width=20,command=self.aerror)
        pura.configure(font=('Comic Sans MS', 10, 'bold'))
        pura.place(x=1270, y=650)

    def aerror(self):
        response=self.errorpur(self.cardnoa.get(),self.cardnamea.get(),self.cvva.get())
        if response==0:
            messagebox.showerror('Error','Please fill all the blanks')
        elif response==1:
            messagebox.showerror('Error','Please enter card number with only digits / Check if it is of length 12')
        elif response==2:
            messagebox.showerror('Error','Please enter string characters in your name')
        elif response==3:
            messagebox.showerror('Error','Please enter cvv number with only digits / Check if it is of length 3')
        else:
            messagebox.showinfo('Success !!', 'Your payment has been successfully made \nYour items will be delivered soon !!')
            self.root.destroy()


    def casho(self):
        canvas = Canvas(bg='#efedf1', width=800, height=800, highlightbackground='black', highlightthickness=5)
        canvas.place(x=310, y=150)
        canvas1 = Canvas(bg='#efedf1', width=300, height=800, highlightbackground='black', highlightthickness=5)
        canvas1.place(x=1200, y=150)
        path3 = "Images/orange.png"
        image3 = Image.open(path3)
        img3 = ImageTk.PhotoImage(image3.resize((200, 200)))
        orange = Label(self.root, image=img3, bg='#efedf1')
        orange.photo = img3
        orange.place(x=400, y=200)

        orange_quan = Label(self.root, text='Quantity (KG)     :', bg='#efedf1', fg='black')
        orange_quan.configure(font=('Comic Sans MS', 15))
        orange_quan.place(x=700, y=220)

        orange_price = Label(self.root, text='Price (per KG)     :', bg='#efedf1', fg='black')
        orange_price.configure(font=('Comic Sans MS', 15))
        orange_price.place(x=700, y=280)

        self.purquano = Label(self.root, text=self.main.puroquan, bg='#efedf1', fg='black')
        self.purquano.configure(font=('Comic Sans MS', 15))
        self.purquano.place(x=900, y=220)

        price_o = Label(self.root, text=self.main.o_price, bg='#efedf1', fg='black')
        price_o.configure(font=('Comic Sans MS', 15))
        price_o.place(x=900, y=280)

        price_total = Label(self.root, text='Total                  :', bg='#efedf1', fg='black')
        price_total.configure(font=('Comic Sans MS', 15))
        price_total.place(x=700, y=340)

        total_price_o = Label(self.root, text=price_o['text'] * self.purquano['text'], bg='#efedf1', fg='black')
        total_price_o.configure(font=('Comic Sans MS', 15))
        total_price_o.place(x=900, y=340)

        choice = Label(self.root, text='Choose any one \ncombination \nto pay', bg='#efedf1', fg='black')
        choice.configure(font=('Comic Sans MS', 20, 'bold underline'))
        choice.place(x=1250, y=200)

        self.l7 = Label(self.root, bg='#efedf1')
        self.l7.place(x=12600, y=300)

        def selected():
            self.l7.config(text=v7.get())

        v7 = StringVar(self.root)

        # Dictionary to create multiple buttons
        values = {"{}".format(self.l[0]): "1",
                  "{}".format(self.l[1]): "2",
                  "{}".format(self.l[2]): "3",
                  "{}".format(self.l[3]): "4",
                  "{}".format(self.l[4]): "5"}

        # Loop is used to create multiple Radiobuttons
        # rather than creating each button separately
        x = 1240
        y = 350
        for (text, value) in values.items():
            r = Radiobutton(self.root, text=text, variable=v7, value=value, background="light blue", command=selected)
            r.configure(font=('Comic Sans MS', 10, 'bold'))
            r.place(x=x, y=y)
            y += 50

        purocash = Button(self.root, text='PURCHASE', width=20, command=self.purocash)
        purocash.configure(font=('Comic Sans MS', 10, 'bold'))
        purocash.place(x=1270, y=650)

    def purocash(self):
        if self.l7['text'] == '':
            messagebox.showerror('Error', 'Please select any one of the above options')
        else:
            messagebox.showinfo('Success',
                                'Your payment has been successfully made \nYour items will be delivered soon !!')
            self.root.destroy()


    def cardo(self):
        canvas = Canvas(bg='#efedf1', width=800, height=800, highlightbackground='black', highlightthickness=5)
        canvas.place(x=310, y=150)
        canvas1 = Canvas(bg='#efedf1', width=300, height=800, highlightbackground='black', highlightthickness=5)
        canvas1.place(x=1200, y=150)
        path3 = "Images/orange.png"
        image3 = Image.open(path3)
        img3 = ImageTk.PhotoImage(image3.resize((200, 200)))
        orange = Label(self.root, image=img3, bg='#efedf1')
        orange.photo = img3
        orange.place(x=400, y=200)

        orange_quan = Label(self.root, text='Quantity (KG)     :', bg='#efedf1', fg='black')
        orange_quan.configure(font=('Comic Sans MS', 15))
        orange_quan.place(x=700, y=220)

        orange_price = Label(self.root, text='Price (per KG)     :', bg='#efedf1', fg='black')
        orange_price.configure(font=('Comic Sans MS', 15))
        orange_price.place(x=700, y=280)

        self.purquano = Label(self.root, text=self.main.puroquan, bg='#efedf1', fg='black')
        self.purquano.configure(font=('Comic Sans MS', 15))
        self.purquano.place(x=900, y=220)

        price_o = Label(self.root, text=self.main.o_price, bg='#efedf1', fg='black')
        price_o.configure(font=('Comic Sans MS', 15))
        price_o.place(x=900, y=280)

        price_total = Label(self.root, text='Total                  :', bg='#efedf1', fg='black')
        price_total.configure(font=('Comic Sans MS', 15))
        price_total.place(x=700, y=340)

        total_price_o = Label(self.root, text=price_o['text'] * self.purquano['text'], bg='#efedf1', fg='black')
        total_price_o.configure(font=('Comic Sans MS', 15))
        total_price_o.place(x=900, y=340)

        self.bill_label_card()

        self.cardnoo = Entry(self.root, width=20)
        self.cardnoo.configure(font=('Comic Sans MS', 10))
        self.cardnoo.place(x=1270, y=350)

        self.cardnameo = Entry(self.root, width=20)
        self.cardnameo.configure(font=('Comic Sans MS', 10))
        self.cardnameo.place(x=1270, y=450)

        self.cvvo = Entry(self.root, width=20)
        self.cvvo.configure(font=('Comic Sans MS', 10))
        self.cvvo.place(x=1270, y=550)

        puro = Button(self.root, text='PURCHASE', width=20,command=self.oerror)
        puro.configure(font=('Comic Sans MS', 10, 'bold'))
        puro.place(x=1270, y=650)

    def oerror(self):
        response=self.errorpur(self.cardnoo.get(),self.cardnameo.get(),self.cvvo.get())
        if response==0:
            messagebox.showerror('Error','Please fill all the blanks')
        elif response==1:
            messagebox.showerror('Error','Please enter card number with only digits / Check if it is of length 12')
        elif response==2:
            messagebox.showerror('Error','Please enter string characters in your name')
        elif response==3:
            messagebox.showerror('Error','Please enter cvv number with only digits / Check if it is of length 3')
        else:
            messagebox.showinfo('Success !!', 'Your payment has been successfully made \nYour items will be delivered soon !!')
            self.root.destroy()


    def cart_(self):
        self.clear()
        count=0
        cart_label = Label(self.root,text='MY CART', bg='#efedf1', fg='black')
        cart_label.configure(font=('Comic Sans MS', 30, 'bold underline'))
        cart_label.pack(pady=(25, 20))

        backcart_button = Button(self.root,text='<- Back', command=self.main_screen)
        backcart_button.configure(font=('Comic Sans MS', 10, 'bold'))
        backcart_button.place(x=20, y=32, anchor=NW, width=80, height=40)
        if self.a:
            cart0_label = Label(self.root, text='\n\nYOUR CART IS EMPTY !! \n PURCHASE FRUITS TO SEE THE BILLS HERE', bg='#efedf1', fg='black')
            cart0_label.configure(font=('Comic Sans MS', 40, 'bold'))
            cart0_label.pack(pady=(100, 100))
        elif self.bcount==1 and self.acount==1 and self.ocount==1:
            canvas = Canvas(bg='#efedf1', width=800, height=800, highlightbackground='black', highlightthickness=5)
            canvas.place(x=310, y=150)
            canvas = Canvas(bg='#efedf1', width=300, height=800, highlightbackground='black', highlightthickness=5)
            canvas.place(x=1200, y=150)
            path1 = "Images/banana.png"
            image1 = Image.open(path1)
            img1 = ImageTk.PhotoImage(image1.resize((200, 200)))
            banana = Label(self.root, image=img1, bg='#efedf1')
            banana.photo = img1
            banana.place(x=400, y=200)

            banana_quan = Label(self.root, text='Quantity (KG)     :', bg='#efedf1', fg='black')
            banana_quan.configure(font=('Comic Sans MS', 15))
            banana_quan.place(x=700, y=220)

            banana_price = Label(self.root, text='Price (per KG)    :', bg='#efedf1', fg='black')
            banana_price.configure(font=('Comic Sans MS', 15))
            banana_price.place(x=700, y=280)

            self.purquanb = Label(self.root, text=self.main.purbquan, bg='#efedf1', fg='black')
            self.purquanb.configure(font=('Comic Sans MS', 15))
            self.purquanb.place(x=900, y=220)

            price_b = Label(self.root, text=self.main.b_price, bg='#efedf1', fg='black')
            price_b.configure(font=('Comic Sans MS', 15))
            price_b.place(x=900, y=280)

            price_total = Label(self.root, text='Total                  :', bg='#efedf1', fg='black')
            price_total.configure(font=('Comic Sans MS', 15))
            price_total.place(x=700, y=340)

            total_price_b = Label(self.root, text=price_b['text'] * self.purquanb['text'], bg='#efedf1', fg='black')
            total_price_b.configure(font=('Comic Sans MS', 15))
            total_price_b.place(x=900, y=340)

            path2 = "Images/apple.png"
            image2 = Image.open(path2)
            img2 = ImageTk.PhotoImage(image2.resize((200, 200)))
            apple = Label(self.root, image=img2, bg='#efedf1')
            apple.photo = img2
            apple.place(x=400, y=450)

            apple_quan = Label(self.root, text='Quantity (KG)     :', bg='#efedf1', fg='black')
            apple_quan.configure(font=('Comic Sans MS', 15))
            apple_quan.place(x=700, y=500)

            apple_price = Label(self.root, text='Price (per KG)     :', bg='#efedf1', fg='black')
            apple_price.configure(font=('Comic Sans MS', 15))
            apple_price.place(x=700, y=560)

            self.purquana = Label(self.root, text=self.main.puraquan, bg='#efedf1', fg='black')
            self.purquana.configure(font=('Comic Sans MS', 15))
            self.purquana.place(x=900, y=500)

            price_a = Label(self.root, text=self.main.a_price, bg='#efedf1', fg='black')
            price_a.configure(font=('Comic Sans MS', 15))
            price_a.place(x=900, y=560)

            price_total = Label(self.root, text='Total                  :', bg='#efedf1', fg='black')
            price_total.configure(font=('Comic Sans MS', 15))
            price_total.place(x=700, y=620)

            total_price_a = Label(self.root, text=price_a['text'] * self.purquana['text'], bg='#efedf1', fg='black')
            total_price_a.configure(font=('Comic Sans MS', 15))
            total_price_a.place(x=900, y=620)

            path3 = "Images/orange.png"
            image3 = Image.open(path3)
            img3 = ImageTk.PhotoImage(image3.resize((200, 200)))
            orange = Label(self.root, image=img3, bg='#efedf1')
            orange.photo = img3
            orange.place(x=400, y=730)

            orange_quan = Label(self.root, text='Quantity (KG)     :', bg='#efedf1', fg='black')
            orange_quan.configure(font=('Comic Sans MS', 15))
            orange_quan.place(x=700, y=760)

            orange_price = Label(self.root, text='Price (per KG)     :', bg='#efedf1', fg='black')
            orange_price.configure(font=('Comic Sans MS', 15))
            orange_price.place(x=700, y=820)

            self.purquano = Label(self.root, text=self.main.puroquan, bg='#efedf1', fg='black')
            self.purquano.configure(font=('Comic Sans MS', 15))
            self.purquano.place(x=900, y=760)

            price_o = Label(self.root, text=self.main.o_price, bg='#efedf1', fg='black')
            price_o.configure(font=('Comic Sans MS', 15))
            price_o.place(x=900, y=820)

            price_total = Label(self.root, text='Total                  :', bg='#efedf1', fg='black')
            price_total.configure(font=('Comic Sans MS', 15))
            price_total.place(x=700, y=880)

            total_price_o = Label(self.root, text=price_o['text'] * self.purquano['text'], bg='#efedf1', fg='black')
            total_price_o.configure(font=('Comic Sans MS', 15))
            total_price_o.place(x=900, y=880)

            self.total_label()
            self.quan_label()
            self.price_label()
            self.purchase_label()
            self.total_value(self.purquanb['text'] + self.purquana['text'] + self.purquano['text'], total_price_b['text'] + total_price_a['text'] + total_price_o['text'])

            self.l=self.main.combination(total_price_b['text'] + total_price_a['text'] + total_price_o['text'])

            cash_button = Button(self.root, text='CASH', width=15, height=1,command=self.cashbao)
            cash_button.configure(font=('Comic Sans MS', 10, 'bold'))
            cash_button.place(x=1290, y=600)

            card_button = Button(self.root, text='CARD', width=15, height=1,command=self.cardbao)
            card_button.configure(font=('Comic Sans MS', 10, 'bold'))
            card_button.place(x=1290, y=660)

        elif self.bcount==1 and self.acount==1:

            canvas = Canvas(bg='#efedf1', width=800, height=800, highlightbackground='black', highlightthickness=5)
            canvas.place(x=310, y=150)
            canvas = Canvas(bg='#efedf1', width=300, height=800, highlightbackground='black', highlightthickness=5)
            canvas.place(x=1200, y=150)
            path1 = "Images/banana.png"
            image1 = Image.open(path1)
            img1 = ImageTk.PhotoImage(image1.resize((200, 200)))
            banana = Label(self.root, image=img1, bg='#efedf1')
            banana.photo = img1
            banana.place(x=400, y=200)

            banana_quan = Label(self.root, text='Quantity (KG)     :', bg='#efedf1', fg='black')
            banana_quan.configure(font=('Comic Sans MS', 15))
            banana_quan.place(x=700, y=220)

            banana_price = Label(self.root, text='Price (per KG)    :', bg='#efedf1', fg='black')
            banana_price.configure(font=('Comic Sans MS', 15))
            banana_price.place(x=700, y=280)

            self.purquanb = Label(self.root, text=self.main.purbquan, bg='#efedf1', fg='black')
            self.purquanb.configure(font=('Comic Sans MS', 15))
            self.purquanb.place(x=900, y=220)

            price_b = Label(self.root, text=self.main.b_price, bg='#efedf1', fg='black')
            price_b.configure(font=('Comic Sans MS', 15))
            price_b.place(x=900, y=280)

            price_total = Label(self.root, text='Total                  :', bg='#efedf1', fg='black')
            price_total.configure(font=('Comic Sans MS', 15))
            price_total.place(x=700, y=340)

            total_price_b = Label(self.root, text=price_b['text'] * self.purquanb['text'], bg='#efedf1', fg='black')
            total_price_b.configure(font=('Comic Sans MS', 15))
            total_price_b.place(x=900, y=340)

            path2 = "Images/apple.png"
            image2 = Image.open(path2)
            img2 = ImageTk.PhotoImage(image2.resize((200, 200)))
            apple = Label(self.root, image=img2, bg='#efedf1')
            apple.photo = img2
            apple.place(x=400, y=470)

            apple_quan = Label(self.root, text='Quantity (KG)     :', bg='#efedf1', fg='black')
            apple_quan.configure(font=('Comic Sans MS', 15))
            apple_quan.place(x=700, y=500)

            apple_price = Label(self.root, text='Price (per KG)     :', bg='#efedf1', fg='black')
            apple_price.configure(font=('Comic Sans MS', 15))
            apple_price.place(x=700, y=560)

            self.purquana = Label(self.root, text=self.main.puraquan, bg='#efedf1', fg='black')
            self.purquana.configure(font=('Comic Sans MS', 15))
            self.purquana.place(x=900, y=500)

            price_a = Label(self.root, text=self.main.a_price, bg='#efedf1', fg='black')
            price_a.configure(font=('Comic Sans MS', 15))
            price_a.place(x=900, y=560)

            price_total = Label(self.root, text='Total                  :', bg='#efedf1', fg='black')
            price_total.configure(font=('Comic Sans MS', 15))
            price_total.place(x=700, y=620)

            total_price_a = Label(self.root, text=price_a['text'] * self.purquana['text'], bg='#efedf1', fg='black')
            total_price_a.configure(font=('Comic Sans MS', 15))
            total_price_a.place(x=900, y=620)

            self.total_label()
            self.quan_label()
            self.price_label()
            self.purchase_label()
            self.total_value(self.purquanb['text'] + self.purquana['text'], total_price_b['text'] + total_price_a['text'])

            self.l = self.main.combination(total_price_b['text'] + total_price_a['text'])

            cash_button = Button(self.root, text='CASH', width=15, height=1, command=self.cashba)
            cash_button.configure(font=('Comic Sans MS', 10, 'bold'))
            cash_button.place(x=1290, y=600)

            card_button = Button(self.root, text='CARD', width=15, height=1, command=self.cardba)
            card_button.configure(font=('Comic Sans MS', 10, 'bold'))
            card_button.place(x=1290, y=660)

        elif self.acount==1 and self.ocount==1:

            canvas = Canvas(bg='#efedf1', width=800, height=800, highlightbackground='black', highlightthickness=5)
            canvas.place(x=310, y=150)
            canvas = Canvas(bg='#efedf1', width=300, height=800, highlightbackground='black', highlightthickness=5)
            canvas.place(x=1200, y=150)
            path2 = "Images/apple.png"
            image2 = Image.open(path2)
            img2 = ImageTk.PhotoImage(image2.resize((200, 200)))
            apple = Label(self.root, image=img2, bg='#efedf1')
            apple.photo = img2
            apple.place(x=400, y=200)

            apple_quan = Label(self.root, text='Quantity (KG)     :', bg='#efedf1', fg='black')
            apple_quan.configure(font=('Comic Sans MS', 15))
            apple_quan.place(x=700, y=220)

            apple_price = Label(self.root, text='Price (per KG)     :', bg='#efedf1', fg='black')
            apple_price.configure(font=('Comic Sans MS', 15))
            apple_price.place(x=700, y=280)

            self.purquana = Label(self.root, text=self.main.puraquan, bg='#efedf1', fg='black')
            self.purquana.configure(font=('Comic Sans MS', 15))
            self.purquana.place(x=900, y=220)

            price_a = Label(self.root, text=self.main.a_price, bg='#efedf1', fg='black')
            price_a.configure(font=('Comic Sans MS', 15))
            price_a.place(x=900, y=280)

            price_total = Label(self.root, text='Total                  :', bg='#efedf1', fg='black')
            price_total.configure(font=('Comic Sans MS', 15))
            price_total.place(x=700, y=340)

            total_price_a = Label(self.root, text=price_a['text'] * self.purquana['text'], bg='#efedf1', fg='black')
            total_price_a.configure(font=('Comic Sans MS', 15))
            total_price_a.place(x=900, y=340)

            path3 = "Images/orange.png"
            image3 = Image.open(path3)
            img3 = ImageTk.PhotoImage(image3.resize((200, 200)))
            orange = Label(self.root, image=img3, bg='#efedf1')
            orange.photo = img3
            orange.place(x=400, y=470)

            orange_quan = Label(self.root, text='Quantity (KG)     :', bg='#efedf1', fg='black')
            orange_quan.configure(font=('Comic Sans MS', 15))
            orange_quan.place(x=700, y=500)

            orange_price = Label(self.root, text='Price (per KG)     :', bg='#efedf1', fg='black')
            orange_price.configure(font=('Comic Sans MS', 15))
            orange_price.place(x=700, y=560)

            self.purquano = Label(self.root, text=self.main.puroquan, bg='#efedf1', fg='black')
            self.purquano.configure(font=('Comic Sans MS', 15))
            self.purquano.place(x=900, y=500)

            price_o = Label(self.root, text=self.main.o_price, bg='#efedf1', fg='black')
            price_o.configure(font=('Comic Sans MS', 15))
            price_o.place(x=900, y=560)

            price_total = Label(self.root, text='Total                  :', bg='#efedf1', fg='black')
            price_total.configure(font=('Comic Sans MS', 15))
            price_total.place(x=700, y=620)

            total_price_o = Label(self.root, text=price_o['text'] * self.purquano['text'], bg='#efedf1', fg='black')
            total_price_o.configure(font=('Comic Sans MS', 15))
            total_price_o.place(x=900, y=620)

            self.total_label()
            self.quan_label()
            self.price_label()
            self.purchase_label()
            self.total_value(self.purquana['text'] + self.purquano['text'], total_price_a['text'] + total_price_o['text'])

            self.l = self.main.combination(total_price_a['text'] + total_price_o['text'])

            cash_button = Button(self.root, text='CASH', width=15, height=1, command=self.cashao)
            cash_button.configure(font=('Comic Sans MS', 10, 'bold'))
            cash_button.place(x=1290, y=600)

            card_button = Button(self.root, text='CARD', width=15, height=1, command=self.cardao)
            card_button.configure(font=('Comic Sans MS', 10, 'bold'))
            card_button.place(x=1290, y=660)


        elif self.ocount==1 and self.bcount==1:
            canvas = Canvas(bg='#efedf1', width=800, height=800, highlightbackground='black', highlightthickness=5)
            canvas.place(x=310, y=150)
            canvas = Canvas(bg='#efedf1', width=300, height=800, highlightbackground='black', highlightthickness=5)
            canvas.place(x=1200, y=150)
            path1 = "Images/banana.png"
            image1 = Image.open(path1)
            img1 = ImageTk.PhotoImage(image1.resize((200, 200)))
            banana = Label(self.root, image=img1, bg='#efedf1')
            banana.photo = img1
            banana.place(x=400, y=200)

            banana_quan = Label(self.root, text='Quantity (KG)     :', bg='#efedf1', fg='black')
            banana_quan.configure(font=('Comic Sans MS', 15))
            banana_quan.place(x=700, y=220)

            banana_price = Label(self.root, text='Price (per KG)    :', bg='#efedf1', fg='black')
            banana_price.configure(font=('Comic Sans MS', 15))
            banana_price.place(x=700, y=280)

            self.purquanb = Label(self.root, text=self.main.purbquan, bg='#efedf1', fg='black')
            self.purquanb.configure(font=('Comic Sans MS', 15))
            self.purquanb.place(x=900, y=220)

            price_b = Label(self.root, text=self.main.b_price, bg='#efedf1', fg='black')
            price_b.configure(font=('Comic Sans MS', 15))
            price_b.place(x=900, y=280)

            price_total = Label(self.root, text='Total                  :', bg='#efedf1', fg='black')
            price_total.configure(font=('Comic Sans MS', 15))
            price_total.place(x=700, y=340)

            total_price_b = Label(self.root, text=price_b['text'] * self.purquanb['text'], bg='#efedf1', fg='black')
            total_price_b.configure(font=('Comic Sans MS', 15))
            total_price_b.place(x=900, y=340)

            path3 = "Images/orange.png"
            image3 = Image.open(path3)
            img3 = ImageTk.PhotoImage(image3.resize((200, 200)))
            orange = Label(self.root, image=img3, bg='#efedf1')
            orange.photo = img3
            orange.place(x=400, y=470)

            orange_quan = Label(self.root, text='Quantity (KG)     :', bg='#efedf1', fg='black')
            orange_quan.configure(font=('Comic Sans MS', 15))
            orange_quan.place(x=700, y=500)

            orange_price = Label(self.root, text='Price (per KG)     :', bg='#efedf1', fg='black')
            orange_price.configure(font=('Comic Sans MS', 15))
            orange_price.place(x=700, y=560)

            self.purquano = Label(self.root, text=self.main.puroquan, bg='#efedf1', fg='black')
            self.purquano.configure(font=('Comic Sans MS', 15))
            self.purquano.place(x=900, y=500)

            price_o = Label(self.root, text=self.main.o_price, bg='#efedf1', fg='black')
            price_o.configure(font=('Comic Sans MS', 15))
            price_o.place(x=900, y=560)

            price_total = Label(self.root, text='Total                  :', bg='#efedf1', fg='black')
            price_total.configure(font=('Comic Sans MS', 15))
            price_total.place(x=700, y=620)

            total_price_o = Label(self.root, text=price_o['text'] * self.purquano['text'], bg='#efedf1', fg='black')
            total_price_o.configure(font=('Comic Sans MS', 15))
            total_price_o.place(x=900, y=620)

            self.total_label()
            self.quan_label()
            self.price_label()
            self.purchase_label()
            self.total_value(self.purquanb['text']+self.purquano['text'],total_price_b['text']+total_price_o['text'])

            self.l = self.main.combination(total_price_o['text'] + total_price_b['text'])

            cash_button = Button(self.root, text='CASH', width=15, height=1, command=self.cashob)
            cash_button.configure(font=('Comic Sans MS', 10, 'bold'))
            cash_button.place(x=1290, y=600)

            card_button = Button(self.root, text='CARD', width=15, height=1, command=self.cardob)
            card_button.configure(font=('Comic Sans MS', 10, 'bold'))
            card_button.place(x=1290, y=660)


        elif self.bcount==1 and self.main.fruit=='banana':

            canvas = Canvas(bg='#efedf1', width=800, height=800, highlightbackground='black', highlightthickness=5)
            canvas.place(x=310, y=150)
            canvas = Canvas(bg='#efedf1', width=300, height=800, highlightbackground='black', highlightthickness=5)
            canvas.place(x=1200, y=150)
            path1 = "Images/banana.png"
            image1 = Image.open(path1)
            img1 = ImageTk.PhotoImage(image1.resize((200, 200)))
            banana = Label(self.root, image=img1, bg='#efedf1')
            banana.photo = img1
            banana.place(x=400, y=200)

            banana_quan = Label(self.root, text='Quantity (KG)     :', bg='#efedf1', fg='black')
            banana_quan.configure(font=('Comic Sans MS', 15))
            banana_quan.place(x=700, y=220)

            banana_price = Label(self.root, text='Price (per KG)    :', bg='#efedf1', fg='black')
            banana_price.configure(font=('Comic Sans MS', 15))
            banana_price.place(x=700, y=280)

            self.purquanb = Label(self.root, text=self.main.purbquan, bg='#efedf1', fg='black')
            self.purquanb.configure(font=('Comic Sans MS', 15))
            self.purquanb.place(x=900, y=220)

            price_b = Label(self.root, text=self.main.b_price, bg='#efedf1', fg='black')
            price_b.configure(font=('Comic Sans MS', 15))
            price_b.place(x=900, y=280)

            price_total = Label(self.root, text='Total                  :', bg='#efedf1', fg='black')
            price_total.configure(font=('Comic Sans MS', 15))
            price_total.place(x=700, y=340)

            total_price_b = Label(self.root, text=price_b['text']*self.purquanb['text'], bg='#efedf1', fg='black')
            total_price_b.configure(font=('Comic Sans MS', 15))
            total_price_b.place(x=900, y=340)

            self.total_label()
            self.quan_label()
            self.price_label()
            self.purchase_label()
            self.total_value(self.purquanb['text'],total_price_b['text'])

            self.l = self.main.combination(total_price_b['text'])

            cash_button = Button(self.root, text='CASH', width=15, height=1, command=self.cashb)
            cash_button.configure(font=('Comic Sans MS', 10, 'bold'))
            cash_button.place(x=1290, y=600)

            card_button = Button(self.root, text='CARD', width=15, height=1, command=self.cardb)
            card_button.configure(font=('Comic Sans MS', 10, 'bold'))
            card_button.place(x=1290, y=660)


        elif self.acount==1 and self.main.fruit=='apple':

            canvas = Canvas(bg='#efedf1', width=800, height=800, highlightbackground='black', highlightthickness=5)
            canvas.place(x=310, y=150)
            canvas = Canvas(bg='#efedf1', width=300, height=800, highlightbackground='black', highlightthickness=5)
            canvas.place(x=1200, y=150)
            path2 = "Images/apple.png"
            image2 = Image.open(path2)
            img2 = ImageTk.PhotoImage(image2.resize((200, 200)))
            apple = Label(self.root, image=img2, bg='#efedf1')
            apple.photo = img2
            apple.place(x=400, y=200)

            apple_quan = Label(self.root, text='Quantity (KG)     :', bg='#efedf1', fg='black')
            apple_quan.configure(font=('Comic Sans MS', 15))
            apple_quan.place(x=700, y=220)

            apple_price = Label(self.root, text='Price (per KG)     :', bg='#efedf1', fg='black')
            apple_price.configure(font=('Comic Sans MS', 15))
            apple_price.place(x=700, y=280)


            self.purquana = Label(self.root, text=self.main.puraquan, bg='#efedf1', fg='black')
            self.purquana.configure(font=('Comic Sans MS', 15))
            self.purquana.place(x=900, y=220)

            price_a = Label(self.root, text=self.main.a_price, bg='#efedf1', fg='black')
            price_a.configure(font=('Comic Sans MS', 15))
            price_a.place(x=900, y=280)

            price_total = Label(self.root, text='Total                  :', bg='#efedf1', fg='black')
            price_total.configure(font=('Comic Sans MS', 15))
            price_total.place(x=700, y=340)

            total_price_a = Label(self.root, text=price_a['text'] * self.purquana['text'], bg='#efedf1', fg='black')
            total_price_a.configure(font=('Comic Sans MS', 15))
            total_price_a.place(x=900, y=340)

            self.total_label()
            self.quan_label()
            self.price_label()
            self.purchase_label()
            self.total_value(self.purquana['text'],total_price_a['text'])

            self.l = self.main.combination(total_price_a['text'])

            cash_button = Button(self.root, text='CASH', width=15, height=1, command=self.casha)
            cash_button.configure(font=('Comic Sans MS', 10, 'bold'))
            cash_button.place(x=1290, y=600)

            card_button = Button(self.root, text='CARD', width=15, height=1, command=self.carda)
            card_button.configure(font=('Comic Sans MS', 10, 'bold'))
            card_button.place(x=1290, y=660)



        elif self.ocount==1 and self.main.fruit=='orange':

            canvas = Canvas(bg='#efedf1', width=800, height=800, highlightbackground='black', highlightthickness=5)
            canvas.place(x=310, y=150)
            canvas1 = Canvas(bg='#efedf1', width=300, height=800, highlightbackground='black', highlightthickness=5)
            canvas1.place(x=1200, y=150)
            path3 = "Images/orange.png"
            image3 = Image.open(path3)
            img3 = ImageTk.PhotoImage(image3.resize((200, 200)))
            orange = Label(self.root, image=img3, bg='#efedf1')
            orange.photo = img3
            orange.place(x=400, y=200)

            orange_quan = Label(self.root, text='Quantity (KG)     :', bg='#efedf1', fg='black')
            orange_quan.configure(font=('Comic Sans MS', 15))
            orange_quan.place(x=700, y=220)

            orange_price = Label(self.root, text='Price (per KG)     :', bg='#efedf1', fg='black')
            orange_price.configure(font=('Comic Sans MS', 15))
            orange_price.place(x=700, y=280)

            self.purquano = Label(self.root, text=self.main.puroquan, bg='#efedf1', fg='black')
            self.purquano.configure(font=('Comic Sans MS', 15))
            self.purquano.place(x=900, y=220)

            price_o = Label(self.root, text=self.main.o_price, bg='#efedf1', fg='black')
            price_o.configure(font=('Comic Sans MS', 15))
            price_o.place(x=900, y=280)

            price_total = Label(self.root, text='Total                  :', bg='#efedf1', fg='black')
            price_total.configure(font=('Comic Sans MS', 15))
            price_total.place(x=700, y=340)

            total_price_o = Label(self.root, text=price_o['text'] * self.purquano['text'], bg='#efedf1', fg='black')
            total_price_o.configure(font=('Comic Sans MS', 15))
            total_price_o.place(x=900, y=340)

            self.total_label()
            self.quan_label()
            self.price_label()
            self.purchase_label()
            self.total_value(self.purquano['text'],total_price_o['text'])

            self.l = self.main.combination(total_price_o['text'])

            cash_button = Button(self.root, text='CASH', width=15, height=1, command=self.casho)
            cash_button.configure(font=('Comic Sans MS', 10, 'bold'))
            cash_button.place(x=1290, y=600)

            card_button = Button(self.root, text='CARD', width=15, height=1, command=self.cardo)
            card_button.configure(font=('Comic Sans MS', 10, 'bold'))
            card_button.place(x=1290, y=660)

    def total_label(self):
        total_label = Label(self.root, text='TOTAL', bg='#efedf1', fg='black')
        total_label.configure(font=('Comic Sans MS', 25, 'bold underline'))
        total_label.place(x=1290, y=200)
    def quan_label(self):
        total_quan_label = Label(self.root, text='Quantity', bg='#efedf1', fg='black')
        total_quan_label.configure(font=('Comic Sans MS', 20, 'bold underline'))
        total_quan_label.place(x=1290, y=280)
    def price_label(self):
        total_price_label = Label(self.root, text='Price', bg='#efedf1', fg='black')
        total_price_label.configure(font=('Comic Sans MS', 20, 'bold underline'))
        total_price_label.place(x=1315, y=380)
    def purchase_label(self):
        pur_label = Label(self.root, text='PURCHASE', bg='#efedf1', fg='black')
        pur_label.configure(font=('Comic Sans MS', 25, 'bold underline'))
        pur_label.place(x=1260, y=500)
    def total_value(self,quan,price):
        quan=quan
        price=price
        total_quan = Label(self.root, text=quan, bg='#efedf1', fg='black')
        total_quan.configure(font=('Comic Sans MS', 20, 'bold'))
        total_quan.place(x=1330, y=330)
        if len(str(price))==2:
            total_price = Label(self.root, text=' '+str(price), bg='#efedf1', fg='black')
            total_price.configure(font=('Comic Sans MS', 20, 'bold'))
            total_price.place(x=1315, y=440)
        elif len(str(price))==3:
            total_price = Label(self.root, text=str(price), bg='#efedf1', fg='black')
            total_price.configure(font=('Comic Sans MS', 20, 'bold'))
            total_price.place(x=1320, y=440)
        elif len(str(price))==4:
            total_price = Label(self.root, text=str(price), bg='#efedf1', fg='black')
            total_price.configure(font=('Comic Sans MS', 20, 'bold'))
            total_price.place(x=1315, y=440)
main()