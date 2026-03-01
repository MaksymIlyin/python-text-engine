class Player:
    def __init__(self):
        self.position = None

    def move(self, direction):
        new_position = self.position
        if direction == "forward":
            new_position = [self.position[0]-1, self.position[1]]
        elif direction == "left":
            new_position = [self.position[0], self.position[1]-1]
        elif direction == "right":
            new_position = [self.position[0], self.position[1]+1]
        elif direction == "back":
            new_position = [self.position[0]+1, self.position[1]]
        return new_position
