from flask import flask

app = Flask(__name__)
app.debug = True

@app.route("/")
def main():
    return "Hi!  I\'m a Flask Application."

if __name__ == "__main__":
    app.run(host="0.0.0.0")
