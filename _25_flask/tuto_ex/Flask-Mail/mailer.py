from flask import *
from flask_mail import *
from random import *

app = Flask(__name__)
mail = Mail(app)

app.config["MAIL_SERVER"] = 'smtp.gmail.com'
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = 'alian1435678@gmail.com'
app.config['MAIL_PASSWORD'] = 'Alian!@#$%'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

otp = randint(000000, 999999)


@app.route('/')
def index():
    return render_template("mail_index.html")


@app.route('/verify', methods=["POST"])
def verify():
    email = request.form["email"]

    msg = Message('OTP', sender='alian1435678@gmail.com', recipients=[email])
    msg.body = str(otp)
    mail.send(msg)
    return render_template('mail_verify.html')


@app.route('/validate', methods=["POST"])
def validate():
    user_otp = request.form['otp']
    if otp == int(user_otp):
        return "<h3>Email verified successfully</h3>"
    return "<h3>failure</h3>"


if __name__ == '__main__':
    app.run(debug=True)
