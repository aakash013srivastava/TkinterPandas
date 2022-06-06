from tkinter import *
from tkinter import filedialog as fd
import pandas as pd
import numpy as np
import os

main = Tk()

ftype = Label(main, text = "Select CSV File ").place(x = 30,y = 50)  


def select_file():
    filetypes = (
            ('CSV files', '*.csv'),
            # ('Excel files', '*.xlsx')
        )
    
    file = fd.askopenfilename(title='Open a file',
            initialdir='/home/dell/Desktop/Jupyter/datasets',
            filetypes=filetypes)

    filepath =  os.path.abspath(file)

    return (filepath)

b = Button(main,text = "Open",command=select_file).place(x=200,y=50)


df = pd.read_csv(select_file())



horizontal = 60
for col in df.columns:
    lbl = Label(main, text = col).place(x = horizontal,y = 130)
    horizontal+=125

# Create listbox with list of column names
listb = Listbox(main, selectmode = "multiple")
listb.place(x=160,y=160)

# Listbox to display selected fields
listbDisplay = Listbox(main)
listbDisplay.place(x=800,y=160)

#  function to get selected columns/items of listbox 
def list_select_func():
    selection = listb.curselection()
    
    if selection:
        selected_list = [listb.get(i) for i in listb.curselection()]
        lbl2 = Label(main,text=selected_list).place(x=600,y=160)
        for j in selected_list:
            for i in range(0,len(df.sample(5))):
                listbDisplay.insert(END,df[j][i])
                print(df[j][i])

                
        print(len(df))


list_select = Button(main,text="Select",command=list_select_func)
list_select.place(x=500,y=160)
select = Label(main, text = "Select").place(x = 60,y = 160)      

for each_item in range(len(df.columns)):
    
    listb.insert(END, df.columns[each_item])
    
    # Check if listbox is selected




headers = Label(main, text = "Headers").place(x = 60,y = 100)  
 

main.mainloop()