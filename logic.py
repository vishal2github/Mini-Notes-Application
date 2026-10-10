from tkinter import filedialog, messagebox

def openFile():
    filepath = filedialog.askopenfilename(filetypes=(("text files", "*.txt"),
                                                     ("all files", "*.*")))

    if filepath == "":
        return

    file = open(filepath, "r")
    filetext = file.read()
    file.close()

    return filetext

def save(filetext):
    file = filedialog.asksaveasfile(defaultextension=".txt",
                                    filetypes=[("Text file", ".txt"),
                                               ("All files", ".*")])

    if file is None:
        return

    file.write(filetext)
    file.close()

    return True

def newNote():
    answer = messagebox.askyesno(title="New Note",
                                 message="Clean the current note?")

    if answer == True:
        return True
    
    return False

def exit():
    answer = messagebox.askyesno(title="Exit",
                                 message="Do you want to exit?")

    if answer:
        return True
    
    return False
