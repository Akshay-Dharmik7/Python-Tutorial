# 7. Write a program to find out the line number where python is present..

file = open('07_File_Handling/files/07_file.txt', 'r')

countline = 0

while True:
    filedata = file.readline()
    if 'python' in filedata.lower():
        countline += 1
        print(countline)  
    else:
        countline += 1
