from flask import Flask
import os

app = Flask(__name__)
# first you must: $ heroku config:set APP_SETTINGS=config.StagingConfig --remote stage1
app.config.from_object(os.environ['APP_SETTINGS'])


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()


