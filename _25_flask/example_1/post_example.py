from flask import *

app = Flask(__name__)


@app.route('/')
def message():
    return render_template('message_1.html')


@app.route('/login1', methods=['GET'])
def login1():
    uname = request.args.get('uname')
    password = request.args.get('pass')
    if uname == "ali" and password == "ali":
        return "Welcome %s" % uname
    return render_template('login_1.html')


if __name__ == '__main__':
    app.run(debug=True)
