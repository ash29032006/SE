# Lab 4: Vibe Coding - Complete Chat History & Documentation

**Course:** Software Engineering (SE) Lab  
**Lab Assignment:** Lab 4 - VibeCoding  
**Repository Assigned:** [SETAPESU26/62_scramble](https://github.com/SETAPESU26/62_scramble)  
**Student Name:** Ashwin Harish  
**Repo:** [ash29032006/SE](https://github.com/ash29032006/SE)  

---

## 1. Objective & Overview
The objective of this lab is to use Vibe Coding / AI-assisted pair programming tools to:
1. Identify and fix deliberate bugs in the provided codebase under three to four prompt iterations.
2. Incrementally implement all the new features requested in the assignment specification.
3. Record gameplay footage demonstrating broken behavior before modifications and working functionality after modifications.
4. Document the full prompt engineering flow and code updates.

---

## 2. Problem Statement & Initial Analysis

### Repository Structure
```
62_scramble/
├── game/
│   ├── game_engine.py
│   └── text_box.py
├── main.py
├── README.md
└── Lab_4_VibeCoding_Student_handout.docx
```

### Initial Bug Discovered (Task 1)
In `game/game_engine.py` (lines 48–51 in original source):
```python
# BUG SYMPTOM: 
# Player's guess is validated against the scrambled text instead of the original solution.
is_correct = (guess == self.scrambled_word)
```
- **Observed Behavior:** When the user types the correct unscrambled word (e.g. typing `PLANET` for `A N L P T E`), the game incorrectly rejected it with:
  > `"WRONG GUESS! Try again."`
- **Root Cause:** The comparison was checking the player's guess against `self.scrambled_word` instead of `self.secret_word`.

---

## 3. Prompts & Step-by-Step Implementation

### Prompt 1: Implementation of Tasks 1 through 4
> **Prompt:**  
> *"go forward"*

- **Task 1: Bug Fix in `game_engine.py`**
  ```python
  # Fixed equality validation:
  is_correct = (guess == self.secret_word)
  ```

- **Task 2: Progressive Hint System**
  - Added a clickable `HINT` button adjacent to `SUBMIT`.
  - Added hint state `self.revealed_hints` revealing letters sequentially (`P _ _ _ _ _`).
  - Implemented 1-point score penalty per hint used.

- **Task 3: Round Countdown Timer (20 Seconds)**
  - Implemented a 20-second countdown timer.
  - Rendered a dynamic multi-colored progress bar transitioning from green to yellow to red.
  - On timeout: Displays `"TIME'S UP! The word was '...'"` and automatically transitions to `self.next_round()`.

- **Task 4: Interactive Letter Tiles Rack**
  - Replaced static text with graphical letter tiles inside a designated rearrangement rack.
  - Implemented both drag-and-drop and click-to-swap mechanics for intuitive anagram experimentation.

---

### Prompt 2: Word Pool Reference & Testing Assistance
> **Prompt:**  
> *"give me answers too"*

- Provided complete dictionary anagram lookup table:
  - `PYTHON`
  - `PYGAME`
  - `PLANET`
  - `ROCKET`
  - `GALAXY`
  - `STREAM`
  - `PUZZLE`
  - `ALGORITHM`

---

## 4. Final Verification
- Executed smoke tests on `GameEngine` logic:
  - Secret word validation: **PASSED**
  - Hint button and penalty logic: **PASSED**
  - Timer and rack initialization: **PASSED**
- Gameplay verified by running `python main.py` and capturing the 10-second "after" video.
