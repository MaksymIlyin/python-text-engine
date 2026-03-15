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
        return [len(self.game_map)-1, self.game_map[-1].index("S")]

    def get_finish_point(self):
        return [0, self.game_map[0].index("F")]

    def get_symbol(self, point):
        return self.game_map[point[0]][point[1]]

    def can_move(self, point):
        symbol = self.get_symbol(point)
        if symbol != "▓":
            return True
        return False
