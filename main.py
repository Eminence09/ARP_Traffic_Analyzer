from tkinter import ttk
import tkinter as tk
import threading



LARGEFONT =("Verdana", 35)
devices = {}

class tkinterApp(tk.Tk):
    
	def __init__(self, *args, **kwargs): 
		
		tk.Tk.__init__(self, *args, **kwargs)
		
		container = tk.Frame(self) 
		container.pack(side = "top", fill = "both", expand = True) 

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		self.frames = {} 
		for F in (StartPage, Page1, Page2, Page3):

			frame = F(container, self)

			self.frames[F] = frame 

			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(StartPage)

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()


class StartPage(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)
		
		details = ">>>Government Polytechnic, Valsad.\n>>>Subject:_ Mobile Computing and Networking (Microproject)\nBanait Yash R. (226290316003)\nKhatri Abdullah P. (226290316020)\nNesneskar Tushar N. (226290316027)"
		label = ttk.Label(self, text=details , font = 12)
		
		label.grid(row = 0, column = 4, padx = 10, pady = 10) 

		button1 = ttk.Button(self, text ="Network Information",
		command = lambda : controller.show_frame(Page1))
	
		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

		button2 = ttk.Button(self, text ="Get MAC Address",
		command = lambda : controller.show_frame(Page2))
	
		button2.grid(row = 2, column = 1, padx = 10, pady = 10)
  
		button3 = ttk.Button(self, text ="ARP Traffic",
		command = lambda : controller.show_frame(Page3))
	
		button3.grid(row = 3, column = 1, padx = 19, pady = 10)

		
  
class Page1(tk.Frame):
	
	def __init__(self, parent, controller):
		
		tk.Frame.__init__(self, parent)
		path = r"ARP_GUI\\Network_Logs\\Network_info.log"
		with open(path, "r") as f:
			data = f.readlines()


		label = ttk.Label(self, text = data, font=4)
		label.grid(row = 0, column = 4, padx = 10, pady = 10)
		
		button1 = ttk.Button(self, text ="StartPage",
							command = lambda : controller.show_frame(StartPage))
	
		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

		button2 = ttk.Button(self, text ="Get MAC Address",
							command = lambda : controller.show_frame(Page2))
	
		button2.grid(row = 2, column = 1, padx = 10, pady = 10)
  
		button3 = ttk.Button(self, text ="ARP Traffic",
							command = lambda : controller.show_frame(Page3))
	
		button3.grid(row = 3, column = 1, padx = 10, pady = 10)



class Page2(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        path = r"ARP_GUI\\Network_Logs\\get_mac.log"
        with open(path, "r") as f:
            data = f.readlines()
            

            
        label = ttk.Label(self, text=data, font = ('Helvetica', 12))
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
        
        button1 = ttk.Button(self, text ="Network Information",
							command = lambda : controller.show_frame(Page1))
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
        button2 = ttk.Button(self, text ="Startpage",
							command = lambda : controller.show_frame(StartPage))
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
        button3 = ttk.Button(self, text ="ARP Traffic",
							command = lambda : controller.show_frame(Page3))
        button3.grid(row = 3, column = 1, padx = 10, pady = 10)
        
	
  
  
class Page3(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        path = r"ARP_GUI\\Network_Logs\\ARP_Traffic.log"
        with open(path, "r") as f:
            data = f.readlines()
        label = ttk.Label(self, text=data, font = ('Helvetica', 12))
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
        button1 = ttk.Button(self, text ="Network Information",
							command = lambda : controller.show_frame(Page1))
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
        button2 = ttk.Button(self, text ="Get MAC Address",
							command = lambda : controller.show_frame(Page2))
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
        button3 = ttk.Button(self, text ="Startpage",
							command = lambda : controller.show_frame(StartPage))
        button3.grid(row = 3, column = 1, padx = 10, pady = 10)


app = tkinterApp()

app.mainloop()

# Driver Code