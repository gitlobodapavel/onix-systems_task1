import os.path

def create_file(filename):
    list = open(filename, "w")
    list.close()

def check_file_empty(filename):
    if os.stat(filename).st_size == 0:
        print("[ log ]: The file "+ filename +" is empty !")
        read_file(filename)
    else:
        read_file(filename)

def check_file(filename):
    if os.path.exists(filename):
        check_file_empty(filename)
    else:
        print("[ log ]: Creating file: "+ filename)
        create_file(filename)
        check_file_empty(filename)

def read_file(filename):
    file = open(filename, "r")
    current_line = file.readline()
    while current_line:
        print(current_line)
        current_line = file.readline()
    file.close()

def main():
    filename = "shopping_list.txt"
    check_file(filename)

main()