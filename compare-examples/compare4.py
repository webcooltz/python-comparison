from difflib import Differ

with open("txt1.txt") as file_1, open("txt2.txt") as file_2:
    differ = Differ()

    for line in differ.compare(file_1.readlines(), file_2.readlines()):
        print(line)