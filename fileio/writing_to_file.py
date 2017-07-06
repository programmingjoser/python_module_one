
'''
open(filename, mode="r")opens a file. More info in the docs.

file.write("hello world") would write "hello world" to whatever file the file variable points at.

file.close() closes the pointer to the file file.

The two most common modes or flags for writing are "w", for truncating and then writing,
and "a" for appending to the file.

The context manager pattern for dealing with files is:

with open("my_file.txt", "a") as file:
    file.write("Hello world")




open(filename, mode="r")opens a file. More info in the docs.

file.read(bytes=-1) would read the entire contents of the file. You can control the number of bytes read by passing in an integer. Relatedly, file.seek() will move the read/write pointer to another part of the file.

file.readlines() reads the entire file into a list, with each line as a list item.

The context manager pattern for dealing with files is:

with open("my_file.txt", "r") as file:
    file.read(10)

For more about sys.argv, check out the docs.

'''

import sys

def remember(thing):
    # built-in with is a context manager
    with open("my_file.txt", "a") as file:
        file.write(thing+"\n")

def show():
    with open("my_file.txt") as file:
        print(file.read(3))
        file.seek(0) # to reset pointer
        lines = file.readlines()
        print(len(lines))
        # names backward
        for line in lines:
            print(line[::-1])

        file.seek(0)
        for line in file:
            print(line)



if __name__ == '__main__':
    if sys.argv[1].lower() == '--list':
        show()
    else:
        remember(' '.join(sys.argv[1:]))
