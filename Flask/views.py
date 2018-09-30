from flask import Flask, render_template, request  # Import of the flask's lib
import json  # Json plugin is needed for read the stop words's list and respond to the template
import wikipediaapi  # Plugin used to make req to wikipedia, listed on mediawiki
import random  # The random lib is used to take random sentence for the answers
import time  # time.sleep

app = Flask(__name__)  # Initialization of Flask

wiki_wiki = wikipediaapi.Wikipedia('fr')  # Initialization of Wikipedia API

positive_answer_list = ["J'vais te dire c'que j'sais mon gamin. ", "J'vais t'dire mon lapin: ", "Oh je connais"
                        " des choses sur cet endroit ! ",
                        "Ca fait un bout d'temps qu'j'ai pas mis les pieds là-bas mon p'tiot ! Et j'en connais"
                        " un rayon sur cet endroit ! "]

negative_answer_list = ["...Pardon.. ?", "De quoi ? J'connais pas mon lapin", "C'est ou ça ?", "...C'est nouveau ? Ca"
                                                                                               " m'dit rien ton affaire"]

know_address_list = ["Voui ! L'adresse c'était...c'était quoi déjà ? Ah voui ! c'était: ", "J'connais cette adresse ! ",
                     "J'connais cette adresse là-bas: "]
susp = "..."


def papy_answer(answer_lst):  # Method which pick-up a random sentence from the lists above.
    rand = random.randint(0, len(answer_lst) - 1)
    string = answer_lst[rand]
    return string


@app.route('/', methods=['GET', 'POST'])  # Talk from itself
def index():
    return render_template("index.html")  # Render index.html to the window


"""The next route is the main one. Once the user submit his request
the content of input is parsed. Then, if the subject of the
research have a wikipedia page, PaPYbot return an answer which 
is displayed onto the page, without refreshing it."""


@app.route("/update_map", methods=['POST'])
def update_map():

    var = request.form.get('research');

    if var == "":
        return json.dumps({'status': 'OK', 'answer': ""});  # If var is empty then return an empty answer

    else:
        stop_words_json = json.loads(open("static/stop_words_fr.json").read())

        for words in var.split():  # Begin the parsing of every word
            word_lowercase = words.lower()  # Put every words into lowercase -easiest way to parse-
            page_in_wiki = wiki_wiki.page(words)  # Then put in var the supposed url of the wiki page of the current word
            exist = page_in_wiki.exists()  # And check if it exist

            if not exist:  # If the page doesn't exist ...

                if word_lowercase in stop_words_json["stop_words"]:  # ... Check if the word is in the stop-word's list
                    pass  # If it the case, do nothing

                else:
                    return json.dumps({'status': 'Ok', 'answer': ''})  # If it not the case reply an empty answer

            else:  # Otherwise...
                if word_lowercase in stop_words_json["stop_words"]:  # Same thing than the first condition...
                    pass

                else:
                    page_to_read = wiki_wiki.page(words)  # Put in var the url the word which isn't in the stop words and which return a page
                    text = page_to_read.summary[0:400]  # Withdraw the 400 first chars of the page

                    if text == "":  # If the page is blank which happen sometimes...
                        negative_answer = (papy_answer(negative_answer_list))  # Pick-up a random sentence from the negative answer's list...
                        return json.dumps({'status': 'Ok', 'answer': negative_answer})  # And return it by the json reponse

                    else:
                        text_susp = text + susp  # Put in var the 400 chars + ellipsis
                        positive_answer = (papy_answer(positive_answer_list) + text_susp)  # Pick-up a random sentence from the positive answer's list
                        link_wiki = page_to_read.fullurl  # Make a variable of the url

                        time.sleep(4)  # Wait a little before sending the answer with the link
                        return json.dumps({'status': 'OK', 'answer': positive_answer, 'link': link_wiki});


"""The next route was created only to display an answer that create a better answer concerning the address"""


@app.route("/answer", methods=["POST", "GET"])
def answer():

    know_address = papy_answer(know_address_list)  # Pick-up a sentence from the know_address's list

    return json.dumps({'status': 'OK', 'know': know_address});

