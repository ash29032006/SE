# Lab 4: Vibe Coding — Word Scramble Repair (`62_scramble`)

## Student Details
- **Name:** Ashwin Harish (Ashwin C H)
- **SRN:** PES1UG24AM900
- **Assigned Base Repository:** `SETAPESU26/62_scramble`

---

## Objective
Use AI-assisted pair programming (Vibe Coding) to diagnose and fix a deliberate validation bug in an existing Pygame Word Scramble game and implement three new interactive features within iterative prompts, documented with before/after gameplay recordings and the complete prompt/chat history.

---

## Folder Structure

```text
lab4/
├── README.md
├── 62_scramble/                       # Updated Pygame application
│   ├── .gitignore
│   ├── README.md                      # Game & implementation documentation
│   ├── main.py                        # Entry point
│   └── game/
│       ├── __init__.py
│       ├── game_engine.py             # GameEngine (bug fix, hints, timer, interactive tiles)
│       └── text_box.py                # TextBox input widget
├── docs/
│   ├── Lab_4_VibeCoding_Student_handout.docx
│   ├── chat_history.docx              # Exported LLM chat history (DOCX)
│   └── chat_history.md                # Markdown copy of chat history
└── videos/
    ├── before_change.mov              # 10s gameplay showing original bug
    └── After_change.mov               # 10s gameplay showing bug fix + new features
```

---

## Summary of Changes Implemented
1. **Task 1 — Guess Validation Bug Fix (`game/game_engine.py`):**
   - Fixed `submit_guess()` to validate `guess == self.secret_word` instead of `guess == self.scrambled_word`.
2. **Task 2 — Progressive Hint System:**
   - Added a clickable `HINT` button next to `SUBMIT` that sequentially reveals letters of `self.secret_word` with a 1-point score penalty.
3. **Task 3 — 20-Second Round Countdown Timer:**
   - Added a color-coded countdown bar (`green` -> `yellow` -> `red`). On expiration, displays `"TIME'S UP!"`, reveals the secret word, and advances to the next round.
4. **Task 4 — Interactive Letter Tiles Rack:**
   - Rendered scrambled letters as graphical square tiles supporting both drag-and-drop and click-to-swap rearrangement.

---

## Running the Game

```bash
pip install pygame
cd lab4/62_scramble
python main.py
```

---

## Deliverables Checklist
- [x] Before-change gameplay recording (`videos/before_change.mov`)
- [x] After-change gameplay recording (`videos/After_change.mov`)
- [x] Fixed and enhanced source code (`62_scramble/`)
- [x] Complete LLM chat history (`docs/chat_history.docx` & `docs/chat_history.md`)
