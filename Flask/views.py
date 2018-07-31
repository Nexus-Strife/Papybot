from flask import Flask, render_template  # Import of the flask's lib

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")  # Display index.html which contain the user interface


if __name__ == "__main__":
    app.run()  # Run local server
