# About
This project is a fork of https://github.com/RutledgePaulV/sudoku-generator but was limited to one puzzle and solution at a time and I needed multiple puzzles.

# Changes Made
- Added an introductory text
- Added prompt for user input to set number of puzzles to generate
- Added for loop to loop to generate the specified number of puzzles
- Added notification of writing the puzzle to the output file
- Commented out the original output
- Write puzzles to file with Puzzle number and difficulty
- Writes the unsolved puzzle first then the solution
- Writes End of File upon completion

# TODO
I know the formating of the console output is not very good looking at the moment but I wanted to get the text away from the left edge of the screen. Eventually I will surround the text in a box thusly:

************
**  Text  **
************

# Need TODO
The process is slow as hell need to make it faster some how maybe using the stack or using gpu to speed things up.