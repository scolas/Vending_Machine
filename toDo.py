import tkinter
import random


root = tkinter.Tk()
#main window

#background color
root.configure(bg="blue")

#title
root.title("To Do List")

# size
root.geometry("400x400")



# data list
task = []

task = ["home work", "pick up dry cleaning", "project", "add new funtion"]


def upd_box():
    clear_box()
    for t in task:
        lbl_task.insert("end", t)



def clear_box():
    lbl_task.delete(0, "end")





def add_method():
    text1 = txtInput.get()
    if text1 !="":
        task.append(text1)
        upd_box()
    else:
        lblDisplay["text"] = "Enter a task please"
    txtInput.delete(0,"end")



def del_all_method():
    global task
    task = []

    #task.clear()
    #update box
    upd_box()



def del_task():
    task1 = lbl_task.get("active")
    if task1 in task:
        task.remove(task1)
    upd_box()



def sort():
    task.sort()
    upd_box()




def number_task():
    #number of task
    number_of_task = len(task)
    msg = "Number of task: %s" %number_of_task
    lblDisplay["text"] = msg

    pass

def desc():
    task.sort()
    #revers
    task.reverse()
    upd_box()


def choose():
    #choos radom task
    tasks = random.choice(task)
    lblDisplay["text"]=tasks



def exit():
    pass




#

lbltitle = tkinter.Label(root, text="To Do", bg="white")
lbltitle.grid(row=0,column=0)


lblDisplay = tkinter.Label(root, text="", bg="white")
lblDisplay.grid(row=1,column=1)


txtInput = tkinter.Entry(root, width=25)
txtInput.grid(row=2,column=1)


btnAdd = tkinter.Button(root, text="add ", fg="blue" , bg="white", command=add_method )
btnAdd.grid(row=1,column=0)


btndel = tkinter.Button(root, text="Delete all", fg="blue" , bg="white", command=del_all_method )
btndel.grid(row=2,column=0)


btndel_one = tkinter.Button(root, text="Delete task", fg="blue" , bg="white", command=del_task )
btndel_one.grid(row=3,column=0)


btnsort = tkinter.Button(root, text="sort", fg="blue" , bg="white", command=sort )
btnsort.grid(row=4,column=0)

btnsort_desc = tkinter.Button(root, text="sort descending ", fg="blue" , bg="white", command=desc)
btnsort_desc.grid(row=5,column=0)


btnchoos_rand = tkinter.Button(root, text="Choose Random ", fg="blue" , bg="white", command=choose )
btnchoos_rand.grid(row=6,column=0)


btn_number_task = tkinter.Button(root, text="task number ", fg="blue" , bg="white", command=number_task )
btn_number_task.grid(row=7,column=0)


btnquit = tkinter.Button(root, text="EXIT", fg="blue" , bg="white", command=exit )
btnquit.grid(row=8,column=0)



lbl_task = tkinter.Listbox(root)
lbl_task.grid(row=3,column=1)





root.mainloop()




