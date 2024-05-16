import os


#class for Hangman playground representation
class Playground:

    def __init__(self, word):
        self.word = word
        self.lenght = len(word)
        self.incorrect = 0
        self.hangman = ['     \n' for _ in range(5)]
        self.guess_state = [' ' for _ in range(len(word))]

    #evaluating incorrect guess
    def incorrect_guess(self):
        self.incorrect += 1
        self.__eval_incorrect()
        print(f"Incorrect letter\nNumber of remaining attempts: {7-self.incorrect}")

    def __eval_incorrect(self):
        match self.incorrect:
            case 1:
                self.__gallows()
            case 2:
                self.__head()
            case 3:
                self.__body()
            case 4:
                self.__left_arm()
            case 5:
                self.__right_arm()
            case 6:
                self.__left_leg()
            case 7:
                self.__right_leg()

    def __gallows(self):
        string = [' ', '_', '_', '_', ' ', os.linesep, '|', ' ', ' ', ' ', '|', os.linesep, '|', ' ', ' ', ' ', ' ', os.linesep,
                  '|', ' ', ' ', ' ', ' ', os.linesep, '|', ' ', ' ', ' ', ' ', os.linesep, '|', ' ', ' ', ' ', ' ', os.linesep]
        self.hangman = string

    def __head(self):
        self.hangman[16] = 'O'

    def __body(self):
        self.hangman[22] = '|'

    def __left_arm(self):
        self.hangman.insert(23, '\\')

    def __right_arm(self):
        self.hangman[21] = '/'

    def __left_leg(self):
        self.hangman.insert(30, '\\')

    def __right_leg(self):
        self.hangman[28] = '/'

