from tkinter import *
from tkinter import ttk

class todo:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title('To-Do-List')
        self.root.geometry('650*410+300+150')

        self.label = Label(self.root, text = 'To-Do-List-App', font = 'ariel, 25 bold', width=10, bd=5, bg='blue', fg='white')
        self.label.pack(side='top', fill=BOTH)

        self.label2 = Label(self.root, text = 'Add Task', font = 'ariel, 18 bold', width=10, bd=5, bg='blue', fg='white')
        self.label.place(x=40, y=34)

    
    
def main():
    root = Tk()
    ul = todo(root)
    root.mainloop()


if __name__ == "__main__":
    main()