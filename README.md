# Four in a Row

This is an implementation of a Four in a Row game.

[![Super-Linter](https://github.com/LeonHosch/FourInARow/actions/workflows/super-linter.yml/badge.svg)](https://github.com/marketplace/actions/super-linter)
[![Pylint](https://github.com/LeonHosch/FourInARow/actions/workflows/pylint.yml/badge.svg)](https://github.com/LeonHosch/FourInARow/actions/workflows/pylint.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![pdm-managed](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fpdm-project%2F.github%2Fbadge.json)](https://pdm-project.org)

## Rules

* Players take turns dropping own pieces into columns of a vertical grid.
* The goal is to connect four or more own pieces in a row—horizontally, vertically, or diagonally.
* Thus the first player to achieve this wins the game.
* If the grid is filled without a winner, the game ends in a draw.

## Setup / Usage

Assumed you have Python 3 installed you can issue the following commands.

Prepare your environment and install site packages.

```bat
python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pdm update
```

Run the unit tests only.

```bat
pdm run pytest -v history.py test\test_history.py
```

Run the unit tests and show line coverage.

```bat
pdm run pytest -v --cov=. history.py test\test_history.py
```

Actually play the game.

```bat
pdm run four_in_a_row.py
```
