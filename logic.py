from tkinter import filedialog, messagebox
import gui

def openFile():
    filepath = filedialog.askopenfilename(filetypes=(("text files", "*.txt"),
                                                     ("all files", "*.*")))

    if filepath == "":
        return

    file = open(filepath, "r")
    filetext = file.read()
    file.close()

    gui.text.delete("1.0", "end")
    gui.text.insert("1.0", filetext)

def save():
    file = filedialog.asksaveasfile(defaultextension=".txt",
                                    filetypes=[("Text file", ".txt"),
                                               ("All files", ".*")])

    if file is None:
        return

    filetext = str(gui.text.get("1.0", "end"))
    file.write(filetext)
    file.close()

    gui.status.config(text="Saved!")

def newNote():
    answer = messagebox.askyesno(title="New Note",
                                 message="Clean the current note?")

    if answer == True:
        gui.text.delete("1.0", "end")

def exit():
    answer = messagebox.askyesno(title="Exit",
                                 message="Do you want to exit?")

    if answer == True:
        gui.window.destroy()
