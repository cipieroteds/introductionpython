***🎮 Project: Python Games***

This project contains two simple games developed in Python: Hangman and Guessing Game. The user can choose which game to play through an interactive menu.

**📌 Features**

Game selection menu: Allows the player to choose between the available games.
Hangman Game: The player must guess a secret word before reaching the maximum number of errors.
Guessing Game: The player tries to guess a secret number within a limited number of attempts.
**📂 Project Structure**

The project contains the following files:

entrada-jogos.py: Main file that displays the menu and allows game selection.
forca.py: Implementation of the Hangman Game.
jogo_adivinhacao.py: Implementation of the Guessing Game.

**🕹️ How to Play**

Run the entrada-jogos.py file:

![img1](https://github.com/cipieroteds/introductionpython/blob/main/image.JPG)

Choose the desired game by entering 1 for Hangman or 2 for Guessing Game.

**🎯 Hangman Game**

The game randomly selects a secret word from a predefined list.
The player must guess the word by entering one letter at a time.
The game ends when the player completes the word or reaches 6 errors.

**🔢 Guessing Game**

The player must guess a secret number between 1 and 100.
Three difficulty levels determine the number of attempts:
Easy: 8 attempts
Medium: 6 attempts
Hard: 3 attempts
The game informs whether the guessed number is higher or lower than the secret number.
The score decreases based on the difference between the guess and the secret number.

**🚀 Technologies Used**

Python 3
Random library for generating random numbers and words.

**📜 License**

This project is free to use for study and modifications.
