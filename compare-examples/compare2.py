import filecmp
  
d1 = "C:/Users/ttucker/Documents/random-code/python-comparison/d1"
d2 = "C:/Users/ttucker/Documents/random-code/python-comparison/d2"
files = ['txt1.txt']
  
# shallow comparison
match, mismatch, errors = filecmp.cmpfiles(d1, d2, files)
print('Shallow comparison')
print("Match:", match)
print("Mismatch:", mismatch)
print("Errors:", errors)
  
# deep comparison
match, mismatch, errors = filecmp.cmpfiles(d1, d2, files, shallow=False)
print('Deep comparison')
print("Match:", match)
print("Mismatch:", mismatch)
print("Errors:", errors)