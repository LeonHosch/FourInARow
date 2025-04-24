# CHANGELOG

The file collects the changelog in anti chronological listing.
First section lists untagged achievements.
Next sections are ordered by tags used in the repository.

## Untagged Achievements

- SuperLinter (not just Linting, add Code Formatters) as a GitHub Action
  - Pylint, Black, Flake8, Ruff, Linting MD, toml, json, YAML, jscpd, ...
  - include SuperLinter as a badge in readme reflecting the current status
- run tests and coverage analysis as a GitHub Action
  - Code Coverage badge and Test badge in readme reflecting the current status

## package_dependency_management_swa_debug_test

(2025-04-15, d40c0ce4c9e5ab97f72e98f27e0168c4bda74570)

- Remove initial set of PyLint warnings (linting warnings)
- create AUTHORS, LICENSE, CHANGELOG, README.md
- pip requirements.txt (to point to pdm with standard Python tools)
- pdm (package and dependency management, configuration management of Python packages)
  - for all other Python packages than PDM itself
- introduce unittest, Pytest
  - sample set up in Visual Studio Code
- coverage analysis (line coverage, branch coverage, function coverage, module coverage)
- Dependabot (Vulnerability alerts, invalid / insecure tooling, baseline configuration checking)
- application debugging (prefer debugpy over deprecated python debugger)
  - [Visual Studio Code](https://code.visualstudio.com/docs/python/debugging)
  - launch.json : "type": "debugpy" instead "type": "python"
- SW Architecture
  - module splitting
    - move generator (legal moves)
    - separate player or engine interface
    - game history (iterate through history to replay)

## linter_as_github_action

(2025-04-03, 1c2c00c111367bdeafd9506a1510e01b1de8dfa1)

- initial commit (Four in a Row running in console version for one human player and random AI player)
- First GitHub Action on community runner (Pylint as a build step to include in a development tool chain)
