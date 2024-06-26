from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! new stable app! on pull request!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
