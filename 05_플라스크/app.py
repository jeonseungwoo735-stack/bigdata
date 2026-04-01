from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/Hello")
def hello():
    return("만나서 반갑습니다.")

@app.route("/user/<userid>")
def profile(userid):
    return f"{userid}\' profile"

if __name__ == "__main__":
    app.run()