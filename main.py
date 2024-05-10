class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        """ Attack another hero, decreasing their health by the attack power. """
        other.health -= self.attack_power

    def is_alive(self):
        """ Check if the hero is still alive. """
        return self.health > 0


class Game:
    def __init__(self, player_name, computer_name="Computer"):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        """ Start the game and continue rounds until one hero dies. """
        round = 1
        while self.player.is_alive() and self.computer.is_alive():
            # Player's turn
            print(f"Round {round}: {self.player.name}'s turn.")
            self.player.attack(self.computer)
            print(f"{self.player.name} attacks! {self.computer.name} has {self.computer.health} health left.")

            # Check if the computer is still alive
            if not self.computer.is_alive():
                print(f"{self.player.name} wins!")
                break

            # Computer's turn
            print(f"Round {round}: {self.computer.name}'s turn.")
            self.computer.attack(self.player)
            print(f"{self.computer.name} attacks! {self.player.name} has {self.player.health} health left.")

            # Check if the player is still alive
            if not self.player.is_alive():
                print(f"{self.computer.name} wins!")
                break

            round += 1


# Example of how to use the game
game = Game("Player")
game.start()
