import os


class Ellie(object):
    def __init__(self) -> None:
        self.name = 'Ellie'
        self.version = 2
        self.run = True
        self.last_c = ''

    def cmd(self):
        while self.run:
            command = input("~e> ")
            if command == 'stop':
                self.last_c = command
                self.run = False


e = Ellie().cmd()