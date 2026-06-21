# Text Utility API

A small Flask-based REST API that performs basic text operations: palindrome
checking, word/character counting, and string reversal. Built as a practice
project for the **IBM/Coursera course "Developing AI Applications with Python
and Flask"**, specifically the module on application development and
packaging using Python — covering Flask, static code analysis, unit testing,
and packaging.

## What this project demonstrates

- **Flask** — a small REST API with multiple POST routes, JSON request/response handling, and basic input validation
- **Static code analysis** — code linted with `pylint`, including a deliberate, documented exception for one rule in the test file
- **Unit testing** — a full `unittest` suite covering normal cases and edge cases (empty strings, extra whitespace, single characters)
- **Packaging** — the core logic is structured as an installable Python package (`text_utils_pkg`), with both `pyproject.toml` and `setup.py`

## Project structure

text-utility-api/
├── app.py # Flask application and routes
├── text_utils_pkg/ # Installable package containing core logic
│ ├── init.py
│ └── text_utils.py
├── test_text_utils.py # Unit tests for the core logic
├── pyproject.toml # Package metadata (modern standard)
├── setup.py # Package metadata (compatibility)
├── requirements.txt # External dependencies
└── README.md

## Setup

1. Clone the repo:
   git clone https://github.com/ericrion42/text-utility-api.git
   cd text-utility-api

2. Create and activate a virtual environment:
   python -m venv venv
   venv\Scripts\activate # Windows
   source venv/bin/activate # macOS/Linux

3. Install dependencies:
   pip install -r requirements.txt

4. Install the local package in editable mode:
   pip install -e .

## Running the app

python app.py
The server starts at `http://127.0.0.1:5000`.

## API Endpoints

All endpoints accept `POST` requests with a JSON body containing a `"text"` field.

| Endpoint      | Description                       | Example request body      |
| ------------- | --------------------------------- | ------------------------- |
| `/palindrome` | Checks if text is a palindrome    | `{"text": "racecar"}`     |
| `/wordcount`  | Returns word and character counts | `{"text": "Hello world"}` |
| `/reverse`    | Reverses the given text           | `{"text": "Hello world"}` |

## Running tests

python -m unittest test_text_utils.py

## Running static analysis

pylint text_utils_pkg/text_utils.py
pylint test_text_utils.py

## Credits

Built by **Eric Rion** as a learning project, with guidance and assistance
from **Claude.ai** (Anthropic) used as a teaching tool throughout the build
process — including code explanations, debugging help, and step-by-step
walkthroughs of Flask, unit testing, static analysis, and Python packaging
concepts.
