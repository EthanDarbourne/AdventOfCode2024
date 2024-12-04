import os


day = -1
dirname = os.path.dirname(__file__) + '\\'
for i in range(1, 26):
    newpath = dirname + f'Day{i}' 
    if not os.path.exists(newpath):
        day = i
        break
if day == -1:
    exit()

os.makedirs(newpath)

for i in range(1, 3):
    f = open(newpath + f"\day{day}-part{i}.py", 'w')
    f.close()

f = open(newpath + "\input.txt", 'w')
f.close()
