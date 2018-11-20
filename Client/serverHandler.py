import websockets as ws
import asyncio
import json

class Handler:

    def __init__(self):
        pass

    async def sUpdate(self,dotlist):
        async with ws.connect('ws://pygame-online-service.herokuapp.com/db') as websocket:
            
            templist = []
            if len(dotlist) != 0:
                for d in dotlist:
                    templist.append({'x':d[1][0],'y':d[1][1],'color':d[0]})
                await websocket.send(json.dumps(templist))
                print(f"> added dots {json.dumps(templist)}")
            else: 
                await websocket.send("get")
                print(f"> get")

            greeting = await websocket.recv()
            #print(f"< {greeting}")
            return eval(greeting)

    def update(self,dotlist):
        response = asyncio.get_event_loop().run_until_complete(self.sUpdate(dotlist))
        return response
