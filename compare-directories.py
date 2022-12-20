import filecmp
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd


def select_directory_1():
    directory_name = fd.askdirectory()
    d1_text.set(directory_name)


def select_directory_2():
    directory_name = fd.askdirectory()
    d2_text.set(directory_name)


def compare_directories():
    result = filecmp.dircmp(d1_text.get(), d2_text.get())
    result.report()
    result_common.set(result.common.__str__())
    result_diff_files_list.set(result.diff_files.__str__())

    diff_result = result.diff_files

    for file in diff_result:
        file_opener1 = open(d1_text.get() + "/" + file, "r")
        file_opener2 = open(d2_text.get() + "/" + file, "r")

        file_reader1 = file_opener1.read()
        file_reader2 = file_opener2.read()

        # print("d1 " + file + ": " + file_opener1.read())
        # print("d2 " + file + ": " + file_opener2.read())

        d1_result_diff_files.set(file_reader1)
        d2_result_diff_files.set(file_reader2)

        file_opener1.close()
        file_opener2.close()

    # d1_result = result.left_list
    # d2_result = result.right_list


# establishes the main GUI window
window = tk.Tk()
window.geometry("500x300")
window.title("Comparyson")

# buttons to open directories
open_button1 = ttk.Button(
    window,
    text='Open Directory',
    command=select_directory_1
).grid(row=0, column=2)

open_button2 = ttk.Button(
    window,
    text='Open Directory',
    command=select_directory_2
).grid(row=1, column=2)

# to change label strings
d1_text = tk.StringVar()
d2_text = tk.StringVar()
result_common = tk.StringVar()
result_diff_files_list = tk.StringVar()
d1_result_diff_files = tk.StringVar()
d2_result_diff_files = tk.StringVar()

# labels for the entry boxes
tk.Label(window, text="Directory 1:").grid(row=0)
tk.Label(window, text="Directory 2:").grid(row=1)

# d1 = ""
# d2 = ""
d1 = tk.Label(window, textvariable=d1_text).grid(row=0, column=1)
d2 = tk.Label(window, textvariable=d2_text).grid(row=1, column=1)

# entry boxes
# d1 = tk.Entry(window).grid(row=0, column=1)
# d2 = tk.Entry(window).grid(row=1, column=1)
file_entry_array = []

# labels for the answer fields
tk.Label(window, text="Match:").grid(row=5)
tk.Label(window, text="Conflicting Files:").grid(row=6)
tk.Label(window, text="Diff Files:").grid(row=7)
tk.Label(window, text="Errors:").grid(row=8)

# button to call compare_directories()
tk.Button(window, text='Compare', command=compare_directories).grid(row=3,
                                                                    column=1,
                                                                    sticky=tk.W,
                                                                    pady=4)

# result labels
match_answer_label = tk.Label(window, textvariable=result_common).grid(row=5, column=1)
diff_answer_label = tk.Label(window, textvariable=result_diff_files_list).grid(row=6, column=1)

# file result labels
tk.Label(window, text="d1 file:").grid(row=9, column=0)
tk.Label(window, text="d2 file:").grid(row=9, column=1)
d1_diff_file_label = tk.Label(window, textvariable=d1_result_diff_files).grid(row=10, column=0)
d2_diff_file_label = tk.Label(window, textvariable=d2_result_diff_files).grid(row=10, column=1)

# create a notebook
# notebook = ttk.Notebook(window).grid(row=12, column=0)

# create frames
# frame1 = ttk.Frame(notebook, width=400, height=280).grid(row=13, column=0)
# frame2 = ttk.Frame(notebook, width=400, height=280).grid(row=13, column=1)

# frame1.pack(fill='both', expand=False)
# frame2.pack(fill='both', expand=False)

# add frames to notebook
# notebook.add(frame1, text='General Information')
# notebook.add(frame2, text='Profile')

window.mainloop()
tk.mainloop()

# D:/projects-coding/python/python-comparison/d1
# D:/projects-coding/python/python-comparison/d2

# TODO - Add directory-picker
# TODO - Add tabs or buttons to show each file comparison
# TODO - Get similarly named files that are identical and list them
# TODO - Compare line-by-line and -- show the differences on the GUI
# TODO - List subdirectories/ their files and compare those
# TODO - Add error handling
# TODO - Add limits to prevent memory leaks, crashes, etc.
