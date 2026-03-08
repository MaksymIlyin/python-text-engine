from engine import Game

def main():
    game = Game()
    while game.is_running:
        game.run()
    exit()


if __name__ == "__main__":
    main()
