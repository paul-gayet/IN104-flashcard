import datetime
import pickle
import csv


class Card:
    """
    Class to define a FlashCard
    """

    def __init__(self, title, question, answer, subject, location, reviewed, date):
        self.title = title
        self.question = question
        self.answer = answer
        self.subject = subject
        self.location = location
        self.reviewed = reviewed
        self.date = date

    def edit_title(self, title):
        self.title = title

    def edit_question(self, question):
        self.question = question

    def edit_answer(self, answer):
        self.answer = answer

    def edit_subject(self, subject):
        self.subject = subject


class Deck:
    """
    A deck contains a list of Cards
    """

    def __init__(self):
        self.deck = []

    def add_card(self, title, top, bottom, subject):
        card = Card(title, top, bottom, subject, 0, False, datetime.datetime.now())
        self.deck.append(card)

    def delete_card(self, card):
        if card != None:
            self.deck.remove(card)

    def save_deck(self, name):
        with open(name, 'wb') as f:
            pickle.dump(self.deck, f)

    def load_deck(self, name):
        with open(name, 'rb') as f:
            self.deck = pickle.load(f)

    def search_card(self, title):
        for card in self.deck:
            if card.title.lower() == title.lower():
                return card

        return None

    def load_deck_from_csv(self, file):
        with open(file, 'r') as f:
            data = csv.reader(f)
            for row in data:
                if len(row) != 4:
                    raise Exception("Incorrect line : " + row)
                self.add_card(row[0], row[1], row[2], row[3])
