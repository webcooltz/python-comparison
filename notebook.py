import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo


def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )


# root window
root = tk.Tk()
root.geometry('400x300')
root.title('File Compare')

open_button = ttk.Button(
    root,
    text='Open a File',
    command=select_file
)

open_button.pack(expand=True)

# create a notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# list of files
file_list = ["test1", "test2"]

# creates a new tab for each file
for file in file_list:
    new_frame = ttk.Frame(notebook, width=400, height=280)
    new_frame.pack(fill='both', expand=True)
    notebook.add(new_frame, text=file.__str__())

root.mainloop()
