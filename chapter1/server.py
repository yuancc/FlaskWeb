from flask import Flask, current_app
from flask_script import Manager

app = Flask(__name__)

'''app_ctx = app.app_context()
app_ctx.push()
print(current_app.name)
print(app.url_map)'''
manager = Manager(app)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>', 404


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name


if __name__ == '__main__':
    app.run(debug=True)
