
import os

BASE_PATH = "C:\\Users\\James\\test"

def directory_sorter(x):
    return x[11:17]

def main():
    dirs = os.listdir(BASE_PATH)
    dirs.sort(key=directory_sorter, reverse=True)
    for dir in dirs:
        path = os.path.join(BASE_PATH, dir, '\\amd64fre\\bin\\')
        if (os.path.exists(path)):
            print(dir)
            break

if __name__ == "__main__":
    main()


