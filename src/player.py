# Write a class to hold player information, e.g. what room they are in
# currently.

# Create a Player class, define constructor and string methods
# Add attributes for name, health, weapon, armor, current_room
class Player:
    def __init__(self, current_room, inventory):
        self.current_room = current_room
        self.inventory = inventory

    def __str__(self):
        return f'Current layer current_room: {self.current_room}'

    # print inventory
    def print_inventory(self):
        for index, inv in enumerate(self.inventory):
            print(f"{index+1} - {inv}")

    def try_direction(self, command):
        attribute = command + '_to'

        # see if the current room has the attribute
        # we can use a Python function called 'hasattr'
        if hasattr(self.current_room, attribute):
            # use 'getattr' to actually move to the room
            self.current_room = getattr(self.current_room, attribute)
        else:
            print("You can't go that way!")
            print()