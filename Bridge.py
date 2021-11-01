import random

class Bridge:
    def __init__(self, N):
        self.steps = []
        self.steps_graph = ""

        graphs = ["-[⭕️]-[❌]-", "-[❌]-[⭕️]-"]

        for _ in range(N):
            step = random.randint(0, 1)
            self.steps.append(step%2)
            self.steps_graph += graphs[step%2]
    
    def showSteps(self):
        print("Show the step result:\n", self.steps)

    def showGraph(self):
        print("Show the bridge:\n%s" % self.steps_graph)