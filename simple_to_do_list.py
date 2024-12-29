from tkinter import *
from tkinter.ttk import *
import random

def add_task():
    pass

def rem_task():
    pass

def view_task():
    pass

def mark_task():
    pass

"""MAIN CODE LOGIC"""
def main():
    tasks=[]
    while True:
        print("TO-DO-LIST")
        print("a . Add Task")
        print("b . Remove Task")
        print("c . View Tasks")
        print("d . Mark as Done")
        print("e . Exit")

        choice = input("Enter the choice:")

        if choice == "a":
            print()
            n_tasks=int(input("How many tasks you want to add ?"))
            for i in range(n_tasks):
                task=input("Enter the task:")
                task.append({"task":task , "done":False})
                print("Task Added")

        elif choice=="b":
            print("Tasks:")
            for index , task in enumerate(tasks):
                status = "Done" if task["done"] else "Not done"
                print(f"{index + 1}. {task['task']}-{status}")

        elif choice=="c":
            task_index=int(input("Enter the task no. to mark as done:")) -1
            if 0<=task_index < len(tasks):
                tasks[task_index]["done"]=True
                print("Task Marked as done")
            else:
                print("Invalid Task Number")

        elif choice=="d":
            print("Exiting the To-Do List")
            break

        else:
            print("Invalid choice . Try again !")


"""GUI BASED COMMANDS GOES HERE"""
root = Tkinter.Tk()
lbl_title = Tkinter.Label(root, text="To-Do-List" , bg="black")
lbl_title.pack()

lbl_disp = Tkinter.Label(root, text="" , bg="black")
lbl_disp.pack()

txt_input = Tkinter.Entry(root,width=15)
txt_input.pack()

btn_add_task = Tkinter.Button(root, text="Add Task", fg ="green" , bg="black" , command = add_task)
btn_add_task.pack()

btn_rem_task = Tkinter.Button(root, text="Remove Task", fg ="green" , bg="black" , command = rem_task)
btn_rem_task.pack()

btn_view_task = Tkinter.Button(root, text="View Task", fg ="green" , bg="black" , command = view_task)
btn_view_task.pack()

btn_mark_task = Tkinter.Button(root, text="Mark as done ", fg ="green" , bg="black" , command = mark_task)
btn_mark_task.pack()

btn_exit = Tkinter.Button(root, text="Exit", fg ="green" , bg="black" , command = exit)
btn_exit.pack()

lb_tasks = Tkinter.Listbox(root)
lb_tasks.pack()


root.mainloop()