import unittest

from classe_for_flashcard import Card,Deck

class Test_Cards(unittest.TestCase):

    #Some strings that should be valid
    new_strings=("",
                " ",
                "a",
                "avec espace",
                "MAJUSCULE",
                "MajetMinuscule",
                "Majuscule et minuscules avec espaces",
                "AccentséèàùêûîâÏÖÜË",
                "Avec-des_tirets"
                "Accént_tirêt_MÂjuscules")


    def test_edit_titles_new_titles(self):

        card= Card("title","question","answer","subject",0,True,0)

        for title in self.new_strings:
            card.edit_title(title)
            self.assertEqual(title,card.title)


    def test_edit_question_new_question(self):
        card= Card("title","question","answer","subject",0,True,0)

        for question in self.new_strings:
            card.edit_question(question)
            self.assertEqual(question,card.question)

    def test_edit_question_new_answer(self):
        card= Card("title","question","answer","subject",0,True,0)

        for answer in self.new_strings:
            card.edit_answer(answer)
            self.assertEqual(answer,card.answer)

    def test_edit_question_new_subject(self):
        card= Card("title","question","answer","subject",0,True,0)

        for subject in self.new_strings:
            card.edit_subject(subject)
            self.assertEqual(subject,card.subject)


class Test_Deck(unittest.TestCase):


    deck=Deck()
    deck.add_card("Tirana","What is the capital of Albania","Tirana","geography")
    deck.add_card("Alger","What is the capital of Algeria","Alger","geography")
    deck.add_card("Yerevan","What is the capital of Armenia","Yerevan","geography")
    deck.add_card("Canberra","What is the capital of Australia","Canberra","geography")
    deck.add_card("Dhaka","What is the capital of Bangladesh","Dhaka","geography")
    deck.add_card("Brussels","What is the capital of Belgium","Brussels","geography")
    deck.add_card("Sucre","What is the capital of Bolivia","Sucre","geography")
    deck.add_card("Brasilia","What is the capital of Brazil","Brasilia","geography")
    deck.add_card("Sofia","What is the capital of Bulgaria","Sofia","geography")
    deck.add_card("Ouagadougou","What is the capital of Burkina Faso","Ouagadougou","geography")
    deck.add_card("Phnom Penhh","What is the capital of Cambodia","Phnom Penh","geography")
    deck.add_card("Yaounde","What is the capital of Cameroon","Yaounde","geography")
#dernier doublé

    existing_titles=("Tirana","tirANa","Alger","alger","Yaounde","sofiA","SOFIA","Sofia","Ouagadougou","BRaSilia","pHNOM pENHH");

    unexisting_titles=("Coucou","Yaoundé"," Canberra","PhnomPenhh")

    def test_add_Card(self):
        deck=Deck()
        deck.add_card("title","question","answer","subject")

        self.assertEqual(len(deck.deck),1)
        self.assertEqual("title",deck.deck[0].title)
        self.assertEqual("question",deck.deck[0].question)
        self.assertEqual("answer",deck.deck[0].answer)
        self.assertEqual("subject",deck.deck[0].subject)


    def test_search_card(self):

        for title in self.existing_titles:
            self.assertNotEqual(None,self.deck.search_card(title))



    def test_search_card_unexisting_value(self):

        for titre in self.unexisting_titles:
            self.assertEqual(None,self.deck.search_card(titre))




if __name__ == '__main__':
    unittest.main()