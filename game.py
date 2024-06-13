from game_result import GameResult


class Game:
    def __init__(self):
        super().__init__()
        self.question = ""

    def guess(self, guessNumber):
        self.assert_illegal_value(guessNumber)
        if self.is_solved(guessNumber):
            return self.get_success_game_result()
        else:
            return self.get_unsolved_game_result(guessNumber)

    def get_unsolved_game_result(self, guessNumber):
        strikes = 0
        balls = 0
        for idx, char in enumerate(self.question):
            if guessNumber.find(char) == idx:
                strikes += 1
            elif char in guessNumber:
                balls += 1
        return GameResult(False, strikes, balls)

    def get_success_game_result(self):
        return GameResult(True, 3, 0)

    def is_solved(self, guessNumber):
        return self.question == guessNumber

    def assert_illegal_value(self, guessNumber):
        if guessNumber is None:
            raise TypeError()
        if len(guessNumber) != 3:
            raise TypeError()
        try:
            int(guessNumber)
        except ValueError as e:
            raise TypeError()
        if self.isDuplicatedNumber(guessNumber):
            raise TypeError()

    def isDuplicatedNumber(self, guessNumber):
        return len(guessNumber) != len(set(guessNumber))
