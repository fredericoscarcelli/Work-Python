
# from tkinter import *
# from tkinter import messagebox
# from tkinter import colorchooser
# from tkinter import filedialog
# from tkinter.ttk import *

# #widgets = GUI elements
# #windows = serves as a container to hold or contain these widgets
# #label = an area widget that holds text and/or an image

# def defineBgColor():
#     color = colorchooser.askcolor()
# #    print(color)
#     colorhex = color[1]
#     window.config(bg=colorhex)

# def click():
#     new_window = Toplevel() #Toplevel() = new window 'on top' of other windows. linked
#                             #Tk() = new independent window
#     #input = text.get(1.0,END)
#     #print('test button')
#     #capture = entry.get()
#     #print(capture)
#     #entry.delete(0,END)

# def openFile():
#     filePath = filedialog.askopenfilename(initialdir="C:/Users/scarcelli.fosm/Desktop/")
#     file = open(filePath,'r')
#     print(file.read())
#     file.close()

# def saveFile():
#     file = filedialog.asksaveasfile(initialdir="C:/Users/scarcelli.fosm/Desktop/",
#                                     defaultextension=".txt",
#                                     filetypes=[
#                                         ("Text File",".txt"),
#                                         ("HTML File",".html"),
#                                         ("All Files",".*")
#                                     ])
#     fileText = str(text.get(1.0,END))
#     file.write(fileText)
#     file.close()

# def display():
#     if(x.get()==1):
#         print("you agree")
#     else:
#         print("you don't agree")

# window = Tk() #instantiate an instance of a window
# window.geometry("800x600")
# window.title("Controle Financeiro - Scar")
# icon = PhotoImage(file="C:/Users/scarcelli.fosm/Documents/Logo Image.png")

# window.iconphoto(True,icon)
# window.config(background="Black") #Hex color also


# notebook = ttk.Notebook(window) #widget that manages a collection of windows/displays
# tabHome = Frame(notebook) #new frame for tabHome
# tabExpense = Frame(notebook)
# tabRevenue = Frame(notebook)
# tabReports = Frame(notebook)
# tabQuit = Frame(notebook)

# notebook.add(tabHome,text="Home")
# notebook.add(tabExpense,text="Expenses")
# notebook.add(tabRevenue,text="Revenues")
# notebook.add(tabReports,text="Reports")
# notebook.add(tabQuit,text="Exit")


# notebook.pack(expand=TRUE, fill=BOTH)

# grid() = geometry manager that organizes widgets in a table
# firstNameLabel = Label(tabQuit, text="First name").grid(row=0,column=0)
# firstNameEntry = Entry(tabQuit).grid(row=0,column=1)

# LastNameLabel = Label(tabQuit, text="Last name").grid(row=1,column=0)
# lastNameEntry = Entry(tabQuit).grid(row=1,column=1)

# emailLabel = Label(tabQuit, text="Email").grid(row=2,column=0)
# firstNameEntry = Entry(tabQuit).grid(row=2,column=1)

# Bar

# bar = Progressbar(window, orient=HORIZONTAL,length=300)


# menuBar = Menu(window)

# HomeMenu = Menu(menuBar)
# menuBar.add_cascade(label="Home")

# expenseMenu = Menu(menuBar,tearoff=0)
# menuBar.add_cascade(label="Expense", menu=expenseMenu)
# expenseMenu.add_command(label="Add Expense",command=click)
# expenseMenu.add_separator()
# expenseMenu.add_command(label="Delete Expense")

# revenueMenu = Menu(menuBar,tearoff=0)
# menuBar.add_cascade(label="Revenue", menu=revenueMenu)
# revenueMenu.add_command(label="Add Revenue")
# revenueMenu.add_separator()
# revenueMenu.add_command(label="Delete Revenue")

# ReportsMenu = Menu(menuBar)
# menuBar.add_cascade(label="Reports")
# ExitMenu = Menu(menuBar)
# menuBar.add_cascade(label="Exit",command=quit)


# window.config(background="Black", menu=menuBar) #Hex color also

# labelHome = Label(tabHome,
#             text="Controle Financeiro",
#             font=("Comic Sans", 30, "bold"),
#             fg="black",
#             bg="#337591",
#             relief=RAISED,
#             bd=10,
#             padx=20,
#             pady=20,
#             image=(icon),
#             compound='left').pack()

# labelExpenses = Label(tabExpense,
#             text="Controle Financeiro",
#             font=("Comic Sans", 30, "bold"),
#             fg="black",
#             bg="#337591",
#             relief=RAISED,
#             bd=10,
#             padx=20,
#             pady=20
#             ).pack()


# button = Button(tabQuit,
#                 text="Submit",
#                 command=click,
#                 font=("Comic Sans", 10),
#                 fg = "black",
# #                 bg = "#337591",
# #                 state=ACTIVE).grid(row=3, column=1)

# buttonBgColor = Button(window,
#                 text="Define Bg Color",
#                 command=click,
#                 font=("Comic Sans", 12, "bold"),
#                 fg = "black",
#                 bg = "#337591",
#                 state=ACTIVE)

# buttonOpenFile = Button(window,
#                 text="Open File",
#                 command=openFile,
#                 font=("Comic Sans", 12, "bold"),
#                 fg = "black",
#                 bg = "#337591",
#                 state=ACTIVE)

# buttonSaveFile = Button(window,
#                 text="Save File",
#                 command=saveFile,
#                 font=("Comic Sans", 12, "bold"),
#                 fg = "black",
#                 bg = "#337591",
#                 state=ACTIVE)
# entry = Entry(window,
#             font=("Comic Sans", 12),
#             fg = "Black")


# text = Text(window,
#             bg="light yellow",
#             font=("Ink Free",23),
#             height=8,
#             width=20,
#             padx=20,
#             pady=20,
#             fg="Purple")

# text = Text(window)

# text.pack()
# button.pack()
# buttonOpenFile.pack()
# buttonSaveFile.pack()
# x=IntVar()

# check_button = Checkbutton(window,
#                           text="I agree with something",
#                           variable=x,
#                           onvalue=1,
#                           offvalue=0,
#                           command=display)

# check_button.pack()

# food = ["pizza","hamburger","hotdog"]
# x=IntVar()

# for index in range(len(food)):
#    radioButton = Radiobutton(window,
#                            text=food[index], #add text to radio buttons
#                            variable=x,       #groups radiobutton together if they share the sam variable
#                            value=index,      #assigns each radiobutton diferentes values
#                            padx=25,
#                            font=("Comic Sans", 30, "bold"),
#                            indicator=0)     #eliminate the cricles
#    radioButton.pack()

# def submit():
#     foodList=[]

#     for index in listbox.curselection():
#         foodList.insert(index,listbox.get(index))

#     for index in food:
#         print(index)


#     print (listbox.get(listbox.curselection()))
# if(listbox.get(listbox.curselection())):
#    print('I want'+ listbox.getvar())
# else:
#    print("Please,choose the options")
# def addItem():
#         #messagebox.showwarning(title="Warning", message='Item added with ressalvas')
#     if messagebox.askokcancel(title="Confirm",message="Confirm the operation"):
#         listbox.insert(listbox.size()+1,entry.get())
#         listbox.config(height=listbox.size())
#         messagebox.showinfo(title="Sucess", message='Item add with success')
#         messagebox.askyesno(title="Error", message='Something went wrong')
#     else:
#         messagebox.showerror(title="Error", message='Something went wrong')

#     entry.delete(0,END)

# def deleteItem():
#     listbox.delete(listbox.curselection())
#     listbox.config(height=listbox.size())

# listbox = Listbox(window,selectmode=MULTIPLE)

# listbox.insert(1,"pizza")
# listbox.insert(2,"salad")
# listbox.insert(3,"hamburger")
# listbox.insert(4,"icecream")

# listbox.config(height=listbox.size())

# buttonList = Button(window,
#                     command=submit,
#                     text='Submit')

# entryNewItem = Entry(window)

# buttonAdd = Button(window,text="Add", command=addItem)

# buttonDelete = Button(window,text="Delete", command=deleteItem)

# listbox.pack()
# entry.pack()
# buttonList.pack()
# buttonAdd.pack()
# buttonDelete.pack()

# labelTitle.pack()
# labelInformtions.pack()
# entry.pack(side=LEFT)
# button.pack()


# window.mainloop() #place window on computer screen, listen for events


from tkinter import *
from tkinter.ttk import *
import time


def start():
    tasks = 10
    x = 0
    while (x < tasks):
        time.sleep(1)
        bar['value'] += 10
        x += 1
        percent.set(str(int((x/tasks)*100))+"%")
        window.update_idletasks()


window = Tk()

percent = StringVar()

window.geometry("800x600")

bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack(pady=10)

percentLabel = Label(window, textvariable=percent).pack()

button = Button(window, text="Download", command=start).pack()

window.mainloop()
