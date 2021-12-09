from flask import *

app = Flask(__name__)


@app.route('/')
def message():
    return render_template('message_1.html')


if __name__ == '__main__':
    app.run(debug=True, port=12345)
