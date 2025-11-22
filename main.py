from customtkinter import *

class MainWindow(CTk):
    def __init__(self):#self  - screen
        super().__init__()
        self.geometry('600x450')
        self.minsize(600, 450)
        set_appearance_mode('system')

        #menu  - ui
        self.menu = CTkFrame(self, width = 200, height= 400)
        self.label_userName = CTkLabel(self.menu,text='User Name',
                                  font=('Times New Roman', 18, 'normal'),
                                  anchor='w',
                                  width = 190)
        self.entry_userName = CTkEntry(self.menu, placeholder_text='...',width = 190)
        self.btn_name = CTkButton(self.menu,text='Change name', 
                                  font=('Times New Roman',16,'normal'),
                                  width=190,
                                  command=self.change_name)
        self.theme = CTkOptionMenu(self.menu, values=['system', 'dark','light'], 
                                   width = 190, 
                                   font=('Times New Roman',16,'normal'),
                                   dropdown_font=('Times New Roman', 14),
                                   command=self.change_theme)
        #menu - pos
        self.label_userName.pack(pady = (150, 10), padx = 5)
        self.entry_userName.pack(padx = 5)
        self.btn_name.pack(padx=5,pady=(5,0))
        self.theme.pack(pady=(50,0), padx=5)
        #
        self.menu.place(x=0, y =0)
        self.menu.pack_propagate(False)
        #
        self.menu.configure(width=0)
        #chat ui
        self.btn_menu = CTkButton(self, text='☰', width = 30, height = 30,
                                  command=self.change_state)
        self.chat = CTkTextbox(self,state="disabled", fg_color='white')
        self.message = CTkEntry(self, placeholder_text='щось пиши...')
        self.send_message = CTkButton(self, text='▶', width = 50, height =30)
        #chat pos
        self.send_message.place(x = 545, y = 365)
        self.btn_menu.place(x = 5, y = 5)
        self.chat.place(x = 5, y = 40)
        self.message.place(x = 5, y = 365)
        #burger_menu
        self.max_size = 200
        self.speed = 20
        self.menu_state = False
        self.size_menu = 0 
        #
        self.user_name = '007'



        self.adaptive_ui()

    def change_theme(self, value):
        set_appearance_mode(value)

    def change_name(self):
        name = self.entry_userName.get()
        if name:
            self.user_name = name
            self.entry_userName.delete(0, 'end')
            print(self.user_name)

    def show_menu(self):
        if self.size_menu <= self.max_size:
            if self.size_menu > 30:
                self.btn_menu.configure(text='MENU ☰')
            self.size_menu += self.speed
            self.btn_menu.configure(width = self.size_menu - 10)
            self.menu.configure(width = self.size_menu)
        if self.menu_state:
            self.after(20, self.show_menu)
    
    def hide_menu(self):
        if self.size_menu > 0:
            if self.size_menu <30:
                self.btn_menu.configure(text='☰')
                self.btn_menu.configure(width=30)
            else:
                self.btn_menu.configure(width=self.size_menu)
            self.size_menu -= self.speed
            self.menu.configure(width = self.size_menu)
        if not self.menu_state:
            self.after(20, self.hide_menu)

    def change_state(self):
        if self.menu_state:
            self.menu_state = False
            self.hide_menu()
            
        else:
            self.menu_state = True
            self.show_menu()
            


    
    def adaptive_ui(self):
        k = 1.25
        w_w = self.winfo_width() / k
        w_h = self.winfo_height() / k
        btn_w = w_w / 12
        btn_h = w_h / 13.3
        #size
        self.send_message.configure(width = btn_w, height = btn_h)
        self.menu.configure(height = w_h)
        self.chat.configure(width = w_w - 10 - self.size_menu,
                            height = w_h - btn_h - 20 - 30)
        self.message.configure(width = w_w - btn_w - 10 - self.size_menu, height = btn_h)
        #place
        self.send_message.place(x = w_w - btn_w, y = w_h - btn_h)
        self.message.place(y = w_h - btn_h, x = self.size_menu + 5)
        self.chat.place(x = self.size_menu + 5)
        self.after(50, self.adaptive_ui)


app = MainWindow()
app.mainloop()