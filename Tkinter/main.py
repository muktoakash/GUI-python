"""./random_wprds.py

GUI App using PyQt5 that choses random words to display from
the nltk.corpus at the press of buttons.
"""

# Import Modules
from random import choice

# imports
from tkinter import Button, Label, messagebox,\
     LabelFrame
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# imports to use for words
from nltk.corpus import wordnet as wn
from PyDictionary import PyDictionary

# global constant:
NUM_RANDOM_WORDS = 3 # currently only choosing three random words
LEVEL = 0

# Class for main app
class RandomWords():
    """
    Creates a Tk() object to play the game.
    """
    def __init__(self):
        """Initialize"""
        # Main App Objects and Settings
        self.root = ttk.Window(themename="cyborg")

        # Title
        self.root.title("Vocab Show Down!")

        # Frame
        self.game_frame = LabelFrame(self.root, \
                                     text="Show off your vocabulary!", \
                                     padx=5, pady=5, \
                                     font=("Helvetica", 15))

        # Create all App Objects
        self.style_info = ttk.Style()
        self.style_info.configure('info.TButton', font=('Helvetica', 15))
        self.text1 = ttk.Button(self.game_frame, text="?", width=30, \
                            command=lambda : self.check_answer(0),
                            style='info.TButton')
        self.text2 = ttk.Button(self.game_frame, text="?", width=30, \
                            command=lambda : self.check_answer(1),
                            style='info.TButton')
        self.text3 = ttk.Button(self.game_frame, text="?", width=30, \
                            command=lambda : self.check_answer(2),
                            style='info.TButton')

        self.give_up = ttk.Button(self.game_frame, text="Pass!",
                                command = self.pass_round,
                                width=60, bootstyle='light',)

        self.random_words = [self.text1, self.text2, self.text3]

        # Use all words in nltk corpus with a meaning
        self.word_list = list(word for word in wn.words() if word.isalpha())

        # Game variables
        self.answer = "?"
        self.parts_of_speech = "?"
        self.meaning = Label(self.game_frame, text="?",
                             height=5, width=100,
                              wraplength=700, font=("Helvetica", 15))
        self.correct = 0
        self.wrong = 0
        self.passed = 0
        self.exp_req = LEVEL+1 *

        # Top objects:
        self.score_book = ttk.Label(self.root,
                                    text = "Current Score: " \
                                        + str(self.get_score()),
                                    font = ("Courier", 15),
                                    bootstyle='primary')

        self.score_frame = ttk.LabelFrame(self.root,
                                          text = "Score Book",
                                          bootstyle = 'primary')

        self.num_correct = ttk.Label(self.score_frame,
                                     text = "Correct Answers: " \
                                     + str(self.correct),
                                     font = ("Courier", 12))

        self.num_wrong = ttk.Label(self.score_frame,
                                     text = "Wrong Answers: " \
                                     + str(self.wrong),
                                     font = ("Courier", 12))

        self.num_passed = ttk.Label(self.score_frame,
                                     text = "Passed: " \
                                          + str(self.passed),
                                     font = ("Courier", 12))


        # Layout
        # self.root.geometry("800x600")
        self.score_book.pack(padx=15, pady=15)

        self.score_frame.pack(fill=X, padx=15, pady=15,)
        self.num_correct.grid(row=0, column=0, padx=100, sticky='nsew')
        self.num_wrong.grid(row=0, column=1, padx=100, sticky='nsew')
        self.num_passed.grid(row=0, column=2, padx=100, sticky='nsew')

        self.game_frame.pack(padx=5, pady=5, fill=X)
        self.meaning.grid(row=0, column=0, columnspan=3, sticky='E'+'W',)
        for index in range(NUM_RANDOM_WORDS):
            self.random_words[index].grid(row = 1, column = index)

        self.give_up.grid(row=3, column=1, pady=15)

        # Initialize
        self.play_game()

    # Getting Random Words
    def random_word(self):
        """
        Chooses a random word to append to random_words
        side-effect: Modifies random_words
        """

        def get_synonyms(word):
            """
            helper function to get all synonyms of a word
            """
            synset = set()
            for similar in wn.synonyms(word):
                for syn in similar:
                    if syn.isalpha():
                        synset.add(syn)
            return synset

        for index in range(NUM_RANDOM_WORDS):
            current_words = [self.random_words[i]["text"] \
                              for i in range(NUM_RANDOM_WORDS)]
            word = choice(self.word_list)
            synonyms = get_synonyms(word).union(*[get_synonyms(wd)\
                                                   for wd in current_words])
            while word in current_words or word in synonyms:
                word = choice(word_list)
            self.random_words[index].configure(text=word)

    def play_game(self):

        def fix_parentheses(input_str):
            "helper function to fix unmatched parenthesis in meanting"
            if "(" in input_str and ")" not in input_str:
                input_str = input_str + ")"
            return input_str

        self.random_word()
        current_words = [self.random_words[i]["text"] \
                              for i in range(NUM_RANDOM_WORDS)]
        self.answer = choice(current_words)
        means = PyDictionary.meaning(self.answer)
        random_key = choice(list(means.keys()))
        random_meaning = choice(list(means[random_key]))
        random_meaning = fix_parentheses(random_meaning)
        self.meaning["text"] = random_meaning
        self.parts_of_speech = random_key

    def check_answer(self, btn_num):
        if self.random_words[btn_num]["text"] == self.answer:
            self.correct += 1
            response = messagebox.askyesno("You got it!",\
                                f'{self.answer} - \n' + \
                                f'{self.parts_of_speech} : {self.meaning["text"]}',
                                icon = 'info')
        else:
            self.wrong += 1
            response = messagebox.askyesno("Sorry", \
                                f'The right answer was \n' + \
                                f'{self.answer} - \n' + \
                                f'{self.parts_of_speech} : {self.meaning["text"]}',
                                icon = 'error')

        self.score_book["text"] = "Current Score: " \
                                + str(self.get_score())

        self.num_correct["text"] = "Correct Answers: " + str(self.correct)
        self.num_wrong["text"] = "Wrong Answers: " + str(self.wrong)

        if response:
            self.play_game()
        else:
            self.root.destroy()

    def pass_round(self):
        self.passed += 1
        self.num_passed["text"] = "Passed: " + str(self.passed)
        self.play_game()

    def get_score(self):
        return 5 * self.correct - 2 * self.wrong

# Show/Run our App
if __name__== "__main__":
    app = RandomWords()
    app.root.mainloop()
