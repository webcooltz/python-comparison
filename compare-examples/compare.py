import filecmp

file1 = open("C:/Users/ttucker/Documents/random-code/python-comparison/txt1.txt", "r")
file2 = open("C:/Users/ttucker/Documents/random-code/python-comparison/txt2.txt", "r")

i = 0

for line1 in file1:
    i += 1

    for line2 in file2:

        if line1 == line2:
            print("Line ", i, ": IDENTICAL")
        else:
            print("Line ", i, ":")
            print("\tFile1: ", line1, end='')
            print("\tFile 2: ", line2, end='')
        break

file1.close()
file2.close()

# result = filecmp.cmp(file1, file2, shallow=False)

# print(result)