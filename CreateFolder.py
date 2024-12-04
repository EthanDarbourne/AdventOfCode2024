import os

day = 3

dirname = os.path.dirname(__file__) + '\\'
newpath = dirname + f'Day{day}' 
if not os.path.exists(newpath):
    os.makedirs(newpath)

for i in range(1, 3):
    f = open(newpath + f"\day{day}-part{i}.py", 'w')
    f.close()

f = open(newpath + "\input.txt", 'w')
f.close()
