from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World"


@app.route('/index/')
def index():
    return "welcome to my homepage"


@app.route('/index/contact/')
def contact():
    return "Contact Me"


if __name__ == '__main__':
    app.debug = True
    app.run()
