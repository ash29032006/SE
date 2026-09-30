# Word Scramble Repair Lab

This project is an interactive anagram deduction word puzzle game using **Pygame**. It introduces students to string permutation, randomized list shuffling, uppercase letter sanitization, and text-box widget integration within an object-oriented codebase.
---

## What's Provided

A working Word Scramble game with:

- A built-in dictionary pool of words chosen at random each round
- A scrambling algorithm that randomizes letter order while ensuring the scrambled version differs from the original word
- A custom `TextBox` input component handling alphabetic keystrokes, automatic uppercase conversion, and backspace
- Interactive guess submission via the `Return` / `Enter` key or clicking the `SUBMIT` button
- Real-time score tracking, spaced letter displays, and color-coded status messaging

This repository contains the **completed** fixes and implemented features for the bug and three feature tasks described below.
---

## Getting Started

### Setup

1. Make sure you have Python 3.10+ installed.
2. Install dependencies:

```bash
pip install pygame
```

3. Run the game:

```bash
python main.py
```

**Controls:** Type letters into the text box and press Return (or click SUBMIT) to submit your unscrambled word


## Tasks to Complete

Each task must be completed using an iterative process involving LLM suggestions and your critical code review.

### Task 1: Fix the guess comparison validation bug

When the player figures out the correct unscrambled word and types it into the text box, the game rejects it with a "WRONG GUESS! Try again." error. In game_engine.submit_guess(), the validation line checks is_correct = (guess == self.scrambled_word) instead of comparing the guess to self.secret_word. This erroneously forces the player to re-type the jumbled letters rather than unscrambling the word. Fix the equality check so guess is validated against self.secret_word.

### Task 2: Implement a hint system with letter reveals

Some long words can be challenging to unscramble. Add a clickable HINT button beside SUBMIT. When clicked, reveal the first unrevealed letter of self.secret_word in its correct position (e.g., displaying P _ _ _ _ _ for PYTHON), while deducting a small point penalty from self.score.
 
### Task 3: Implement a round countdown timer

Currently, players have unlimited time to ponder each word. Add an active countdown timer bar (e.g., 20 seconds) in game_engine.render(). If the timer expires before a correct guess is entered, reveal the correct secret word, display a "TIME'S UP!" warning, and transition automatically to self.next_round().

### Task 4: Implement letter tile drag-and-drop or clickable letter sorting

Instead of reading scrambled letters as a static text string, render each scrambled letter inside its own graphical square tile. Allow players to click or drag tiles into a rearrangement rack to experiment with different anagram configurations before submitting.
---

## Expected Behavior

- At the start of each round, a word is chosen and displayed with its letters jumbled.
- Typing the correctly unscrambled word into the input box awards 1 point, displays a success message, and advances to a new word.
- Typing an incorrect word displays a warning message and clears the input box for retry without advancing the round.
- Empty submissions trigger a prompt without penalty.
---

## Folder Structure

```text
62_scramble/
├── .gitignore
├── game/
│   ├── __init__.py
│   ├── game_engine.py
│   └── text_box.py
├── main.py
└── README.md
```

## Submission Checklist

- [x] A 10-second video of gameplay **before** changes (`../videos/before_change.mov`)
- [x] A 10-second video of gameplay **after** changes (`../videos/After_change.mov`)
- [x] Complete Chat/LLM history (`../docs/chat_history.docx`, `../docs/chat_history.md`)
