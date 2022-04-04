from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    """Function return h1 tag at endpoint 127.0.0.1:5000/"""
    return "<h1>Hello WSB! Greetings from Flask & Docker!<h1>"


if __name__ == "__main__":
    app.run(debug=True)
