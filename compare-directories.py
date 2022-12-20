import filecmp
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import *


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

    # ---------- finds differing files ----------
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

    # --------------- new window with tabs to compare conflicting files -------------

    conflicting_files = result.diff_files

    new_window = Toplevel(window)
    new_window.title("Compare Conflicting Files")
    new_window.geometry("500x300")

    # create a notebook
    notebook = ttk.Notebook(new_window)
    notebook.pack(fill=BOTH, expand=1)

    # creates a new tab for each file
    for file in conflicting_files:
        file_opener1 = open(d1_text.get() + "/" + file, "r")
        file_opener2 = open(d2_text.get() + "/" + file, "r")

        file_reader1 = file_opener1.read()
        file_reader2 = file_opener2.read()

        d1_result_diff_files.set(file_reader1)
        d2_result_diff_files.set(file_reader2)

        new_frame = ttk.Frame(notebook, width=400, height=280)
        new_frame.pack(fill='both', expand=True)
        notebook.add(new_frame, text=file.__str__())

        frame_left = ttk.Frame(new_frame)
        frame_left.pack(side=LEFT, expand=True)
        frame_top_left = ttk.Frame(frame_left)
        frame_top_left.pack(side=TOP, expand=False)
        title1 = tk.Label(frame_top_left, text="Directory 1")
        title1.pack(side=TOP)
        frame_bottom_left = ttk.Frame(frame_left)
        frame_bottom_left.pack(side=BOTTOM, expand=True)
        file_data1 = tk.Label(frame_bottom_left, text=file_reader1)
        file_data1.pack()

        frame_right = ttk.Frame(new_frame)
        frame_right.pack(side=RIGHT, expand=True)
        frame_top_right = ttk.Frame(frame_right)
        frame_top_right.pack(side=TOP, expand=False)
        title2 = tk.Label(frame_top_right, text="Directory 2")
        title2.pack(side=TOP)
        frame_bottom_right = ttk.Frame(frame_right)
        frame_bottom_right.pack(side=BOTTOM, expand=True)
        file_data2 = tk.Label(frame_bottom_right, text=file_reader2)
        file_data2.pack()

        file_opener1.close()
        file_opener2.close()

        # scrollbar1 = Scrollbar(frame_bottom_left)
        # scrollbar1.pack(side=RIGHT, fill=Y)
        #
        # mylist = Listbox(new_frame, yscrollcommand=scrollbar1.set)
        # for line in range(100):
        #     mylist.insert(END, "This is line number " + str(line))
        #
        # mylist.pack(side=LEFT, fill=BOTH)
        # scrollbar1.config(command=mylist.yview)


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
# tk.Label(window, text="d1 file:").grid(row=10, column=0)
# tk.Label(window, text="d2 file:").grid(row=10, column=1)
# d1_diff_file_label = tk.Label(window, textvariable=d1_result_diff_files).grid(row=11, column=0)
# d2_diff_file_label = tk.Label(window, textvariable=d2_result_diff_files).grid(row=11, column=1)

window.mainloop()
tk.mainloop()

# D:/projects-coding/python/python-comparison/d1
# D:/projects-coding/python/python-comparison/d2

# TODO - Clean up tabs to make it look nicer
# TODO - Add links from each file to open up?
# TODO - Add red or green text to show differences
# TODO - Compare line-by-line and -- show the differences on the GUI
# TODO - List subdirectories/ their files and compare those
# TODO - Add error handling
# TODO - Add limits to prevent memory leaks, crashes, etc.
# TODO - Prevent from being run multiple times? -- It may be fixed
