import websockets as ws
import asyncio
import json

class Handler:

    def __init__(self):
        pass

    async def sUpdate(self,game,score,opt1,opt2,opt3):
        async with ws.connect('ws://pygame-online-service.herokuapp.com/db') as websocket:

            dump = {'Game':str(game),'Score':int(score),'Opt1':str(Opt1),'Opt2':str(Opt2),'Opt3':str(Opt3)}
            await websocket.send(json.dumps(dump))
            print(f"> added dots {json.dumps(dump)}")

            greeting = await websocket.recv()

            return eval(greeting)

    def update(self,game,score,opt1="n/a",opt2="n/a",opt3="n/a"):
        response = asyncio.get_event_loop().run_until_complete(self.sUpdate())
        return response
