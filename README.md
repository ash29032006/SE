# Software Engineering (SE) — Coursework & Lab Repository

## Student Details
- **Name:** Ashwin C H (Ashwin Harish)
- **SRN:** PES1UG24AM900
- **Course:** Software Engineering (Semester 5)

---

## Overview

This repository consolidates multiple Software Engineering course assignments and labs, including:
1. **ML Regression Notebook & GitHub Actions CI/CD Pipeline** (`ml_cicd/`)
2. **ISA 2 — Python Calculator Module, PyUnit & Pylint CI** (`isa2/`)
3. **Lab 4 — Vibe Coding: Word Scramble Repair** (`lab4/`)

---

## Repository Structure

```text
.
├── .github/
│   └── workflows/
│       └── ci-cd.yml                  # CI/CD pipeline (lint, unit tests, notebook build, Pages deploy)
├── .gitignore
├── README.md
├── requirements.txt                   # Dependencies for the ML notebook CI workflow
├── ml_cicd/
│   ├── README.md                      # Regression notebook & CI/CD documentation
│   └── notebook085d1cc1d4.ipynb       # Linear & polynomial regression notebook
├── isa2/
│   ├── .pylintrc                      # Pylint configuration for ISA2
│   ├── README.md                      # Calculator module & test documentation
│   ├── x.py                           # Arithmetic & factorial module
│   └── test_x.py                      # PyUnit test suite (18 tests)
└── lab4/
    ├── README.md                      # Lab 4 overview & deliverables index
    ├── 62_scramble/                   # Updated Word Scramble Pygame application
    │   ├── .gitignore
    │   ├── README.md
    │   ├── main.py
    │   └── game/
    │       ├── __init__.py
    │       ├── game_engine.py
    │       └── text_box.py
    ├── docs/
    │   ├── Lab_4_VibeCoding_Student_handout.docx
    │   ├── chat_history.docx
    │   └── chat_history.md
    └── videos/
        ├── before_change.mov
        └── After_change.mov
```

---

## Modules & Quick Start

### 1. ML Regression Notebook & CI/CD (`ml_cicd/`)
Automated via [`.github/workflows/ci-cd.yml`](.github/workflows/ci-cd.yml):
- Lints the converted notebook script with `pylint`.
- Executes `ml_cicd/notebook085d1cc1d4.ipynb` using `jupyter nbconvert` and publishes an HTML report to GitHub Pages.

```bash
pip install -r requirements.txt
jupyter nbconvert --to notebook --execute ml_cicd/notebook085d1cc1d4.ipynb --output executed_notebook.ipynb --output-dir=.
```

### 2. ISA 2 — Calculator Module (`isa2/`)
Implements `add`, `subtract`, `multiply`, `divide`, and `factorial` with input validation, covered by 18 `unittest` test cases and `pylint`.

```bash
python -m unittest discover -s isa2 -p "test_*.py" -v
pylint isa2/x.py --rcfile=isa2/.pylintrc
```

### 3. Lab 4 — Vibe Coding: Word Scramble Arena (`lab4/`)
Fixes the guess validation bug (`self.secret_word` comparison) and implements a progressive hint system, 20-second countdown timer bar, and interactive drag-and-drop / click-to-swap letter tile rack.

```bash
pip install pygame
cd lab4/62_scramble
python main.py
```

See [`lab4/README.md`](lab4/README.md) for the complete deliverables breakdown, chat history, and gameplay recordings.
