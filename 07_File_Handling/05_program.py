# Repeat program 4 for a list of such words to be censored.

file = open('07_File_Handling/files/05_file.txt', 'w')

for  i in range(2, 21):
    file.write(f'----------- Table of {i} ----------\n')

    for j in range (1, 11):
        data = f'i * j = {i*j} \n'
        file.write(data)

    file.write('---------------------------------------\n')
