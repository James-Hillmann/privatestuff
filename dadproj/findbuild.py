
import os
path = "C:\\Users\\James\\test"
dirs = os.listdir(path)
def func(x):
    return x[11:17]
dirs.sort(key = func,reverse=True)
for file in dirs:
    path = 'C:\\Users\\James\\test\\' + file + '\\amd64fre\\bin\\'
    isExist = os.path.exists(path)
    if(isExist):
        print(file)
        break
        

