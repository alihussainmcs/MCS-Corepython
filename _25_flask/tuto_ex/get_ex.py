from flask import *

app = Flask(__name__)


@app.route('/login_1', methods=['GET'])
def login():
    uname = request.args.get('uname')
    passwrd = request.args.get('pass')
    if uname == "Thor" and passwrd == "cyclone":
        return "Welcome %s" % uname


if __name__ == '__main__':
    app.run(debug=True)
