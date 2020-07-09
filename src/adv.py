from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     ["rope", "twigs"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                    ["torch", "sword"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                    ["pebbles", "twigs"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                    ["pickaxe", "shovel"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                    ["gold", "silver", "rubies", "dragon_skin", "game_boy"]),
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
p1 = Player(room['outside'], ['sword'])

# counts how many moves the user makes
num_moves = 0

# List of possible directions that a player can travel
possible_directions = ['n', 's', 'e', 'w']

# Inventory commands
inv_commands = ['i', 'inventory']

# Action commands
action_commands = ['get', 'take']

# Write a loop that:
while True:

    if num_moves == 0:
        # prints header
        print()
        print('********************  Cave Adventure Game  ********************')

    # prints the current room name
    if p1.current_room:
        print(f'{p1.current_room}\n')

        if len(p1.current_room.items) != 0:
            print('The following items are visible:')
            for item in p1.current_room.items:
                print(f'{item}')
            print()

    # prints the current description (the textwrap module might be useful here).

    # waits for user input and decides what to do
    # when input comes in, strip off whitespace, lowercase the input, and split it
    command = input('Which direction would you like to go? ').strip().lower().split()
    print()

    # check if command has 1 or 2 words
    if len(command) == 1:
        command = command[0][0] # extracts the first letter of command
    elif len(command) == 2 and command[0] in action_commands:
        print("action command")
        requested_item = command[1]
        for item in p1.current_room.items:
            if item == requested_item:
                p1.current_room.items.remove(requested_item)
                p1.inventory.append(requested_item)
        

    # If the user enters a cardinal direction, attempt to move to the room there.
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
            print(f'{item}')
        print()

    num_moves += 1
    #
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.
