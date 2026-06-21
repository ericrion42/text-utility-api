# app.py
# This is the entry point for our Flask application.
# Right now it just confirms Flask is installed and working correctly.

from flask import Flask

# Create the Flask application object.
# __name__ tells Flask where to look for resources relative to this file.
app = Flask(__name__)

# This decorator tells Flask: "when someone visits the root URL ('/'),
# run the function right below it."
@app.route('/')
def home():
    return "Text Utility API is running."

# This block only runs if we execute this file directly (python app.py),
# not if it gets imported elsewhere. Standard Python convention.
if __name__ == '__main__':
    app.run(debug=True)