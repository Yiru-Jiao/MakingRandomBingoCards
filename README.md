# Making random bingo cards
[LaTeX](http://tug.org/) and [python](http://www.python.org)-powered randomized bingo cards with custom cells. 
Takes a user-supplied list of phrases and randomly assigns them to a user-specified number of bingo cards, using LaTeX. 
This project is for a kind of indoor social event called "Human Bingo".

This is a forked version (with my adjustments) from https://github.com/jessehamner/BingoCards. As stated by the author of the original repo, the bulk of the code -- and all of the hard stuff -- 
was taken from [tex.stackexchange.com](http://tex.stackexchange.com/questions/63357/automatically-generated-bingo-cards).

## How to use
- __Step 1__: Clone/download the repo.
- __Step 2__: Prepare a csv file of Bingo questions. The file have to include more than 25 questions, and the questions should be concise and clear. In thie repo you can find an example file `BingoQuestions.csv`, which we used for TRAIL Congress 2024.
- __Step 3__: Run the script `extract_questions.py` to extract the questions from the csv file. The script will generate a file `to_copy_into_tex.txt` of usable format of the questions.
- __Step 4__: Copy the content of the file `to_copy_into_tex.txt` and paste it into the file `bingoquestions.tex` in the repo. The pasted content should be within `\myItems{}` as shown in the file.
- __Step 5__: Modify `bingocards.tex` to adjust the number of cards and the number of questions per card.
    - Number of grids: the default is 5x5, but you can change the number of rows and columns by modifying lines 31&32 `\def\NumOfColumns{5}` and `\def\Sequence{1, 2, 3, 4, 5}` into your desired number. 
    - Number of questions: then you may also want to also change the number of questions per card by modifying line 33 `\def\NumOfQuestions{25}`.
    - Number of cards: the default is 10 cards, but you can change the number of cards by modifying line 34 `\def\NumOfCards{10}`.
    - Title&Instructions: you can also modify the title and instructions of the bingo cards by modifying lines 86~108.
- __Step 6__: Compile the `bingocards.tex` file using a LaTeX compiler. A useful online compiler is [Overleaf](https://www.overleaf.com/), where you can zip the modified repo, upload the zip file, compile the `bingocards.tex` file, and download the generated pdf file.
