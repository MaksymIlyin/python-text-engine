from game_map import GameMap
from player import Player


INSTRUCTION = r"""
Type forward|left|right|back to move.
Type \q to exit.
"""

class Game:
    def __init__(self):
        self.game_map = GameMap()
        self.player = Player()
        self.player.position = self.game_map.start_point
        self.is_running = True

    def run(self):
        self.game_map.describe_surroundings(self.player.position)
        if self.is_exit_found():
            print("You found exit. YOU WIN!")
            self.is_running = False
        else:
            print(INSTRUCTION)
            resp = input()
            if resp == r"\q":
                print("You gave up! YOU LOSE!")
                self.is_running = False
            else:
                new_position = self.player.move(resp)
                if new_position == self.player.position:
                    print("Wrong input")
                if self.game_map.can_move(new_position):
                    self.player.position = new_position
                else:
                    print(f"Can't move {resp}")

    def is_exit_found(self):
        if self.player.position == self.game_map.finish_point:
            return True
        return False
