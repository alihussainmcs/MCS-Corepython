from flask import *

app = Flask(__name__)


@app.route('/login', methods=['GET'])
def login():
    uname = request.args.get('uname')
    passwrd = request.args.get('pass')
    if uname == "ayush" and passwrd == "google":
        return "Welcome %s" % uname
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
