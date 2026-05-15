# Write a program to generate multiplication tables from 2 to 20 and write it to the different files.

for i in range(2, 21):
    file = open(f'07_File_Handling/files/tableof{i}.txt', 'w')

    for j in range(1, 11):
        filedata = f'{i} * {j} = {i*j}'

        file.write(f'{filedata} \n')