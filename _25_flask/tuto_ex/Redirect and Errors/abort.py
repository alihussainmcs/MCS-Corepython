from flask import *

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home_3.html")


@app.route('/login')
def login():
    return render_template("login_03.html")


@app.route('/validate', methods=["POST"])
def validate():
    if request.method == 'POST' and request.form['pass'] == 'jtp':
        return redirect(url_for("success"))
    else:
        abort(401)


@app.route('/success')
def success():
    return "logged in successfully"


if __name__ == '__main__':
    app.run(debug=True)

    ''' 
    if password is not jtp below o/p will come
    Unauthorized
The server could not verify that you are authorized to access the URL requested. You either supplied the wrong 
credentials (e.g. a bad password), or your browser doesn't understand how to supply the credentials required.
    '''