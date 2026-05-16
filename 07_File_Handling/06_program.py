# Write a program to mine a log file and find out whether it contains 'python'

file = open('07_File_Handling/files/06_file.txt', 'r')

filedata = file.read()

count_of_word = filedata.lower().count('python')

print(count_of_word)

print('python' in filedata.lower())