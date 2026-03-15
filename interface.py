import os
import subprocess

from game_map import GameMap
from player import Player


INSTRUCTION = r"""
Type forward|left|right|back to move.
Type \quit to exit.
Type \restart to start again.
Type \clean to clear text.

"""


class Interface():
    def __init__(self):
        self.game_map = GameMap()
        self.player = Player()
        self.player.position = self.game_map.start_point
        self.instruction = INSTRUCTION
        self.player_input = None
        self.restart = False
        self.quit = False

    def is_exit_found(self):
        if self.player.position == self.game_map.finish_point:
            print("You found exit. YOU WIN!")
            return True
        return False

    def describe_surroundings(self):
        point = self.player.position
        surroundings = {
            "in front of": None,
            "left to": None,
            "right to": None,
            "behind": None
        }
        if point == self.game_map.start_point:
            surroundings["behind"] = "enter to the maze"
        elif point == self.game_map.finish_point:
            surroundings["in front of"] = "exit from the maze"
            return surroundings
        for key, value in surroundings.items():
            if not value:
                if key == "in front of":
                    symbol_point = [point[0]-1, point[1]]
                elif key == "left to":
                    symbol_point = [point[0], point[1]-1]
                elif key == "right to":
                    symbol_point = [point[0], point[1]+1]
                elif key == "behind":
                    symbol_point = [point[0]+1, point[1]]
                surroundings[key] = symbol_point
                symbol = self.game_map.get_symbol(symbol_point)
                if symbol == " ":
                    value = "corridor"
                elif symbol == "S":
                    value = "enter to maze"
                elif symbol == "F":
                    value = "exit from maze"
                elif symbol == "▓":
                    value = "wall"
            print(f"You see a {value} {key} you")
        return surroundings

    def get_input(self):
        self.player_input = input(self.instruction)

    def process_input(self):
        if self.player_input == r"\quit":
            print("You gave up! YOU LOSE!")
            self.quit = True
        elif self.player_input == r"\restart":
            print("You got lost and use teleport to start again!")
            self.restart = True
        elif self.player_input == r"\clean":
            self.clear_console()
        else:
            new_position = self.player.move(self.player_input)
            if new_position == self.player.position:
                print("Wrong input")
            if self.game_map.can_move(new_position):
                self.player.position = new_position
            else:
                print(f"Can't move {self.player_input}")

    def clear_console(self):
        command = 'cls' if os.name == 'nt' else 'clear'
        subprocess.run([command], shell=True)
