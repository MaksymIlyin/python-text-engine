from interface import Interface


class Game:
    def __init__(self):
        self.interface = Interface()
        self.is_running = True

    def run(self):
        if self.interface.is_exit_found():
            self.is_running = False
        else:
            self.interface.describe_surroundings()
            self.interface.get_input()
            self.interface.process_input()
            if self.interface.restart:
                self.__init__()
            if self.interface.quit:
                self.is_running = False
