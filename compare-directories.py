import filecmp
import tkinter as tk


def compare_directories():
    # deep comparison
    file_entry_array.append(file_entry.get())
    print("compare_directories() called ")
    match, mismatch, errors = filecmp.cmpfiles(d1.get(), d2.get(), file_entry_array, shallow=False)
    print('Deep comparison')
    print("Match:", match)
    print("Mismatch:", mismatch)
    print("Errors:", errors)

    for file in mismatch:
        file_opener1 = open(d1.get() + "/" + file, "r")
        file_opener2 = open(d2.get() + "/" + file, "r")
        
        print("d1: " + file_opener1.read())
        print("d2: " + file_opener2.read())
        file_opener1.close()
        file_opener2.close()


window = tk.Tk()

tk.Label(window, text="Directory 1:").grid(row=0)
tk.Label(window, text="Directory 2:").grid(row=1)
tk.Label(window, text="File:").grid(row=2)

d1 = tk.Entry(window)
d2 = tk.Entry(window)
file_entry = tk.Entry(window)
file_entry_array = []

d1.grid(row=0, column=1)
d2.grid(row=1, column=1)
file_entry.grid(row=2, column=1)

# files = ['web.config']

# d1 = "C:/SDx Server Files/WebClient_Sites/SDxClipWC"
# d2 = "C:/SDx Server Files/WebClient_Sites/SDxTuckWC"

tk.Button(window, text='Compare', command=compare_directories).grid(row=3,
                                                                    column=1,
                                                                    sticky=tk.W,
                                                                    pady=4)

window.mainloop()

tk.mainloop()

# D:/projects-coding/python/python-comparison/d1
# D:/projects-coding/python/python-comparison/d2
