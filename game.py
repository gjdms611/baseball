class Game:
    def guess(self, guessNumber):
        self.assert_illegal_value(guessNumber)

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

