"""./random_wprds.py

GUI App using PyQt5 that choses random words to display from
the nltk.corpus at the press of buttons.
"""

# Import Modules
from time import sleep
from math import atan, pi
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
LEVELS = 5 # Game ends when level 20 is reached

# Class for main app
class RandomWords():
    """
    Creates a Tk() object to play the game.
    """
    def __init__(self):
        """Initialize"""
        # Main App Objects and Settings
        self.root = ttk.Window(themename="morph")

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

        # Initialize Game variables
        self.WIN = False

        self.answer = "?"
        self.parts_of_speech = "?"

        self.meaning = Label(self.game_frame, text="?",
                             height=5, width=100,
                              wraplength=700, font=("Helvetica", 15))
        self.correct = 0
        self.wrong = 0
        self.passed = 0

        self.current_level = 1
        self.current_exp = 0

        self.answer_checked_or_passed = True


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

        self.display_level = ttk.Label(self.root,
                                       text = "Current Level: " \
                                        + str(self.current_level),
                                        font = ("Helvetica", 15),
                                        bootstyle=SUCCESS)
        self.exp_gauge = ttk.Floodgauge(
            bootstyle=SUCCESS,
            font=(None, 24, 'bold'),
            mask='XP: {}%',
            )

        # Bottom Objects
        self.display_result = ttk.LabelFrame(self.root,
                                             text="Result",
                                             bootstyle=SUCCESS)
        self.display_answer = ttk.Label(self.display_result,
                                        text="Click a word above to see the result",
                                        wraplength=700,
                                        font=("Courier", 15),
                                        bootstyle=SUCCESS)
        # self.proceed = ttk.Button(self.display_result,
        #                             text="Next Round >>",
        #                             bootstyle = WARNING,
        #                             command=self.next_round,
        #                             state=DISABLED )
        self.leave = ttk.Button(self.display_result,
                                text="Quit Game",
                                bootstyle = DANGER,
                                command=self.root.destroy)

        # Layout
        # self.root.geometry("800x600")

        # Top:
        self.score_book.pack(padx=15, pady=15)

        self.display_level.pack(padx=15, pady=15)
        self.exp_gauge.pack(fill=BOTH, expand=YES, padx=10, pady=10)

        self.score_frame.pack(fill=X, padx=15, pady=15,)
        self.num_correct.grid(row=0, column=0, padx=100, sticky='nsew')
        self.num_wrong.grid(row=0, column=1, padx=100, sticky='nsew')
        self.num_passed.grid(row=0, column=2, padx=100, sticky='nsew')

        #Game
        self.game_frame.pack(padx=5, pady=5, fill=X)
        self.meaning.grid(row=0, column=0, columnspan=3, sticky='E'+'W',)
        for index in range(NUM_RANDOM_WORDS):
            self.random_words[index].grid(row = 1, column = index)

        self.give_up.grid(row=3, column=1, pady=15)

        # Result
        self.display_result.pack(padx=15, pady=15)
        self.display_answer.pack(fill=X)
        self.leave.pack(fill=X)
        # self.display_answer.grid(row=0, column=0,
        #                          columnspan=2, padx=50, pady=15)
        # self.proceed.grid(row=1, column=1, padx=50, pady=15, sticky="ew")
        # self.leave.grid(row=1, column=0, padx=50, pady=15, sticky="ew")

        # Initialize
        self.play_game()
        # while not self.WIN:
        #     self.play_game()
        #     if self.answer_checked_or_passed == False:
        #         sleep(10)

        # while self.answer_checked_or_passed and not self.WIN:
        #     self.answer_checked_or_passed = False
        #     self.play_game()
        if self.WIN:
            self.root.destroy()

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
            current_words = [self.random_words[i].cget('text') \
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

        if self.WIN:
            messagebox.showinfo("Winner!", "You Won!")
            return True

        self.answer_checked_or_passed = False
        self.random_word()
        current_words = [self.random_words[i].cget('text') \
                              for i in range(NUM_RANDOM_WORDS)]
        self.answer = choice(current_words)
        means = PyDictionary.meaning(self.answer)
        random_key = choice(list(means.keys()))
        random_meaning = choice(list(means[random_key]))
        random_meaning = fix_parentheses(random_meaning)
        self.meaning["text"] = random_meaning
        self.parts_of_speech = random_key

        return True

    def check_answer(self, btn_num):

        if self.WIN:
            messagebox.showinfo("Winner!", "You Won!")
            return True

        self.answer_checked_or_passed = False
        # self.give_up["state"] = DISABLED
        # self.proceed['state'] = NORMAL
        if self.random_words[btn_num]["text"] == self.answer:
            self.correct += 1
            self.display_result["text"] = "You Got It!"
            self.display_result.configure(bootstyle=SUCCESS)
            self.display_answer["text"] =f'{self.answer} - \n' + \
                  f'{self.parts_of_speech} : {self.meaning["text"]}'
            self.display_answer.configure(bootstyle=SUCCESS)
        else:
            self.wrong += 1
            self.display_result["text"] ="Sorry, " + 'The right answer was:'
            self.display_result.configure(bootstyle=WARNING)
            self.display_answer["text"] = f'{self.answer} - \n' + \
                                f'{self.parts_of_speech} : {self.meaning["text"]}'
            self.display_answer.configure(bootstyle=WARNING)

        self.score_book["text"] = "Current Score: " \
                                + str(self.get_score())

        self.num_correct["text"] = "Correct Answers: " + str(self.correct)
        self.num_wrong["text"] = "Wrong Answers: " + str(self.wrong)

        self.current_exp = self.exp_get()

        self.display_level["text"] = "Current Level: " \
                                        + str(self.current_level)

        self.answer_checked_or_passed = True

        self.play_game()
        return True

    def pass_round(self):

        if self.WIN:
            messagebox.showinfo("Winner!", "You Won!")
            return True

        self.answer_checked_or_passed = False

        self.passed += 1
        self.num_passed["text"] = "Passed: " + str(self.passed)

        self.answer_checked_or_passed = True
        self.play_game()
        return True

    def get_score(self):
        return max(5 * self.correct - 2 * self.wrong, 0)

    def exp_multiplier(self):
        return atan(self.current_level / LEVELS * pi /4 ) # return value <= 1

    def exp_increment(self):
        # in future versions may be use exp_multiplier
        multiplier = self.exp_multiplier()

        # Current version:
        multiplier = 0

        exp_increment = 1 - multiplier * self.current_exp
        return exp_increment

    def exp_get(self):
        """self.exp_get()

        Computes the experience achieved at a certain level based on the score,
        with the default being the maximum score allowed for the given level.

        Side effects:
        - conditionally modifies self.current_level
        - conditionally modifies self.WIN

        Requires:
        1 <= self.current_level <= LEVELS
        0 <= self.current_exp
        """

        if self.WIN:
            messagebox.showinfo("Winner!", "You Won!")
            return True

        try:
            assert (1 <= self.current_level) and (self.current_level <= LEVELS)
            assert self.current_exp >= 0
        except AssertionError as e:
            messagebox.showerror("Assertions Failed", "Something went wrong, exiting program")
            self.root.destroy()

        increment = self.exp_increment()

        exp = self.current_exp + increment

        if exp >= LEVELS-1:
            exp = 0
            self.current_level += 1

        if self.current_level == LEVELS:
            self.WIN = True

        return exp

    def next_round(self):
        pass



# Show/Run our App
if __name__== "__main__":
    app = RandomWords()
    app.root.mainloop()
