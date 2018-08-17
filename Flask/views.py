from flask import Flask, render_template, request  # Import of the flask's lib
from flask_googlemaps import GoogleMaps
import json
import webbrowser


app = Flask(__name__)

GoogleMaps(app, key='AIzaSyDPEk_9cUI_Z9aeLSMn-JnnXKFjvxW7r-s')


cities = ['Paris']


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")  # Display index.html which contain the UI


def mapview():
    # creating a map in the view
    mymap = Map(
        identifier="view-map",
    )
    return render_template('index.html', mymap=mymap)


@app.route('/result', methods=['POST'])
def result():
    txt = request.form['research'];
    if txt in cities:
        webbrowser.open('https://google.fr/maps/place/' + txt)
    else:
        pass
    return json.dumps({'status': 'OK', 'txt': txt});


@app.route("/resultat", methods=['POST'])
def resultat():
    txt = request.form['research'];
    if txt in cities:
        webbrowser.open('http://google.fr/maps/place/' + txt)
    else:
        pass
    return json.dumps({'status': 'OK', 'txt': txt});


if __name__ == "__main__":
    app.run()  # Run local server
