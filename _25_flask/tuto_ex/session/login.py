from flask import *

app = Flask(__name__)
app.secret_key = "ali"


@app.route('/')
def home():
    return render_template("home_0.html")


@app.route('/login')
def login():
    return render_template("login_0.html")


@app.route('/success', methods=["POST"])
def success():
    if request.method == "POST":
        session['email'] = request.form['email']
    return render_template('success_0.html')


@app.route('/logout')
def logout():
    if 'email' in session:
        session.pop('email', None)
        return render_template('logout_0.html')
    else:
        return '<p>user already logged out</p>'


@app.route('/profile')
def profile():
    if 'email' in session:
        email = session['email']
        return render_template('profile_0.html', name=email)
    else:
        return '<p>Please login first</p>'


if __name__ == '__main__':
    app.run(debug=True)
