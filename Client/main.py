from highscoreLogger import Logger

#EKSEMPEL

class main:

    def __init__(self):
        self.logger = Logger()

        #def post_score(self,game,score,opt1="n/a",opt2="n/a",opt3="n/a"):
        #"game" er spillet (String)
        #"score" er scoren (Int)
        #"opt1-3" er valgfrie strings til scoren (String)
        self.logger.post_score("TestGame",420,"Victor")

        #def get_scores(self,game):
        #Returnerer en liste af dictionaries med formatet {Game:String,Score:Integer,Opt1:String,Opt2:String,Opt3:String}
        for s in self.logger.get_scores("TestGame"):
            print(s["Score"],s["Opt1"])

        #Dette printer alle [Score]s og medfølgende [Opt1] for spillet "TestGame", hvor Scoren er 420 og Opt1 er brugt til navnet "Victor"


test = main()