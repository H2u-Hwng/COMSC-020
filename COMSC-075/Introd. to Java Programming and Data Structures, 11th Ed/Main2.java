from tkinter import ttk
from tkinter import messagebox
from tkinter import Tk

public class Main2 {




	root = Tk()

	root.geometry("400x400")
	#^ width - heghit window :D


	cmb = ttk.Combobox(root, width="10", values=("prova","ciao","come","stai"))
	#cmb = Combobox

	class TableDropDown(ttk.Combobox):
	    def __init__(self, parent):
	        self.current_table = tk.StringVar() # create variable for table
	        ttk.Combobox.__init__(self, parent)#  init widget
	        self.config(textvariable = self.current_table, state = "readonly", values = ["Customers", "Pets", "Invoices", "Prices"])
	        self.current(0) # index of values for current table
	        self.place(x = 50, y = 50, anchor = "w") # place drop down box 

	def checkcmbo():

	    if cmb.get() == "prova":
}
