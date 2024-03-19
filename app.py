from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Live Life Easily!'

if __name__ == '__main__':
    app.run()

