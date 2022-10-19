from invalidassignmentexception import InvalidAssignmentException


class Hangman():
    def __init__(self):
        self.lifes = 5
        self.resolved_word = ''
        self.word = ''

    def set_word(self, word):
        self.resolved_word = word.lower()
        for i in self.resolved_word:
            self.word += '_ '
    def play(self):
        while True:
            print(self.show())
            try:
                self.assign(input('Ingrese una letra '))
            except InvalidAssignmentException:
                print("Invalid Letter. Try again")
            if self.winner():
                return 'Ganaste'
            if self.lifes < 1:
                return 'Perdiste'

    def assign(self, letter):
        letter = letter.lower()
        tempList = list(self.word)
        tempList_result = list(self.resolved_word)
        for index, letter_in_resolved_word in enumerate(self.resolved_word):
            if letter not in self.resolved_word:
                self.lifes -= 1
            if letter in self.word or letter not in self.resolved_word:
                raise InvalidAssignmentException()
            if letter == tempList_result[index]:
                tempList[index*2] = (letter)
        self.word = "".join(tempList)

    def winner(self):
        return list(self.resolved_word) == self.word.split()

    def show(self):
        return (f'Lifes: {self.lifes} - Word: {self.word}')
