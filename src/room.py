# Implement a class to hold room information. This should have name and
# description attributes.

# Create a room class, define constructor and string methods
# Add attributes for name and room description
class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        return f'Room: {self.name}, {self.description}'

    def print_items(self):
        for index, item in enumerate(self.items):
            print(f'{index+1} - {item}')