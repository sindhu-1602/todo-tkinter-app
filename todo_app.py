import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task")

app = tk.Tk()
app.title("Todo List")

task_entry = tk.Entry(app, width=30)
task_entry.pack(pady=10)

add_button = tk.Button(app, text="Add Task", command=add_task)
add_button.pack(pady=5)

listbox = tk.Listbox(app, width=50)
listbox.pack(pady=10)

app.mainloop()