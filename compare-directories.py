import filecmp
import tkinter as tk


def compare_directories():
    result = filecmp.dircmp(d1.get(), d2.get())
    result.report()
    result_common.set(result.common.__str__())
    result_diff_files_list.set(result.diff_files.__str__())

    diff_result = result.diff_files

    # print("d1: " + result.left_list.__str__())
    # print("d2: " + result.right_list.__str__())
    # print("common: " + result.common.__str__())
    # print("diff_files: " + result.common.__str__())

    for file in diff_result:
        file_opener1 = open(d1.get() + "/" + file, "r")
        file_opener2 = open(d2.get() + "/" + file, "r")

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


window = tk.Tk()
window.geometry("500x300")
window.title("Comparyson")

# to change label strings
result_common = tk.StringVar()
result_diff_files_list = tk.StringVar()
d1_result_diff_files = tk.StringVar()
d2_result_diff_files = tk.StringVar()

# labels for the entry boxes
tk.Label(window, text="Directory 1:").grid(row=0)
tk.Label(window, text="Directory 2:").grid(row=1)
# tk.Label(window, text="File:").grid(row=2)

d1 = tk.Entry(window)
d2 = tk.Entry(window)
# file_entry = tk.Entry(window)
file_entry_array = []

d1.grid(row=0, column=1)
d2.grid(row=1, column=1)
# file_entry.grid(row=2, column=1)

# labels for the answer fields
tk.Label(window, text="Match:").grid(row=5)
tk.Label(window, text="Conflicting Files:").grid(row=6)
tk.Label(window, text="Diff Files:").grid(row=7)
tk.Label(window, text="Errors:").grid(row=8)

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

window.mainloop()

tk.mainloop()

# D:/projects-coding/python/python-comparison/d1
# D:/projects-coding/python/python-comparison/d2

# TODO - Add tabs to show each file's contents side-by-side with the other directory
# TODO - Get similarly named files that are the same and list them
# TODO - Compare line-by-line and show the differences on the GUI