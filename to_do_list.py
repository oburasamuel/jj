from tkinter import *
from tkinter import ttk

class todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To-Do-List')
        self.root.geometry('650*410+300+150')

        self.label = Label(self.root, text = 'To-Do-List-App', font = 'ariel, 25 bold', width=10, bd=5, bg='blue', fg='white')
        self.label.pack(side='top', fill=BOTH)

        self.label2 = Label(self.root, text = 'Add Task', font = 'ariel, 18 bold', width=10, bd=5, bg='blue', fg='white')
        self.label.place(x=40, y=54)

        self.label3 = Label(self.root, text = 'Tasks', font = 'ariel, 18 bold', width=10, bd=5, bg='blue', fg='white')
        self.label.place(x=320, y=54)

        self.main_text = Listbox(self.root, height=9, bd=5, width=23, font="ariel, 20 italic bold")
        self.main_text.place(x=280, y=100)

        self.text = Text(self.root, bd=5, height=2, width=30, font='ariel, 10 bold')
        self.text.place(x=29, y=120)


        def add():
            content = self.text.get(1.0, END)
            self.main_text.insert(END, content)
            with open('data.txt', 'a') as f:
                f.write(content)
                f.seek(0)
                f.close()
            self.text.delete(1.0, END)

        
        def delete():
            delete = self.main_text
    
    
def main():
    root = Tk()
    ul = todo(root)
    root.mainloop()


if __name__ == "__main__":
    main()