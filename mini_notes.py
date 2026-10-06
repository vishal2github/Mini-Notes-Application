from tkinter import Tk, Label, Text, Button, Frame, Menu, PhotoImage, messagebox
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(filetypes=(("text files", "*.txt"),
                                                     ("all files", "*.*")))

    if filepath == "":
        return

    file = open(filepath, "r")
    filetext = file.read()
    file.close()

    text.delete("1.0", "end")
    text.insert("1.0", filetext)

def save():
    file = filedialog.asksaveasfile(defaultextension=".txt",
                                    filetypes=[("Text file", ".txt"),
                                               ("All files", ".*")
                                               ])
    if file is None:
        return

    filetext = str(text.get("1.0", "end"))
    file.write(filetext)
    file.close()

    status.config(text="Saved!")

def newNote():
    answer = messagebox.askyesno(title="New Note",
                                 message="Clear the current note?")

    if answer == True:
        text.delete("1.0", "end")

def exit():
    answer = messagebox.askyesno(title="Exit",
                                 message="Do you want to exit?")

    if answer == True:
        window.destroy()

window = Tk()

icon = PhotoImage(file="images/window-icon.png")
window.iconphoto(True, icon)

# window.geometry("600x550")
window.minsize(600, 550)
window.title("Mini Notes")
window.config(bg="#1e1e2e")

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=save)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=exit)

title = Label(window,
              text="MINI NOTES",
              font=("Arial", 25, "bold"),
              fg="#ffffff",
              bg="#1e1e2e",
              padx=20,
              pady=20
              )

title.pack()

text = Text(window,
            bg="#313244",
            fg="#ffffff",
            font=("Arial", 15),
            height=15,
            width=45,
            padx=15,
            pady=15,
            relief="sunken",
            bd=5)

text.pack()

buttonFrame = Frame(window,
                    bg="#1e1e2e")

buttonFrame.pack()

status = Label(window,
               text="",
               font=("Arial", 12),
               fg="#a6e3a1",
               bg="#1e1e2e")

status.pack()

openButton = Button(buttonFrame,
                    text="Open",
                    font=("Arial", 15, "bold"),
                    fg="#ffffff",
                    bg="#89b4fa",
                    activebackground="#74a7ff",
                    activeforeground="#ffffff",
                    padx=15,
                    pady=5,
                    command=openFile)

openButton.pack(side="left", padx=5)

saveButton = Button(buttonFrame,
                    text="Save",
                    font=("Arial", 15, "bold"),
                    fg="#ffffff",
                    bg="#a6e3a1",
                    activebackground="#8bd48a",
                    activeforeground="#ffffff",
                    padx=15,
                    pady=5,
                    command=save)

saveButton.pack(side="left", padx=5)

newButton = Button(buttonFrame,
                     text="New",
                     font=("Arial", 15, "bold"),
                     fg="#ffffff",
                     bg="#f38ba8",
                     activebackground="#eb7892",
                     activeforeground="#ffffff",
                     padx=15,
                     pady=5,
                     command=newNote)

newButton.pack(side="left", padx=5)

window.mainloop()
