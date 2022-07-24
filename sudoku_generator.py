# !/usr/bin/python
import sys
from Sudoku.Generator import *

# setting difficulties and their cutoffs for each solve method
difficulties = {
    'easy': (35, 0), 
    'medium': (81, 5), 
    'hard': (81, 10), 
    'extreme': (81, 15)
}

print('''\n\t\t\t\tSudoku Generator\n
      This Python script will generate Sudoku puzzles and their solutions then output
      said puzzles and solutions to a text file. The file name is the difficulty that you
      set at the start of the script with the txt file extention.
      ''')

# Get user to enter the number of puzzles to generate
numPuzzles = int(input('\tHow many puzzles do you want: '))

for n in range(numPuzzles):

    # getting desired difficulty from command line
    difficulty = difficulties[sys.argv[2]]
    
    if difficulty == (35, 0):
        dif = 'Easy'
    elif difficulty == (81, 5):
        dif = 'Medium'
    elif difficulty == (81, 10):
        dif = 'Hard'
    else:
        dif = 'Extreme'

    # constructing generator object from puzzle file (space delimited columns, line delimited rows)
    gen = Generator(sys.argv[1])

    # applying 100 random transformations to puzzle
    gen.randomize(100)

    # getting a copy before slots are removed
    initial = gen.board.copy()

    # applying logical reduction with corresponding difficulty cutoff
    gen.reduce_via_logical(difficulty[0])

    # catching zero case
    if difficulty[1] != 0:
        # applying random reduction with corresponding difficulty cutoff
        gen.reduce_via_random(difficulty[1])


    # getting copy after reductions are completed
    final = gen.board.copy()

    if n == 0:
        print(f'\n\tWriting Puzzle: {n + 1} to file: {dif}.txt')
    else:
        print(f'\tWriting Puzzle: {n + 1} to file: {dif}.txt')
    # # printing out board after reduction
    # print("The generated board after removals was: \r\n\r\n{0}".format(final))

    # # printing out complete board (solution)
    # print("The initial board before removals was: \r\n\r\n{0}".format(initial))

    # Save output to file
    with open(f'{dif}.txt', 'a') as f:
        if n + 1 != numPuzzles:
            f.write(f'\nPuzzle: {n + 1} Difficulty: {dif} \n' + str(final) + '\n\n' + str(initial) + '\n\n')
        else:
            f.write(f'\nPuzzle: {n + 1} Difficulty: {dif} \n' + str(final) + '\n\n' + str(initial) + '\n\n')
            print(f'\n\t{numPuzzles} puzzles were written\n')
            f.write('End of File')
