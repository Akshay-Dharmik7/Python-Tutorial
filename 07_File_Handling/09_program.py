# 9. Write a program to find out whether a file is identical & matches the content of another file.

file1 = open('07_File_Handling/files/09_file1.txt', 'r')
file2 = open('07_File_Handling/files/09_file2.txt', 'r')

file1data = file1.read()
file2data = file2.read()

print(file1data == file2data)


