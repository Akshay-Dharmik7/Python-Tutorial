# write a program to read the text from a given file 'poems.txt' and find out whether it contains the word 'twinkle'.

file = open('07_File_Handling/files/poems.txt', 'r')
#  or
# by default it will set to read mode 
# file = open('poems.txt')

file_data = file.read()

if 'twinkle' in file_data.lower():
    print(True)
else:
    print(False)