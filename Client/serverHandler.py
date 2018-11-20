import websockets as ws
import asyncio
import json

class Handler:

    def __init__(self):
        pass

    async def sUpdate(self,game,score,opt1,opt2,opt3):
        async with ws.connect('ws://highscore-logger.herokuapp.com/db') as websocket:

            if game != "get":
                dump = {'Game':str(game),'Score':int(score),'Opt1':str(opt1),'Opt2':str(opt2),'opt3':str(opt3)}
                await websocket.send(json.dumps(dump))
                print(f"> added score {json.dumps(dump)}")

            else:
                await websocket.send("get")
                print("got scores")

            greeting = await websocket.recv()

            return eval(greeting)

    def update(self,game,score,opt1="n/a",opt2="n/a",opt3="n/a"):
        response = asyncio.get_event_loop().run_until_complete(self.sUpdate(game,score,opt1,opt2,opt3))
        return response
