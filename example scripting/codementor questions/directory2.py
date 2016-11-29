import os
def print_files(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            print(file)
        for dir in dirs:
            print(dir)



test =print_files("C:\\Users\\jongguk\\PycharmProjects\\Python-for-Trading\\example scripting")
