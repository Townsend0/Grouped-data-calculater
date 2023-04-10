import tkinter, tkinter.messagebox
from Backend import Stats
COLOR = "darkslategrey"

class GUI(Stats):
    
    def make(self):
        self.window = tkinter.Tk()
        self.window.config(bg = COLOR)
        self.window.title("Statistics")
        self.window.geometry("800x700")
        
        
    def entries(self):
        
        def del_1(event):
            self.entr1.delete(0, "end")
        def del_2(event):
            self.entr2.delete(0, "end")
            
        self.entr1 = tkinter.Entry()
        self.entr2 = tkinter.Entry()
        self.entr1.insert(0, "seperate the values by -")
        self.entr1.bind("<FocusIn>", del_1)
        self.entr2.insert(0, "seperate the values by -")
        self.entr2.bind("<FocusIn>", del_2)
        self.entr1.place(x = 145, y = 200)
        self.entr2.place(x = 525, y = 200)
        
        
    def labels(self):
        self.title = tkinter.Label(bg = COLOR, text = "Grouped data calculater".title(), font = ("arial", 30, "normal"))
        self.title.pack(pady = 50)
        self.lbl_entr1 = tkinter.Label(bg = COLOR, text = "First row")
        self.lbl_entr2 = tkinter.Label(bg = COLOR, text = "Frequency")
        self.lbl_entr1.place(x = 50, y = 200)
        self.lbl_entr2.place(x = 420, y = 200)
        
        
    def f_result(self):
        
        self.result = tkinter.Label(bg = COLOR, text = "Answer")
        self.result.place(x = 600, y = 400)
        self.img = tkinter.PhotoImage(file = "start-button-50x50.png")
        self.clk = tkinter.Button(highlightthickness = 0, bg = COLOR, text = "Calculate", command = self.selected, image = self.img)
        self.clk.pack(side = "bottom", pady = 50)
        
        
    def radio_buttons(self):
        
        self.select = tkinter.IntVar()
        self.a1 = tkinter.Radiobutton(highlightthickness = 0, bg = COLOR, text = "Mean", variable = self.select, value = 1)
        self.a1.place(x = 37, y = 300)
        self.a2 = tkinter.Radiobutton(highlightthickness = 0, bg = COLOR, text = "Mode", variable = self.select, value = 2)
        self.a2.place(x = 37, y = 325)
        self.a3 = tkinter.Radiobutton(highlightthickness = 0, bg = COLOR, text = "Median", variable = self.select, value = 3)
        self.a3.place(x = 37, y = 350)
        self.a4 = tkinter.Radiobutton(highlightthickness = 0, bg = COLOR, text = "Q1", variable = self.select, value = 4)
        self.a4.place(x = 37, y = 375)
        self.a5 = tkinter.Radiobutton(highlightthickness = 0, bg = COLOR, text = "Q3", variable = self.select, value = 5)
        self.a5.place(x = 37, y = 400)
        self.a6 = tkinter.Radiobutton(highlightthickness = 0, bg = COLOR, text = "Variance", variable = self.select, value = 6)
        self.a6.place(x = 37, y = 425)
        self.a7 = tkinter.Radiobutton(highlightthickness = 0, bg = COLOR, text = "Standard deviathion", variable = self.select, value = 7)
        self.a7.place(x = 37, y = 450)
        self.a8 = tkinter.Radiobutton(highlightthickness = 0, bg = COLOR, text = "OMS", variable = self.select, value = 8)
        self.a8.place(x = 37, y = 475)
        self.a9 = tkinter.Radiobutton(highlightthickness = 0, bg = COLOR, text = "SKp", variable = self.select, value = 9)
        self.a9.place(x = 37, y = 500)
        
        
    def selected(self):
        
        try:
            match self.select.get():
                
                case 1:
                    self.result.config(text = self.f_mean())
                    
                case 2:
                    self.result.config(text = self.f_mode())
                    
                case 3:
                    self.result.config(text = self.f_median())
                    
                case 4:
                    self.result.config(text = self.f_q1())
                    
                case 5:
                    self.result.config(text = self.f_q3())
                    
                case 6:
                    self.result.config(text = self.f_variance())
                    
                case 7:
                    self.result.config(text = self.f_standard_deviation())
                    
                case 8:
                    self.result.config(text = self.f_oms())
                    
                case 9:
                    self.result.config(text = self.f_skp())
                        
                case _:
                    tkinter.messagebox.showerror("Error", "Select a radiobutton first")
                    
        except:
            tkinter.messagebox.showerror("Error", "Wrong data")