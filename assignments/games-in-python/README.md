# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a command-line Hangman game that uses string manipulation, loops, conditionals, user input, and random selection. The player should guess a hidden word one letter at a time before running out of attempts.

## 📝 Tasks

### 🛠️ Set Up the Hidden Word

#### Description

Create a predefined list of words and use Python's `random` module to select one word for each game. Prepare a display that shows the hidden word as underscores before the player begins guessing.

#### Requirements

Completed program should:

- Store at least five possible words in a list.
- Select one word randomly at the start of each game.
- Display one underscore for each letter in the selected word.
- Keep the selected word hidden from the player.

### 🛠️ Implement the Guessing Game

#### Description

Add a loop that accepts letter guesses, updates the word display, and tracks the player's remaining attempts. End the game when the player reveals the word or runs out of attempts.

#### Requirements

Completed program should:

- Accept one-letter guesses from the player.
- Reveal correctly guessed letters in their matching positions.
- Track incorrect guesses and display the number of attempts remaining.
- Prevent a guessed letter from being counted more than once.
- End with a win message when the player reveals the complete word.
- End with a lose message that reveals the word when no attempts remain.

For example, if the hidden word is `python` and the player has guessed `p` and `o`, the display should be similar to:

```text
p _ _ _ _ _
Incorrect guesses: o
Attempts remaining: 5
```
