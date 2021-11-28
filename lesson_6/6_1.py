import time


class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'


class TrafficLight:
    __color = {"red": [7, bcolors.RED], "yellow": [2, bcolors.YELLOW], "green": [5, bcolors.GREEN]}

    def __init__(self):
        pass

    def running(self):
        while True:
            for c, t in TrafficLight.__color.items():
                print(f"{t[1]}{c}{bcolors.ENDC}")
                time.sleep(t[0])


tl = TrafficLight()
tl.running()
