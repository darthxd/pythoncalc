import customtkinter as ctk
import re

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Python Calculator')
        self.geometry('400x600')
        self.resizable(False,False)

        #main frame
        self.frame = ctk.CTkFrame(self, width=400, height=600, fg_color='#0F0F0F')
        self.frame.pack(fill='both', expand=True)

        def addnum(num):
            if self.screen.cget('text') == '0':
                self.screen.configure(text='')

            self.screen.configure(text=self.screen.cget('text') + str(num))

        def clear():
            self.screen.configure(text='0')

        def operation(ope):
            operators = ('+', '-', '*', '/')
            text = self.screen.cget('text')
            if text.endswith(operators):
                pass
            else:
                self.screen.configure(text=text + str(ope))

        def result():
            value = str(self.screen.cget('text').replace('%','/100*'))
            res = str(eval(value))
            
            self.screen.configure(text=res)
        
        def percentage():
            operators = ('+', '-', '*', '/')
            text = self.screen.cget('text')
            if text.endswith(operators):
                pass
            else:
                self.screen.configure(text=self.screen.cget('text') + '%')

        def dot():
            operators = ('+', '-', '*', '/')
            text = self.screen.cget('text')
            if text.endswith(operators):
                pass
            else:
                self.screen.configure(text=text + '.')     

        #result screen
        self.screen = ctk.CTkLabel(self.frame, width=360, height=85, text='0', bg_color='#0F0F0F', font=('Segoe UI', 56), text_color='#D3D3D3', anchor='e', padx=20)
        self.screen.grid(row=0, column=0, columnspan=4, pady=(20,0), padx=20)

        #first row
        self.acbtn = ctk.CTkButton(self.frame, width=75, height=75, text='AC', font=('Segoe UI', 32), text_color='#0F0F0F', fg_color='#989898', hover_color='#989898', corner_radius=0,
                                    command=lambda: clear())
        self.acbtn.grid(row=1, column=0, pady=(20,0), padx=(20,0))

        self.xdbtn = ctk.CTkButton(self.frame, width=75, height=75, text='XD', font=('Segoe UI', 32), text_color='#0F0F0F', fg_color='#989898', hover_color='#989898', corner_radius=0)
        self.xdbtn.grid(row=1, column=1, pady=(20,0), padx=(20,0))

        self.percbtn = ctk.CTkButton(self.frame, width=75, height=75, text='%', font=('Segoe UI', 32), text_color='#0F0F0F', fg_color='#989898', hover_color='#989898', corner_radius=0,
                                     command=lambda: percentage())
        self.percbtn.grid(row=1, column=2, pady=(20,0), padx=(20,0))

        self.divbtn = ctk.CTkButton(self.frame, width=75, height=75, text='÷', font=('Segoe UI', 32), text_color='#0F0F0F', fg_color='#C87B21', hover_color='#C87B21', corner_radius=0,
                                    command=lambda: operation('/'))
        self.divbtn.grid(row=1, column=3, pady=(20,0), padx=(20))

        #second row
        self.sevbtn = ctk.CTkButton(self.frame, width=75, height=75, text='7', font=('Segoe UI', 32), text_color='#989898', fg_color='#2F2F2F', hover_color='#2F2F2F', corner_radius=0,
                                    command=lambda: addnum(7))
        self.sevbtn.grid(row=2, column=0, pady=(20,0), padx=(20,0))

        self.eightbtn = ctk.CTkButton(self.frame, width=75, height=75, text='8', font=('Segoe UI', 32), text_color='#989898', fg_color='#2F2F2F', hover_color='#2F2F2F', corner_radius=0,
                                    command=lambda: addnum(8))
        self.eightbtn.grid(row=2, column=1, pady=(20,0), padx=(20,0))

        self.ninebtn = ctk.CTkButton(self.frame, width=75, height=75, text='9', font=('Segoe UI', 32), text_color='#989898', fg_color='#2F2F2F', hover_color='#2F2F2F', corner_radius=0,
                                    command=lambda: addnum(9))
        self.ninebtn.grid(row=2, column=2, pady=(20,0), padx=(20,0))

        self.multbtn = ctk.CTkButton(self.frame, width=75, height=75, text='X', font=('Segoe UI', 32), text_color='#0F0F0F', fg_color='#C87B21', hover_color='#C87B21', corner_radius=0,
                                    command=lambda: operation('*'))
        self.multbtn.grid(row=2, column=3, pady=(20,0), padx=(20))

        #third row
        self.fourbtn = ctk.CTkButton(self.frame, width=75, height=75, text='4', font=('Segoe UI', 32), text_color='#989898', fg_color='#2F2F2F', hover_color='#2F2F2F', corner_radius=0,
                                    command=lambda: addnum(4))
        self.fourbtn.grid(row=3, column=0, pady=(20,0), padx=(20,0))

        self.fivebtn = ctk.CTkButton(self.frame, width=75, height=75, text='5', font=('Segoe UI', 32), text_color='#989898', fg_color='#2F2F2F', hover_color='#2F2F2F', corner_radius=0,
                                    command=lambda: addnum(5))
        self.fivebtn.grid(row=3, column=1, pady=(20,0), padx=(20,0))

        self.sixbtn = ctk.CTkButton(self.frame, width=75, height=75, text='6', font=('Segoe UI', 32), text_color='#989898', fg_color='#2F2F2F', hover_color='#2F2F2F', corner_radius=0,
                                    command=lambda: addnum(6))
        self.sixbtn.grid(row=3, column=2, pady=(20,0), padx=(20,0))

        self.subbtn = ctk.CTkButton(self.frame, width=75, height=75, text='-', font=('Segoe UI', 32), text_color='#0F0F0F', fg_color='#C87B21', hover_color='#C87B21', corner_radius=0,
                                    command=lambda: operation('-'))
        self.subbtn.grid(row=3, column=3, pady=(20,0), padx=(20))

        #fourth row
        self.onebtn = ctk.CTkButton(self.frame, width=75, height=75, text='1', font=('Segoe UI', 32), text_color='#989898', fg_color='#2F2F2F', hover_color='#2F2F2F', corner_radius=0,
                                    command=lambda: addnum(1))
        self.onebtn.grid(row=4, column=0, pady=(20,0), padx=(20,0))

        self.twobtn = ctk.CTkButton(self.frame, width=75, height=75, text='2', font=('Segoe UI', 32), text_color='#989898', fg_color='#2F2F2F', hover_color='#2F2F2F', corner_radius=0,
                                    command=lambda: addnum(2))
        self.twobtn.grid(row=4, column=1, pady=(20,0), padx=(20,0))

        self.threebtn = ctk.CTkButton(self.frame, width=75, height=75, text='3', font=('Segoe UI', 32), text_color='#989898', fg_color='#2F2F2F', hover_color='#2F2F2F', corner_radius=0,
                                    command=lambda: addnum(3))
        self.threebtn.grid(row=4, column=2, pady=(20,0), padx=(20,0))

        self.plusbtn = ctk.CTkButton(self.frame, width=75, height=75, text='+', font=('Segoe UI', 32), text_color='#0F0F0F', fg_color='#C87B21', hover_color='#C87B21', corner_radius=0,
                                    command=lambda: operation('+'))
        self.plusbtn.grid(row=4, column=3, pady=(20,0), padx=(20))

        #fourth row
        self.zerobtn = ctk.CTkButton(self.frame, width=170, height=75, text='0', font=('Segoe UI', 32), text_color='#989898', fg_color='#2F2F2F', hover_color='#2F2F2F', corner_radius=0,
                                    command=lambda: addnum(0))
        self.zerobtn.grid(row=5, column=0, columnspan=2, pady=(20,0), padx=(20,0))

        self.dotbtn = ctk.CTkButton(self.frame, width=75, height=75, text=',', font=('Segoe UI', 32), text_color='#989898', fg_color='#2F2F2F', hover_color='#2F2F2F', corner_radius=0,
                                    command=lambda: dot())
        self.dotbtn.grid(row=5, column=2, pady=(20,0), padx=(20,0))

        self.resbtn = ctk.CTkButton(self.frame, width=75, height=75, text='=', font=('Segoe UI', 32), text_color='#0F0F0F', fg_color='#C87B21', hover_color='#C87B21', corner_radius=0,
                                    command=lambda: result())
        self.resbtn.grid(row=5, column=3, pady=(20,0), padx=(20))

app = App()

if __name__ == '__main__':
    app.mainloop()