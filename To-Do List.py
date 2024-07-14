import tkinter as tk
from tkinter import messagebox

def on_entry_click(event):
    if entry_task.get() == "Enter task here...":
        entry_task.delete(0, tk.END)
        entry_task.insert(0, '')
        entry_task.config(fg='blue')

def on_focus_out(event):
    if entry_task.get() == '':
        entry_task.insert(0, 'Enter task here...')
        entry_task.config(fg='blue')

def add_task(event=None):
    task = entry_task.get().strip()
    if task and task != "Enter task here...":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def delete_all_tasks():
    confirm = messagebox.askyesno("Delete All Tasks", "Are you sure you want to delete all tasks?")
    if confirm:
        listbox_tasks.delete(0, tk.END)

def save_task():
    with open("tasks.txt", "w") as f:
        for i in range(listbox_tasks.size()):
            task = listbox_tasks.get(i)
            bg_color = listbox_tasks.itemcget(i, "background")
            f.write(f"{task},{bg_color}\n")

def update_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        task = entry_task.get()
        if task != "" and task != "Enter task here...":
            listbox_tasks.delete(task_index)
            listbox_tasks.insert(task_index, task)
            entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update.")

def mark_complete():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.itemconfig(task_index, {'bg': 'pink'})
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as complete.")

def exit_application():
    confirm = messagebox.askyesno("Exit Application", "Do you want to exit the application?")
    if confirm:
        window.destroy()

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            for line in f:
                data = line.strip().split(",")
                task = data[0]
                bg_color = data[1] if len(data) > 1 else ''
                listbox_tasks.insert(tk.END, task)
                if bg_color == 'green':
                    listbox_tasks.itemconfig(tk.END, {'bg': bg_color})
    except FileNotFoundError:
        pass

window = tk.Tk()
window.title("To-Do List")
window.configure(bg="cyan")
window.geometry('550x320')

entry_task = tk.Entry(window, width=35, bg="lightyellow", fg="blue",font=('Arial',12))
entry_task.pack(side=tk.TOP, pady=10)
entry_task.insert(0, 'Enter task here...')
entry_task.bind('<FocusIn>', on_entry_click)
entry_task.bind('<FocusOut>', on_focus_out)
entry_task.bind("<Return>", add_task)

listbox_tasks = tk.Listbox(window, height=5, width=100, bg="lightpink",font=('Arial',12))
listbox_tasks.pack(side=tk.LEFT, expand=True,fill=tk.BOTH,padx=5,pady=5)

scrollbar_tasks = tk.Scrollbar(listbox_tasks, orient=tk.VERTICAL)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

button_add_task = tk.Button(window, text="Add Task", width=10, command=add_task,bg='violet',font=('Arial',12))
button_add_task.pack(pady=5)

button_delete_task = tk.Button(window, text="Delete Task", width=10, command=delete_task,bg='red',font=('Arial',12))
button_delete_task.pack(pady=5)

button_delete_all_tasks = tk.Button(window, text="Delete All Tasks", width=15, command=delete_all_tasks,bg='yellow',font=('Arial',12))
button_delete_all_tasks.pack(pady=5)

button_update_task = tk.Button(window, text="Update Task", width=10, command=update_task,bg='lightblue',font=('Arial',12))
button_update_task.pack(pady=5)

button_mark_complete = tk.Button(window, text="Mark Complete", width=12, command=mark_complete,bg='lightgreen',font=('Arial',12))
button_mark_complete.pack(pady=5)


button_save = tk.Button(window, text="Save", width=10, command=save_task,bg='white',font=('Arial',12))
button_save.pack(side=tk.LEFT, padx=5, pady=5)

button_exit = tk.Button(window, text="Close",width=10, command=exit_application,bg='white',font=('Arial',12))
button_exit.pack(side=tk.RIGHT, padx=5, pady=5)

load_tasks()

window.mainloop()