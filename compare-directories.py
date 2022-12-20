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
    # compares directories
    result = filecmp.dircmp(d1_text.get(), d2_text.get())
    # finds similarly-named files
    result_matching_name_list.set(result.common.__str__())
    # finds similarly-named files that have SAME contents
    result_identical_list.set(result.same_files.__str__())
    # finds similarly-named files that have DIFF contents
    result_conflicting_list.set(result.diff_files.__str__())
    # finds similarly-named directories
    # result_matching_directory_list.set(result.common_dirs.__str__())

    # ----- finds differing files -----
    result_1 = result.left_list
    result_2 = result.right_list
    diff_array_1 = []
    diff_array_2 = []

    for file in result_1:
        if file not in result_2:
            diff_array_1.append(file)

    result_diff_files_list_1.set(diff_array_1.__str__())

    for file in result_2:
        if file not in result_1:
            diff_array_2.append(file)

    result_diff_files_list_2.set(diff_array_2.__str__())

    conflicting_files = result.diff_files

# reads each conflicting file and displays the contents
    for file in conflicting_files:
        file_opener1 = open(d1_text.get() + "/" + file, "r")
        file_opener2 = open(d2_text.get() + "/" + file, "r")

        file_reader1 = file_opener1.read()
        file_reader2 = file_opener2.read()

        d1_result_diff_files.set(file_reader1)
        d2_result_diff_files.set(file_reader2)

        file_opener1.close()
        file_opener2.close()


# establishes the main GUI window
window = tk.Tk()
window.geometry("500x300")
window.title("Comparyson")

# StringVars
d1_text = tk.StringVar()
d2_text = tk.StringVar()
result_matching_name_list = tk.StringVar()
result_conflicting_list = tk.StringVar()
result_identical_list = tk.StringVar()
result_diff_files_list_1 = tk.StringVar()
result_diff_files_list_2 = tk.StringVar()
d1_result_diff_files = tk.StringVar()
d2_result_diff_files = tk.StringVar()

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

# labels for selected directories
tk.Label(window, text="Directory 1:").grid(row=0)
tk.Label(window, text="Directory 2:").grid(row=1)
d1 = tk.Label(window, textvariable=d1_text).grid(row=0, column=1)
d2 = tk.Label(window, textvariable=d2_text).grid(row=1, column=1)

# call compare_directories()
tk.Button(window, text='Compare', command=compare_directories).grid(row=3,
                                                                    column=1,
                                                                    sticky=tk.W,
                                                                    pady=4)

# labels for the result fields
tk.Label(window, text="Same file names:").grid(row=5)
tk.Label(window, text="Identical files:").grid(row=6)
tk.Label(window, text="Conflicting Files:").grid(row=7)
tk.Label(window, text="Different Files (d1):").grid(row=8)
tk.Label(window, text="Different Files (d2):").grid(row=9)
# tk.Label(window, text="Errors:").grid(row=10)

# result fields
match_answer_label = tk.Label(window, textvariable=result_matching_name_list).grid(row=5, column=1)
identical_answer_label = tk.Label(window, textvariable=result_identical_list).grid(row=6, column=1)
conflicting_files_label = tk.Label(window, textvariable=result_conflicting_list).grid(row=7, column=1)
diff_files_label_1 = tk.Label(window, textvariable=result_diff_files_list_1).grid(row=8, column=1)
diff_files_label_2 = tk.Label(window, textvariable=result_diff_files_list_2).grid(row=9, column=1)

# printed file labels
tk.Label(window, text="d1 file:").grid(row=10, column=0)
tk.Label(window, text="d2 file:").grid(row=10, column=1)
d1_diff_file_label = tk.Label(window, textvariable=d1_result_diff_files).grid(row=11, column=0)
d2_diff_file_label = tk.Label(window, textvariable=d2_result_diff_files).grid(row=11, column=1)

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

# TODO - Get different files and list them
# TODO - Add tabs or buttons to show each file comparison
# TODO - Compare line-by-line and -- show the differences on the GUI
# TODO - List subdirectories/ their files and compare those
# TODO - Add error handling
# TODO - Add limits to prevent memory leaks, crashes, etc.
# TODO - Prevent from being run multiple times?
