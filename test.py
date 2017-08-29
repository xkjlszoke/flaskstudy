from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'wrajj_forever'

if __name__ == '__main__':
    app.run()
