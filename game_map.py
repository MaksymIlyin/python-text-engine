class GameMap:
    def __init__(self):
        self.game_map = self.create_map()
        self.start_point = self.get_start_point()
        self.finish_point = self.get_finish_point()

    def create_map(self):
        game_map = []
        with open("./map.txt", "r") as file:
            data = file.read()
        rows = data.split("\n")
        game_map = [list(row) for row in rows[:-1]]
        return game_map

    def get_start_point(self):
        return [len(self.game_map)-1, self.game_map[-1].index("$")]

    def get_finish_point(self):
        return [0, self.game_map[0].index("×")]

    def get_symbol(self, point):
        return self.game_map[point[0]][point[1]]


    def describe_surroundings(self, point: list[int]):
        surroundings = {
            "in front of": None,
            "left to": None,
            "right to": None,
            "behind": None
        }
        if point == self.start_point:
            surroundings["behind"] = "enter to the maze"
        elif point == self.finish_point:
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
                symbol = self.get_symbol(symbol_point)
                if symbol == " ":
                    value = "corridor"
                elif symbol == "$":
                    value = "enter to dungeon"
                elif symbol == "×":
                    value = "exit from dungeon"
                elif symbol == "▓":
                    value = "wall"
            print(f"You see a {value} {key} you")
        return surroundings

    def can_move(self, point):
        symbol = self.get_symbol(point)
        if symbol != "▓":
            return True
        return False
