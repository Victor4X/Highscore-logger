from highscoreLogger import Logger

class main:

    def __init__(self):
        self.logger = Logger()

        print(self.logger.post_score("GH",0))


test = main()