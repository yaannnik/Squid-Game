import random

class Player:
    def __init__(self, number):
        self.num = number

    def makePrediction(self):
        prediction = random.randint(0, 1)
        return prediction%2
    
    def makePredictionImmersedMode(self, num):
        i = input("Player #%d please make your prediction [0(default)/1]: " % num)
        prediction = 1 if i == '1' else 0
        return prediction%2

    def playGame(self, bridge, start_point):
        N = len(bridge.steps)

        print("Player #%d starts at step %d" % (self.num, start_point+1))
        
        for _ in range(start_point, N):
            pred = self.makePrediction()
            print("Player #%d made prediction %d at step %d. The true value is %d" % (self.num, pred, _+1, bridge.steps[_]))
            if(pred != bridge.steps[_]):
                print("Player #%d died at step %d\n" % (self.num, _+1))
                return _
        
        print("Player #%d wins this game" % self.num)
        return -1

    def playGameImmersedMode(self, bridge, start_point):
        N = len(bridge.steps)

        print("Player #%d starts at step %d" % (self.num, start_point+1))
        
        for _ in range(start_point, N):
            pred = self.makePredictionImmersedMode(self.num)
            print("Player #%d made prediction %d at step %d. The true value is %d" % (self.num, pred, _+1, bridge.steps[_]))
            if(pred != bridge.steps[_]):
                print("Player #%d died at step %d\n" % (self.num, _+1))
                return _
        
        print("Player #%d wins this game" % self.num)
        return -1