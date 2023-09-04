from tkinter import *
from tkinter import messagebox

def newTask():
    task = my_entry.get()
    priority = priority_var.get()
    
    if task.strip() != "":
        lb.insert(END, f"[{priority}] {task}")
        my_entry.delete(0, "end")
        priority_var.set("Priority")
    else:
        messagebox.showwarning("Warning", "Please enter a task to perform.")

def deleteTask():
    selected_task = lb.curselection()
    if selected_task:
        lb.delete(selected_task)

ws = Tk()
ws.geometry('600x600+400+150')
ws.title('Personalized To-Do List')
ws.config(bg='#121212')
ws.resizable(width=False, height=False)

frame = Frame(ws, bg='#121212')
frame.pack(pady=20)

lb = Listbox(
    frame,
    width=45,
    height=10,
    font=('Arial', 14),
    bd=0,
    fg='#4ecca3',
    selectbackground='#ffb703',
    activestyle="none",
    bg='#212121'
)
lb.pack(side=LEFT, fill=BOTH)

task_list = []

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=Y)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    ws,
    font=('Arial', 18),
    bg='#212121',
    fg='#4ecca3',
    insertbackground='#4ecca3'
)
my_entry.pack(pady=20)
my_entry.insert(0, "")

priority_var = StringVar()
priority_var.set("Priority")
priority_menu = OptionMenu(
    ws,
    priority_var,
    "High", "Medium", "Low"
)
priority_menu.config(
    font=('Arial', 12),
    bg='#212121',
    fg='#4ecca3',
    activebackground='#212121',
    activeforeground='#4ecca3',
    highlightthickness=0
)
priority_menu.pack(pady=10)

button_frame = Frame(ws, bg='#121212')
button_frame.pack()

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('Arial', 12, 'bold'),
    bg='#4ecca3',
    fg='white',
    padx=15,
    pady=8,
    activebackground='#35a384',
    command=newTask
)
addTask_btn.pack(side=LEFT, padx=10)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('Arial', 12, 'bold'),
    bg='#ff6b6b',
    fg='white',
    padx=15,
    pady=8,
    activebackground='#d44b4b',
    command=deleteTask
)
delTask_btn.pack(side=LEFT, padx=10)

developer_label = Label(
    ws,
    text="Developed with  by Aayush Dushane",
    font=('Arial', 10),
    fg='#4ecca3',
    bg='#121212'
)
developer_label.pack(pady=(20, 0))

ws.mainloop()
