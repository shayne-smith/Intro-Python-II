from room import Room
from player import Player
from item import Item

# Declare some items
twigs = Item("twigs", "a small bunch of broken twigs")

# Declare all the rooms and fill with items
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons",
                     [Item("rope", "a coil of rope"), twigs]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                    [Item("torch", "a bright light emanates from the torch"), Item("sword", "the incredible blade of Icyene")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                    [Item("pebbles", "small black pebbles"), twigs]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                    [Item("pickaxe", "a bronze pickaxe"), Item("shovel", "a bronze shovel")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                    [Item("gold", "shiny gold"), Item("silver", "shiny silver"), Item("rubies", "red light dances around the rubies"), Item("dragon_skin", "the strongest armor in the land"), Item("game_boy", "a mysterious device from the future")]),
}


# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
# p1 = Player('Shayne', 100, 'Sword', 'Bronze', room['outside'], ['bread'])
p1 = Player(room['outside'], [Item('sword', "the great sword of Saradomin")])

# counts how many moves the user makes
num_moves = 0

# List of possible directions that a player can travel
possible_directions = ['n', 's', 'e', 'w']

# Inventory commands
inv_commands = ['i', 'inventory']

# Pickup commands
pickup_commands = ['get', 'take']

# Write a loop that:
while True:

    if num_moves == 0:
        # prints header
        print()
        print('********************  Cave Adventure Game  ********************')

    # prints the current room name
    if p1.current_room:
        print(f'{p1.current_room}\n')

        # print room items
        if len(p1.current_room.items) != 0:
            print('The following items are visible:')
            for item in p1.current_room.items:
                print(f'{item}')
            print()

    # waits for user input and decides what to do
    # when input comes in, strip off whitespace, lowercase the input, and split it
    command = input('Which direction would you like to go? ').strip().lower().split()
    print()

    # check if command has 1 word
    if len(command) == 1:
        command = command[0][0] # extracts the first letter of command

    # check if command has 2 words and one of the pickup commands
    elif len(command) == 2 and command[0] in pickup_commands:
        requested_item = command[1] # store the request item in variable

        # iterate over room items with enumerate (allows access to index values)
        for index, item in enumerate(p1.current_room.items):

            # checks if the requested item is in the room
            if item.name == requested_item:

                # call on_take message, remove item from room, and add to inventory
                p1.current_room.items[index].on_take(item)
                p1.current_room.items.remove(item)
                p1.inventory.append(item)

    # check if command has 2 words and first word is 'drop'     
    elif len(command) == 2 and command[0] == 'drop':
        dropped_item = command[1] # store the request item in variable

        # iterate over room items with enumerate (allows access to index values)
        for index, item in enumerate(p1.inventory):

            # checks if the requested item is in Player's inventory
            if item.name == dropped_item:

                # call on_take message, remove item from inventory, and add to room
                p1.inventory[index].on_drop(item)
                p1.current_room.items.append(item)
                p1.inventory.remove(item) 

    # If the user enters "q", quit the game.
    if command == "q":
        break

    # check to see if we can go in that direction
        # if we can, go there
    if command in possible_directions:
        p1.try_direction(command)

    # print Player's inventory
    elif command in inv_commands:
        print("Current inventory:")
        for item in p1.inventory:
            print(f'*** {item}')
        print()

    num_moves += 1 # count Player moves
