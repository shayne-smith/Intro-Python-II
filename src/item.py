# Write a class to hold item information, e.g. name and description
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}: {self.description}'

    def print_name(self):
        print(f'{self.name}')

    def on_take(self, item):
        print(f"You have picked up {item}")