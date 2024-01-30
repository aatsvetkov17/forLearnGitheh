import os


class Ellie(object):
    def __init__(self) -> None:
        self.name = 'Ellie'
        self.version = 2
        self.run = True

    def cmd(self):
        while self.run:
            command = input("~e> ")
            if command == 'stop':
                self.run = False
        
e = Ellie().cmd()