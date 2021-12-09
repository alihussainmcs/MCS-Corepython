from flask import Flask

app = Flask(__name__)  # creating the Flask class object


@app.route('/')  # decorator defines the
def home():
    return "hello, this is our first 00_flask website"


if __name__ == '__main__':
    app.run(debug=True)
