"""
This module contains function to operate on files with some additional features.
"""
from pathlib import Path
import os

def read(source_folder, file_name, number_of_lines = None ):
    """
    This function made to read or display a whole file content or specific lines of it.
    :param source_folder: The path of the text file location folder.
    :param file_name: The name of the file with extension (name.txt)
    :param number_of_lines: This is a number of lines you'll read, and these will be the firs in file.
    :return: None.
    """
    path = Path(source_folder) / file_name
    file = open(path, "r")

    if type(number_of_lines) is int:
        counter = 0
        for l in file:
            counter+=1
        file.seek(0)
        if number_of_lines > counter:
            print("The number you entered more than actual number of lines")
        else:
            for n in range(number_of_lines):
                print(file.readline().rstrip(), end="\n")
            file.close()
    else:
        # read file content
         print(file.read(), end="\n")
         file.close()


def read_by_kb(source_folder, file_name, kilo_bytes):
    """
    Read a segment of kiloBytes from file.
    :param source_folder: The path of file location folder
    :param file_name: file name with extension (ex: file.text)
    :param kilo_bytes: The number of kilo bytes the user requires.
    :return: None.
    """
    path = Path(source_folder) / file_name
    size = os.path.getsize(path)
    Bytes = kilo_bytes * 1024
    if size >= Bytes:
        file = open(path, "r")
        print(file.read(Bytes), end="\n")
    else:
        print("The size you entered is greater than file size !", end='')

# Reading binary files
def read_binary(source_folder, file_name):
    """
    Use this function to read a whole binary file.
    :param source_folder: The path of file location folder
    :param file_name: file name with extension (ex:file.pdf)
    :return: None.
    """
    path = Path(source_folder) / file_name
    file = open(path, "rb")
    print(file.read(), end="\n")


def list_directory(directory):
    """
    Using this function to list sub-directories.
    :param directory: Directory path.
    :return: None
    """
    entries = os.scandir(directory)
    for entry in entries:
        print(entry)


def write(source_folder, file_name, text, mode):
    """
    Use this function to write in your text files
    :param source_folder: String of location folder path.
    :param file_name: String of file name with extension (file.txt).
    :param text: String of text you would write.
    :param mode: This is how to write in files. For more: https://www.tutorialspoint.com/python3/python_files_io.htm.
    :return: None.
    """
    path = Path(source_folder) / file_name
    file = open(path, mode= mode)
    file.write(text)


if __name__ == '__main__':
    list_directory("D:\IT")
    
