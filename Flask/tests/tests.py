import random
import pytest

positive_answer_list = ["J'vais te dire c'que j'sais mon gamin. ", "J'vais t'dire mon lapin: ", "Oh je connais"
                        " des choses sur cet endroit ! ",
                        "Ca fait un bout d'temps qu'j'ai pas mis les pieds là-bas mon p'tiot ! Et j'en connais"
                        " un rayon sur cet endroit ! "]

negative_answer_list = ["...Pardon.. ?", "De quoi ? J'connais pas mon lapin", "C'est ou ça ?", "...C'est nouveau ? Ca"
                                                                                               " m'dit rien ton affaire"]

know_address_list = ["Voui ! L'adresse c'était...c'était quoi déjà ? Ah voui ! C'était: ", "J'connais cette adresse ! ",
                     "J'connais cette adresse là-bas: "]


def papy_answer(answer_lst):  # Method which pick-up a random sentence from the lists above.
    rand = random.randint(0, len(answer_lst) - 1)
    string = answer_lst[rand]
    return string


def test_papy_positive():
    var = papy_answer(positive_answer_list)
    assert var in positive_answer_list


def test_papy_negative():
    var = papy_answer(negative_answer_list)
    assert var in negative_answer_list


def test_papy_address():
    var = papy_answer(know_address_list)
    assert var in know_address_list

