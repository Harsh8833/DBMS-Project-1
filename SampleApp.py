import tkinter as tk
from tkinter import ttk
import MenuPage
import ctypes
import NewShopping
import BestCustomer
import FindCustomer
import Invoice_history
import ProdUpdate

'''
Here We are Creating a App that connects all pages.
Logic ------> Create all pages and store them in a bucket then raise the frame on call.(similar to Staking, i use this as this makes the transition b/w pages fast.)
Function used to call page is show_frame use this on every page to change page.

IMPORTANT: Import module of new page and then add class of the frame on for loop.

we write all pages class in for loop so that we can create all pages when our Sample App Class is initiated.
'''


class SampleApp(tk.Tk):
	ctypes.windll.shcore.SetProcessDpiAwareness(1)
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		container = tk.Frame(self)
		container.pack(side="top", fill="both" ,expand=True)
		container.grid_rowconfigure(0, weight =1)
		container.grid_columnconfigure(0, weight=1)

		
		
		self.frames = {}

		#Add newly added pages here in for loop
		for F in (ProdUpdate.prod_update,Invoice_history.invoice_history,FindCustomer.find_customer,BestCustomer.best_customer_page,NewShopping.New_shopping_page,MenuPage.MenuPage):
			page_name = F.__name__
			frame = F(parent=container, controller=self)
			self.frames[page_name] = frame
			frame.grid(row=0, column=0, sticky="nsew")
		self.show_frame("MenuPage")# Add the page Name which you want to show when the app start's.
	def show_frame(self, page_name):
		frame = self.frames[page_name]
		frame.tkraise()  

		
if __name__ == "__main__":
    app = SampleApp() #Calling the App class
    app.mainloop() #helding the main class in loop to keep our ui responsive
