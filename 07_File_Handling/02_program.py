# The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file 'Hi-score.txt' which is either blank or contains the previous Hi-score. You need to write a program to update the Hi- score whenever the game() function breaks the Hi-score.


def game():
    file = open('07_File_Handling/files/Hi-score.txt', 'r+')

    filedata = file.read()

    hi_score = 100

    if len(filedata) ==  0:
        file.write(f'Hi-Score: {hi_score}')
        file.close()
    else:
        for value in filedata:
            if value.isdigit():
                pos = filedata.index(value)
                # if int(filedata[pos:len(filedata) + 1]) < hi_score:
                if int(filedata[pos:]) < hi_score:
                    file = open('07_File_Handling/files/Hi-score.txt', 'w')
                    file.write(f'Hi-Score: {hi_score}')
                
                return

    file.close()

game()
