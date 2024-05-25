


class Dinorunnergame:
    def __init__(self):
        print("initial constructors")

    def startgame(self):
        print("game starts")

    def endgame(self):
        print("game ends")

    def reset(self):
        print("game resets")


class Player(Dinorunnergame):
    def __init__(self):
        self._mydisplay = LCDDisplay(sda=0, scl=1, i2cid=0)

    def testDisplay(self):
        self._mydisplay.showText("game starts")
        self._mydisplay.addShape(0,[0x15,0x0A,0x04,0x04,0x0E,0x11,0x0A,0x15])
        self._mydisplay.showText(f"   {chr(0)}  {chr(0)}", row=1, col=0)  

    def jump(self):

    def duck(self):

    def start(self, name):  