from Bridge import Bridge
from Player import Player
import os

N = 10

if __name__ == "__main__":
    os.system("clear")

    i = input("Do you want to play your game in Immersed Mode [y/n]: ")
    mode = True if i == 'y' else False

    bridge = Bridge(N)
    if mode == False:
        bridge.showSteps()
        bridge.showGraph()

    num = 0
    start_point = 0
    stop_point = 0
    
    while stop_point != -1:
        num += 1
        player = Player(num)
        
        if mode:
            stop_point = player.playGameImmersedMode(bridge, start_point)
        else:
            stop_point = player.playGame(bridge, start_point)

        start_point = stop_point + 1

        if(start_point == N):
            print("The game is over")
            break