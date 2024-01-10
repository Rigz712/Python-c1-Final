#Joseph Huffer Project 2 Submission

# Part 1 -  Instructions: Explain the game rules, premise, and movement as well as item’s purpose.
def show_instructions():
 print('\n A Night with a Necromancer: a Text-Based Video Game\n')
 print('Rules: Collect all 6 Mythical Items scattered around the castle in order to take down the Necromancer!')
 print('For Move commands, Type: go North, go South, go East, Or go West')
 print('Add item to Inventory: get \'item name\' (Capitalization Matters)')
 print('You may end the game at any time by typing \'End Game\'')

#Part 2 -  Dictionary Elements: Create a dictionary for all rooms / items in map.
#Also changing Directions of N, S, E, &W to North, South, East, & West and I’m adding when it requests for movement inputs to request full direction not only beginning letter ( For Example the player will now type: “go North” and not just “N”).
#I originally split items and rooms into separate dict – I’m now combining rooms with items.
rooms = {
    'Spawn': {'North': 'Castle Gate'},
    'Castle Gate': {'North': 'Castle Courtyard', 'South': 'Spawn'},
    'Castle Courtyard': {'North': 'Main Hall', 'South': 'Castle Gate', 'East': 'Eastern Guardhouse', 'West': 'Western Guardhouse', 'item': 'Cuirass Of Ominous Vengeance'},
    'Eastern Guardhouse': {'West': 'Castle Courtyard', 'item': 'Timeworn Kite Shield'},
    'Western Guardhouse': {'East': 'Castle Courtyard', 'item': 'The Mace Of Fate'},
    'Main Hall': {'North': 'Cloister', 'South': 'Castle Courtyard', 'East': 'Hidden Corridor'},
    'Hidden Corridor': {'West': 'Main Hall', 'item': 'Phantom Scaled Belt'},
    'Cloister': {'East': 'Dungeon', 'West': 'Castle Halls', 'South': 'Main Hall', 'item': 'Blood Infused Padded Cloak'},
    'Library': {'East': 'Castle Halls', 'item': 'Helm Of Binding Sorrow'},
    'Castle Halls': {'East': 'Cloister', 'West': 'Library'},
    'Dungeon': {'West': 'Cloister', 'item': 'Necromancer'},
}

# Original Item Statments * * Comments with Strikes through them are items I am removing for the final submission for project 2.
# items =
# STRIKE {"Castle Gate": "Health Potion",
#"Castle Courtyard": "Cuirass of Ominous Vengeance",
 # ITEM STATEMENT + THIS INTO DICTIONARY ABOVE -->       , 'item': 'Cuirass of Ominous Vengeance'
# STRIKE "Main Hall": "Another Health Potion",
# STRIKE "Castle Halls": "Another Health Potion",
#"Eastern Guardhouse": "Timeworn Kite Shield",
# ITEM STATEMENT + THIS INTO DICTIONARY ABOVE -->       , "item": "Timeworn Kite Shield"
#"Western Guardhouse": "The Mace of Fate",
# ITEM STATEMENT + THIS INTO DICTIONARY ABOVE -->       , "item": "The Mace of Fate"
#"Hidden Corridor": "Phantom Scaled Belt",
# ITEM STATEMENT + THIS INTO DICTIONARY ABOVE -->       , "item": "Phantom Scaled Belt"
#"Cloister": "Blood Infused Padded Cloak",
# ITEM STATEMENT + THIS INTO DICTIONARY ABOVE -->       , "item": "Blood Infused Padded Cloak"
#"Library": "Helm of Binding Sorrow",
# ITEM STATEMENT + THIS INTO DICTIONARY ABOVE -->       , "item": "Helm of Binding Sorrow"
    #Funny work around, my code will still prompt for an item each room so I added the following note 'no more items left...
    #UPDATE* Reworking this section see later if statement' - will now be -->  , "item": "Necromancer!"
#STRIKE "Dungeon": "No more items left to acquire!  You have reached the lair of the Necromancer!  Prepare yourself."}

#Changing 'you are now in' to 'you are at the' current_room.
def player_stats():
 global current_room
 global inventory
 print('_' * 20)
 print('You are at the {}'.format(current_room))
 print('Inventory: ' + str(inventory))
 if 'item' in rooms[current_room]:
    print('You see ' + rooms[current_room]['item'])
 print('_' * 20)

global current_room
current_room = 'Spawn'
global inventory
inventory = []
show_instructions()

#Gameplay Loop - changing N,E,S, and W to go North, 'go East', 'go South', 'go East' and 'go West' - I feel like 'what would you like to do' needed that player saying 'go' somewhere.
def main():
 global current_room
 global inventory
 player_stats()
 player_move = ''
 while player_move == '':
    player_move = input('What would you like to do:\n').title()
 if player_move == 'Go North' or player_move == 'Go South' or player_move == 'Go East' or player_move == 'Go West':
    player_move = player_move[3:]
    if player_move not in rooms[current_room]:
        print('\nSorry, no path in that direction!')
    else:
        current_room = rooms[current_room][player_move]
 elif player_move[0:3] == 'Get':
      if 'item' not in rooms[current_room] or player_move[4:] not in rooms[current_room]['item']:
        print('Can\'t get {}!'.format(player_move[4:]))
      else:
        inventory += [player_move[4:]]
        print('Congratulations! You have acquired:', player_move[4:])
        del rooms[current_room]['item']

#If you have not acquired enough items, you lose
 if len(inventory) < 3 and current_room == 'Dungeon':
    print('Oh no! You have entered the Dungeon and the Necromancer has spotted you!')
    print('You failed to collect enough of the mythical items required to face the Necromancer and died.')
    print('GAME OVER! Better luck next time!')
    exit(0)
#If you have Acquired enough Items, you win
 if len(inventory) >= 4 and current_room == 'Dungeon':
    print('\nCongratulations! You collected the mythical items required to defeat the Necromancer!')
    exit(0)

#Part 5c: Quit or Exit Movement Command – Self Explanatory, Player can type “Quit’ or ‘ Exit’  or ‘End Game’ as a movement to exit the program/game.
 if player_move == 'End Game':
    print('Play again soon!')
    exit(0)

#Loop Forever
while True:
    main()