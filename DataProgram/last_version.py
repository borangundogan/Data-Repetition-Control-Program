import tkinter as tk
from tkinter import filedialog, Text
import os
import pandas as pd
import pyautogui

def background():
    canvas = tk.Canvas(tk_w, height=700, width=700, bg="#263D42")
    canvas.pack()
    frame = tk.Frame(tk_w, bg="white")
    frame.place(relwidth=0.8, relheight=0.8,relx=0.1, rely=0.1)

def buttons():
    '''Create Browse Button'''
    browse_file = tk.Button(tk_w,text="Browse", font="Verdana 12 bold",
                        padx=10, pady=5,fg= "white",bg="#263D42",command=browse)
    browse_file.pack()

    write_save= tk.Button(tk_w,text="Write&Save Data", font="Verdana 12 bold",
                        padx=10, pady=5,fg= "white",bg="#263D42",command=write_file)
    write_save.pack()
    
    write_save= tk.Button(tk_w,text="Read Data", font="Verdana 12 bold",
                        padx=10, pady=5,fg= "white",bg="#263D42",command=read_all_data)
    write_save.pack()
    
    print_dupblicates_data = tk.Button(tk_w,text="Compare Excel File", font="Verdana 11 bold",
                    padx=10, pady=5,fg= "white", bg="#263D42",command= data_print)
    print_dupblicates_data.pack()
    
    show_file = tk.Button(tk_w,text="Show", font="Verdana 11 bold",
                    padx=10, pady=5,fg= "white", bg="#263D42",command= show)
    show_file.pack()
    
def browse():
    filepath = filedialog.askopenfilename(initialdir="/", 
                                            title="Open File",
                                            filetypes=(("|*.xlsx files", "*.xlsx") , ("|*.xls files " , "*.xls"), ("|*.csv files " , "*.csv")))
    '''Importing data from excel to .py'''
    df = pd.read_excel(filepath)
    global listofdf
    '''Returning from dataframe to List '''
    listofdf = list(df["ID"])
    pyautogui.alert("Your file has been received. Please press the Write&Save Data button to save.")

def write_file():
    '''Open file and dynamic memory'''
    with open("DataFile.txt", "a") as file:
        for element in listofdf:
            file.writelines(str(element) + "\n" )

def compare_each_value(x):
    _size = len(x)
    repeat = []
    for i in range(_size):
        k =  i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeat:
                repeat.append(x[i])
    return ("Duplicated: "+ str(repeat))

def compare_all_data(x):
    if (len(x) == len(set(x))):
        return False
    else:
        return True
    
def read_all_data():
    global lines
    if os.path.isfile("DataFile.txt"):
        mainfile = open("DataFile.txt")
        lines = mainfile.readlines()
        lines = [line.strip() for line in lines]
    return lines

def data_print():
    pyautogui.alert(compare_each_value(lines))
    print(compare_each_value(lines))
    
def show():
    result1 = compare_all_data(listofdf)
    result2 = compare_all_data(lines)
    if (result1 or result2):
        pyautogui.alert(text="List contains duplicates!!")
        print('Yes, list contains duplicates')
    else:
        pyautogui.alert(text="No duplicates found in list!!")
        print('No duplicates found in list')
        
if __name__ == "__main__":
    global tk_w
    tk_w = tk.Tk()
    buttons()
    tk.mainloop()
