# Write a class to hold player information, e.g. what room they are in
# currently.

# create a Player class, define constructor and string methods
class Player:
    def __init__(self, name, health, weapon, armor, current_room):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor
        self.current_room = current_room

    def __str__(self):
        return f'Player: {self.name}, {self.health}, {self.weapon}, {self.armor}, {self.current_room}'