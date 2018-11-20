from highscoreLogger import Logger

class main:

    def __init__(self):
        self.logger = Logger()

        print(self.logger.post_score("test",6969))

test = main()