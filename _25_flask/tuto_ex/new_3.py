from flask import *

app = Flask(__name__)


@app.route('/table/<int:num>')
def table(num):
    return render_template('message_3.html', n=num)


if __name__ == '__main__':
    app.run(debug=True, port=12345)


# http://127.0.0.1:12345/table/10
