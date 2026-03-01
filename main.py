from game_map import GameMap
from player import Player

INSTRUCTION = r"""
Type forward|left|right|back to move.
Type \q to exit.
"""


def main():
    resp = input(r"Type \start to start the game: ")
    if resp == r"\start":
        game_map = GameMap()
        player = Player()
        player.position = game_map.start_point
        while True:
            game_map.describe_surroundings(player.position)
            if player.position == game_map.finish_point:
                print("You WIN!")
                exit()
            print(INSTRUCTION)
            resp = input()
            new_position = player.move(resp)
            if new_position == player.position:
                print("Wrong input")
            if game_map.can_move(new_position):
                player.position = new_position
            else:
                print(f"Can't move {resp}")
            if resp == r"\q":
                break
    print("END")
    exit()


if __name__ == "__main__":
    main()

