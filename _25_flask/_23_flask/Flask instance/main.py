'''
steps to deploy a flask application

1. import packages, modules as per requirements.txt using  "pip install flask"
(pip install --upgrade pip,  pip install -r requirements.txt)

2. create app instance
 ( app = flask(__name__)

3. create route, path and callable declarations
  @app.route('/')
      def get():
          return "hello"

4. App confugaration to run
     if __name__ == '__main__':

5. give the port  which is 8000, 5000, 1234  0000



'''

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "welcome to home page"


@app.route('/index')
def home():
    return "welcome to index page"


@app.route('/welcome')
def welcome():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=1234)




