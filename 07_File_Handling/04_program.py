# A file contains a word "Donkey" multiple times. You need to write a program which replace this word with '#####' by updating the same file.

file = open('07_File_Handling/files/04_file.txt', 'r')

filedata = file.read()
print(filedata)

filedata = filedata.lower()

filedata = filedata.replace('donkey', "######")

file = open('07_File_Handling/files/04_file.txt', 'w')
file.write(filedata)
print(filedata)
