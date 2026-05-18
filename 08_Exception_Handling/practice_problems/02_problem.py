# 2. File Reader Safeguard
# Task: Prompt the user for a filename, attempt to open it, and print its contents.  
# Exception to handle: FileNotFoundError.  
# Goal: If the file doesn't exist, catch the error gracefully and print a helpful message instead of a stack trace.

try:
    file = open('08_Exception_Handling/02_file.txt', 'r')

    file.read()

except FileNotFoundError:
    print('attempt to read file which is not present in path shared!')