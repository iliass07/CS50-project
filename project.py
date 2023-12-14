import re
import csv
import sys
import os


def main():
    # file name input by user
    file_name = input("File name: ").lower().strip()

    if get_file(file_name) == False:
        sys.exit("The file extension is incorrect")

    if is_exist(file_name):
        print("File exist")
    else:
        sys.exit("File not found")





# This function verifies the input from user
def get_file(file_name):
    return True if re.search("^.+\.csv$", file_name) else False


# This function verifies the existence of the file in directory
def is_exist(file_name):
    return os.path.exists(file_name)




if __name__ == "__main__":
    main()
