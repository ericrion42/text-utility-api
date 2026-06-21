# app.py
# This is the entry point for our Flask application.
# Right now it just confirms Flask is installed and working correctly.

from flask import Flask

from flask import Flask, request, jsonify
from text_utils_pkg.text_utils import is_palindrome, word_count, reverse_text

# ANSI color codes for console output.
# These work in most modern terminals, including VS Code's integrated terminal.
class Colors:
    RED = '\033[91m'      # Errors
    ORANGE = '\033[93m'   # Data/header information (closest ANSI has to true orange)
    YELLOW = '\033[33m'   # Menus and prompts
    GREEN = '\033[92m'    # Success messages
    RESET = '\033[0m'     # Resets color back to terminal default — always use after colored text

# Create the Flask application object.
# __name__ tells Flask where to look for resources relative to this file.
app = Flask(__name__)

# This decorator tells Flask: "when someone visits the root URL ('/'),
# run the function right below it."
@app.route('/')
def home():
    return "Text Utility API is running."

@app.route('/palindrome', methods=['POST'])
def check_palindrome():
    # Get the JSON data sent in the request body.
    data = request.get_json()

    # Validate that the request actually included a "text" field.
    if not data or 'text' not in data:
        print(f"{Colors.RED}ERROR: /palindrome called with missing 'text' field{Colors.RESET}")
        return jsonify({"error": "Request must include a 'text' field"}), 400

    text = data['text']
    result = is_palindrome(text)

    print(f"{Colors.GREEN}SUCCESS: /palindrome checked \"{text}\" -> {result}{Colors.RESET}")
    return jsonify({"input": text, "is_palindrome": result})

@app.route('/wordcount', methods=['POST'])
def check_word_count():
    data = request.get_json()

    if not data or 'text' not in data:
        print(f"{Colors.RED}ERROR: /wordcount called with missing 'text' field{Colors.RESET}")
        return jsonify({"error": "Request must include a 'text' field"}), 400

    text = data['text']
    result = word_count(text)

    print(f"{Colors.GREEN}SUCCESS: /wordcount checked \"{text}\" -> {result}{Colors.RESET}")
    return jsonify({"input": text, "word_count": result})

@app.route('/reverse', methods=['POST'])
def reverse_string():
    data = request.get_json()

    if not data or 'text' not in data:
        print(f"{Colors.RED}ERROR: /reverse called with missing 'text' field{Colors.RESET}")
        return jsonify({"error": "Request must include a 'text' field"}), 400

    text = data['text']
    result = reverse_text(text)

    print(f"{Colors.GREEN}SUCCESS: /reverse checked \"{text}\" -> \"{result}\"{Colors.RESET}")
    return jsonify({"input": text, "reversed": result})

if __name__ == '__main__':
    print(f"{Colors.ORANGE}Text Utility API starting up...{Colors.RESET}")
    print(f"{Colors.ORANGE}Available routes: /palindrome, /wordcount, /reverse (all POST){Colors.RESET}")
    app.run(debug=True)