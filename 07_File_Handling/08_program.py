# 8. Write a program to make a copy of a text file "this. txt".

file1 = open('07_File_Handling/files/08_this.txt', 'r')

file2 = open('07_File_Handling/files/08_this2.txt', 'w')

file1data = file1.read()

file2.write(file1data)