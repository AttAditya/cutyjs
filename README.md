# [CutyJS](https://pypi.org/project/cutyjs/)

> CutyJS currently doesn't obey PEP 8 in many cases. It is a work in progress and may not be ready for production use. Use with caution and report any issues you encounter.

A lightweight JavaScript/TypeScript code formatter.

## Installation

`pip install cutyjs`

## About

CutyJS is a minimal and fast JavaScript/TypeScript formatter designed to enforce consistent formatting rules across JS/TS codebases.

Unlike large formatters that heavily restructure code, CutyJS focuses on deterministic formatting rules applied through a small rule engine. Each rule handles a specific formatting concern such as indentation, spacing, blank lines, or import ordering.

The formatter processes files using modular formatting rules, making the system easier to reason about, extend, and control.

## Features

- Deterministic JavaScript/TypeScript formatting
- Rule-based formatting system
- Import sorting
- Consistent indentation enforcement
- Blank line normalization
- Trailing space cleanup
- Line ending normalization
- Automatic EOF newline insertion
- Optional check mode for CI pipelines

## Usage

Format a file or directory:

`cutyjs path/to/file_or_directory`

Check if files need formatting (useful for CI or pre-commit):

`cutyjs --check path/to/project`

If formatting changes are required in check mode, CutyJS exits with a non-zero status code.

## Formatting Rules

CutyJS applies a set of focused formatting rules:

- Blank line normalization
- Declaration spacing adjustments
- Removal of excessive blank lines
- End-of-file newline enforcement
- Import ordering
- Indentation consistency
- Leading blank line cleanup
- Line ending normalization
- Trailing comma formatting
- Removal of trailing spaces

Each rule operates independently, allowing the formatter to remain simple and predictable.

## Project Structure

```tree
cutyjs
├── __init__.py
├── fmt.py
├── format_file.py
└── rules
    └── format
        ├── blank_lines.py
        ├── declaration_spacing.py
        ├── double_blanks.py
        ├── eof_newline.py
        ├── import_sort.py
        ├── indentation.py
        ├── leading_blank_lines.py
        ├── line_endings.py
        ├── trailing_commas.py
        └── trailing_spaces.py
```

- **fmt.py** provides the CLI entrypoint.
- **format_file.py** handles formatting of individual files.
- **rules/format** contains independent formatting rules applied sequentially.

## Design Philosophy

CutyJS is built around a few core ideas:

- Minimal implementation
- Explicit formatting rules
- Predictable output
- Easy extensibility
- Suitable for automation (CI / pre-commit)

Rather than trying to cover every stylistic decision, CutyPy focuses on enforcing a small set of reliable formatting guarantees.

## Status

Experimental and under active development.

## Links

- [PyPI](https://pypi.org/project/cutyjs/)
- [GitHub](https://github.com/AttAditya/cutyjs)

> Made by AttAditya