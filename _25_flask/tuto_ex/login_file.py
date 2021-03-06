"""
Login application in Flask
Here, we will create a login application in the flask where a login page (login_0.html) is shown to the user which prompts
    to enter the email and password. If the password is "jtp", then the application will redirect the user to the
    success page (success_0.html) where the message and a link to the profile (profile.html) is given otherwise it will
    redirect the user to the error page.

The controller python flask script (login_03.py) controls the behaviour of the application. It contains the view functions
    for the various cases. The email of the user is stored on the browser in the form of the cookie. If the password
    entered by the user is "jtp", then the application stores the email id of the user on the browser as the cookie
    which is later read in the profile page to show some message to the user.

The application contains the following python and HTML script.The directory structure of the application is given below.

"""

from flask import *

app = Flask(__name__)


@app.route('/error')
def error():
    return "<p><strong>Enter correct password</strong></p>"


@app.route('/')
def login():
    return render_template("login_file.html")


@app.route('/success', methods=['POST'])
def success():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['pass']

    if password == "12345":
        resp = make_response(render_template('login_file_success.html'))
        resp.set_cookie('email', email)
        return resp
    else:
        return redirect(url_for('error'))


@app.route('/viewprofile')
def profile():
    email = request.cookies.get('email')
    resp = make_response(render_template('login_file_profile.html', name=email))
    return resp


if __name__ == "__main__":
    app.run(debug=True)