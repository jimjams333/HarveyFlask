from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Harveys Simple Flask App v2</h1>"

@app.route('/info')
def info():
    return "<h2>Harveys Flask App Info Page</h2>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    