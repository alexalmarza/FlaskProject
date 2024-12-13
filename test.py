from flask import Flask

app = Flask(__name__)
@app.route('/')

def hello_world():
    return 'hello tes 23'

if __name__ == '__main__':
    app.run(debug=True)