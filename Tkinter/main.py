"""./random_wprds.py

GUI App using PyQt5 that choses random words to display from
the nltk.corpus at the press of buttons.
"""

# Import Modules
from random import choice

# imports
from tkinter import Tk, Button, Label, messagebox,\
     LabelFrame, END

# imports to use for words
from nltk.corpus import wordnet as wn
from PyDictionary import PyDictionary

# global constant:
NUM_RANDOM_WORDS = 3 # currently only choosing three random words

# Class for main app
class RandomWords():
    """
    Creates a Tk() object to play the game.
    """
    def __init__(self):
        """Initialize"""
        # Main App Objects and Settings
        self.root = Tk()

        # Title
        self.root.title("Vocab Show Down!")

        # Frame
        self.game_frame = LabelFrame(self.root,
                                     text="Show off your vocabulary!",
                                     padx=50, pady=50)

        # Create all App Objects
        self.text1 = Button(self.game_frame, text="?", height=2, width=30, \
                            command=lambda : self.check_answer(0))
        self.text2 = Button(self.game_frame, text="?", height=2, width=30, \
                            command=lambda : self.check_answer(1))
        self.text3 = Button(self.game_frame, text="?", height=2, width=30, \
                            command=lambda : self.check_answer(2))
        self.button = Button(self.game_frame, text="Play Again!", command = self.play_game)

        self.random_words = [self.text1, self.text2, self.text3]

        # Use all words in nltk corpus with a meaning
        self.word_list = list(word for word in wn.words() if word.isalpha())

        # Game variables
        self.answer = "?"
        self.parts_of_speech = "?"
        self.meaning = Label(self.game_frame, text="?", height=5, width=100)
        self.correct = 0
        self.wrong = 0

        # Layout
        self.game_frame.pack(padx=5, pady=5)
        self.meaning.grid(row=0, column=1)
        for index in range(NUM_RANDOM_WORDS):
            self.random_words[index].grid(row = 1, column = index)

        self.button.grid(row=3, column=1)

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
        self.random_word()
        current_words = [self.random_words[i]["text"] \
                              for i in range(NUM_RANDOM_WORDS)]
        self.answer = choice(current_words)
        means = PyDictionary.meaning(self.answer)
        random_key = choice(list(means.keys()))
        random_meaning = choice(list(means[random_key]))
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
        if response:
            self.play_game()
        else:
            self.root.destroy()


# Show/Run our App
if __name__== "__main__":
    app = RandomWords()
    app.root.mainloop()
