from tkinter import Tk, PhotoImage, Menu, Label, Text, Frame, Button
import logic

window = Tk()

icon = PhotoImage(file="images/window-icon.png")
window.iconphoto(True, icon)

window.geometry("600x550")
window.minsize(600, 550)
window.title("Mini Notes")
window.config(bg="#1e1e2e")

menubar = Menu(window)
window.config(menu=menubar)
fileMenu = Menu(menubar, tearoff=0)

def openNote():
    filetext = logic.openFile()

    if filetext is None:
        return

    text.delete("1.0", "end")
    text.insert("1.0", filetext)

def saveNote():
    status.config(text="")

    filetext = text.get("1.0", "end")
    saved = logic.save(filetext)

    if saved:
        status.config(text="Saved!")

def createNote():
    answer = logic.newNote()

    if answer:
        text.delete("1.0", "end")

def exitApp():
    answer = logic.exit()

    if answer:
        window.destroy()

menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=openNote)
fileMenu.add_command(label="Save", command=saveNote)
fileMenu.add_command(label="New", command=createNote)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=exitApp)

title = Label(window,
              text="MINI NOTES",
              font=("Arial", 25, "bold"),
              fg="#ffffff",
              bg="#1e1e2e",
              padx=20,
              pady=20)

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

buttonFrame = Frame(window, bg="#1e1e2e")
buttonFrame.pack()

openButton = Button(buttonFrame,
                    text="Open",
                    font=("Arial", 15, "bold"),
                    fg="#ffffff",
                    bg="#89b4fa",
                    activebackground="#74a7ff",
                    activeforeground="#ffffff",
                    padx=15,
                    pady=5,
                    command=openNote)

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
                    command=saveNote)

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
                    command=createNote)

newButton.pack(side="left", padx=5)

status = Label(window,
               text="",
               font=("Arial", 12),
               fg="#a6e3a1",
               bg="#1e1e2e")

status.pack()
