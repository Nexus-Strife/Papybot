from flask import Flask, render_template, request  # Import of the flask's lib
from flask_googlemaps import GoogleMaps
import json
import wikipediaapi
import random
import time


app = Flask(__name__) # Initialization of Flask

GoogleMaps(app, key='AIzaSyDPEk_9cUI_Z9aeLSMn-JnnXKFjvxW7r-s')

wiki_wiki = wikipediaapi.Wikipedia('fr')  # Initialization of Wikipedia API

positive_anwser_list = ["J'vais te dire c'que j'sais mon gamin. ", "J'vais t'dire mon lapin: ", "Oh je connais"
                        " des choses sur cet endroit ! ",
                        "Ca fait un bout d'temps qu'j'ai pas mis les pieds là-bas mon p'tiot ! Et j'en connais"
                        " un rayon sur cet endroit ! "]

negative_anwser_list = ["...Pardon.. ?", "De quoi ? J'connais pas mon lapin", "C'est ou ça ?", "...C'est nouveau ? Ca"
                                                                                               "m'dit rien ton affaire"]

know_address_list = ["Voui ! L'adresse c'était...c'était quoi déjà ? Ah voui ! c'était: ", "J'connais cette adresse ! ",
                     "J'connais cette adresse là-bas: "]
susp = "..."


def papy_anwser(anwser_lst):
    rand = random.randint(0, len(anwser_lst) - 1)
    string = anwser_lst[rand]
    return string


@app.route('/', methods=['GET', 'POST'])
def index():

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

            if not exist:  # Si la page du mot en cours n'existe pas

                if word_lowercase in stop_words_json["stop_words"]:
                    pass
                else:
                    pass

            else:  # Si la page du mot en cours existe
                if word_lowercase in stop_words_json["stop_words"]:
                    pass

                else:

                    page_to_read = wiki_wiki.page(words)
                    text = page_to_read.summary[0:400]

                    if text == "":
                        negative_anwser = (papy_anwser(negative_anwser_list))
                        return json.dumps({'status': 'OK', 'answer': negative_anwser});

                    else:
                        text_susp = text + susp
                        positive_answer = (papy_anwser(positive_anwser_list) + text_susp)
                        link_wiki = page_to_read.fullurl

                        time.sleep(4)
                        return json.dumps({'status': 'OK', 'answer': positive_answer, 'link': link_wiki});


@app.route("/answer", methods=["POST", "GET"])
def answer():

    know_address = papy_anwser(know_address_list)

    return json.dumps({'status': 'OK', 'know': know_address});


if __name__ == "__main__":
    app.run(debug=True)  # Run local server. Mode debug on for dev
