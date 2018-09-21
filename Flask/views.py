from flask import Flask, render_template, request  # Import of the flask's lib
from flask_googlemaps import GoogleMaps
import json
import wikipediaapi


app = Flask(__name__) # Initialization of Flask

GoogleMaps(app, key='AIzaSyDPEk_9cUI_Z9aeLSMn-JnnXKFjvxW7r-s')

wiki_wiki = wikipediaapi.Wikipedia('fr')  # Initialization of Wikipedia API
page_paris = wiki_wiki.page("Nintendo")
city = ["Paris"]
susp = "..."


@app.route('/', methods=['GET', 'POST'])
def index():

    paris = "Paris"

    if paris in city:
        wiki_desc = page_paris.summary[0:295]
        response = render_template("index.html", wiki_desc=wiki_desc)
        return response
    else:
        wiki_desc = page_paris.summary[0:295]
        return render_template("index.html")


@app.route("/update_map", methods=['GET', 'POST'])
def update_map():

    var = request.form.get('research');

    if var == "":
        pass

    else:
        stop_words_json = json.loads(open("static/stop_words_fr.json").read())

        for words in var.split():
            word_lowercase = words.lower()
            page_in_wiki = wiki_wiki.page(words)
            exist = page_in_wiki.exists()

            if exist == False:  # Si la page du mot en cours n'existe pas

                if word_lowercase in stop_words_json["stop_words"]:
                    pass
                else:
                    pass

            else:  # Si la page du mot en cours existe
                if word_lowercase in stop_words_json["stop_words"]:
                    pass

                else:

                    page_to_read = wiki_wiki.page(words)
                    text = page_to_read.summary[0:300]

                    if not text:
                        print("J'sais pas grand chose là d'sus mon p'tit gars")
                        # rajouter adresse
                    else:
                       text_susp = text + susp
                       print("J'vais te dire c'que j'sais mon gamin. " + text_susp)
                       print(page_to_read.fullurl)
                       # rajouter url wiki et adresse

    return json.dumps({'status': 'OK'});


if __name__ == "__main__":
    app.run(debug=True)  # Run local server. Mode debug on for developpment
