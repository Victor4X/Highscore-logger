from serverHandler import Handler

class Logger:
    
    def __init__(self):
        self.handler = Handler
    
    def post_score(self,game,score,opt1="n/a",opt2="n/a",opt3="n/a"):
        #Poster score til game
        #Returnerer liste af scores til game
        scores = self.handler.update(game,score,opt1,opt2,opt3)
        templist = []
        for s in scores:
            if s["Game"] == str(game):
                templist.append(s)
        
        return templist
            

    def get_scores(self,game):
        #Poster score til game
        #Returnerer liste af scores til game
        scores = self.handler.update("get",0,"n/a","n/a","n/a")
        templist = []
        for s in scores:
            if s["Game"] == str(game):
                templist.append(s)

        return templist

