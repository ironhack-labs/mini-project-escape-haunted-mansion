from classes import Room, Item, Player # entities for the game

import random # random library to get random npc
import time # time library for the final delay

def setup_rooms() -> dict:
    """
    Initialize the rooms dictionary
    Return:
        rooms (dict): A dictionary with all rooms information
    """        
    # Define rooms
    rooms = {
        'Foyer': Room('Foyer', 'A dimly lit entrance hall with a grand staircase.', 
                      ['Library', 'Dining Room', 'Main Gate']),
        'Library': Room('Library', 'Walls lined with ancient books. A cold draft chills you.', 
                        ['Foyer', 'Study'], ['Study Key'], locked=True),
        'Dining Room': Room('Dining Room', 'A grand room with a long table. A chandelier swings gently.', 
                            ['Foyer', 'Kitchen']),
        'Kitchen': Room('Kitchen', 'Smells of stale food and rusted utensils abound.', 
                        ['Dining Room', 'Basement'], ['Flashlight', 'Library Key']),
        'Basement': Room('Basement', 'A damp, dark space with creaking floorboards.', 
                         ['Kitchen'],['Main Gate Key'], locked=True),
        'Attic': Room('Attic', 'Filled with cobwebs and old trunks. A strange aura pervades.', 
                      ['Study'],['Basement Key']),
        'Study': Room('Study', 'A cozy room with a crackling fireplace and a locked desk.', 
                      ['Library', 'Attic'], locked=True),
        'Main Gate': Room('Main Gate', 'The Haunted Mansion Main Gate!!', ['FREEDOM'], locked=True)
    }
    return rooms

def setup_npcs_characters() -> dict:
    """
    Initialize the npcs dictionary
    Return:
        npcs (dict): A dictionary with npc characters information, classified by risk
    """    
    # Define characters
    npcs = {
        "low": {
            "Whisperer": {
                "description": "An incorporeal shadow that whispers unintelligible words into your ears.",
                "behavior": "Appear and whispers randomly, causing you distraction.",
            },
            "Laughing Girl": {
                "description": "A young girl in an old-fashioned dress laughs and vanishes in dark hallways.",
                "behavior": "Runs in from of you, leaving echoes of laughter and vanishes.",
            },
            "Living Clock": {
                "description": "A grandfather clock that chimes incorrect hours while being watched.",
                "behavior": "Change the time back and play a bell.",
            }
        },
        "medium": {
            "Disfigured Butler": {
                "description": "A man with a partially burned face holding a rusty serving tray.",
                "behavior": "Walks slowly toward you, murmuring 'Dinner is served.'",
            },
            "Shadow Ballerina": {
                "description": "A spectral figure that dances lit by candles.",
                "behavior": "Stops dancing when approached closely, briefly transforming into a terrifying figure.",
            }
        },
        "high": {
            "Soul Jailer": {
                "description": "A large chained spirit with burning eyes.",
                "behavior": "Pulls you toward its area with chains emerging from the ground, but you escape.",
            },
            "Cursed Chief": {
                "description": "A blood-soaked chief with rusty knife.",
                "behavior": "Stealthily stalks and launches surprise attacks, but you escape.",
            }
        }
    }    
    return npcs

def is_npc_character_inside(npcs_classified):
    """
    Search a random npc character
    Args:
        npcs_classified (dict): A npc dictionary of characters
    Return:
        npc_character (str): Details about the npc character
    """
    npc_danger_key = random.choice(list(npcs_classified))            
    npc_key = random.choice(list(npcs_classified[npc_danger_key]))
    npc_character_details = f"You see a {npc_key} ... {npcs_classified[npc_danger_key][npc_key]['description']}\n"
    npc_character_details += f"   {npcs_classified[npc_danger_key][npc_key]['behavior']}\n"
    npc_character_details += f"   It's a {npc_danger_key.upper()} risk situation for you!!\n"    
    
    return npc_character_details

def start_game():
    """
    Start the game until the user type "quit"
    Args:
        nothing
    Return:
        nothing
    """    
    rooms = setup_rooms()
    npcs_classified = setup_npcs_characters()
    
    player = Player(rooms['Foyer'])
    
    print("\nO: Welcome to 'Escape from the Haunted Mansion'! :O")
    print("   Commands: 'rooms', 'am', 'items', 'go to <room>', 'move to <room>', 'pick up <item>', 'use <item>', inventory, or quit.\n")    
    print(player.current_room.describe())
    
    while True:
        command = input("\nWhat will you do? ").strip().lower()
        if command.startswith("go to") or command.startswith("move to"):
            _, _, room_name = command.partition("to ") # get only the room_name part from the command string
            
            move_action_message = player.move(room_name.title(), rooms)
            print(move_action_message)
            
            if 'You moved to the' in move_action_message: # if new room, describe the room
                print(player.current_room.describe())

            if "FREEDOM" in player.current_room.connections:
                print(f"\n\nYou survive at this ocassion...\n");
                time.sleep(2)
                print(f"But ...");
                time.sleep(3)
                print(f"\n\n👻 😱 👻 😱 👻  WHATCH YOU BACK!!  👻 😱 👻 😱 👻\n\n\n");
                break

            if player.current_room.name == room_name.title(): # enter to new room
                print(is_npc_character_inside(npcs_classified))                
        elif command.startswith("pick up"):
            _, _, item_name = command.partition("up ") # get only the item_name part from the command string
            print(player.pick_up_item(item_name.title()))
        elif command.startswith("use"):
            _, _, item_name = command.partition("use ") # get only the item_name part from the command string
            item_name = item_name.title()
            is_used = player.use_item(item_name)
            if is_used:
                print(f"You used {item_name}.")
                if 'Key' in item_name:
                    locked_room = item_name.split("Key")[0].strip() 
                    if locked_room in player.current_room.connections: # check if is the correct room key
                        if rooms[locked_room].is_locked():               
                            rooms[locked_room].unlock()
                            print(f"You unlock the {locked_room} room. Now, move to inside...at your risk!")
                        else:
                            print(f"The {locked_room} room is not locked any more.!")
                    else:
                        print(f"You can not use the {locked_room} Key here!")                        
            else:
                print(f"You don't have {item_name} in your inventory.")
        elif command == "items":
            print(f"  Items in {player.current_room.name}: {', '.join(player.current_room.items) if player.current_room.items else 'Nothing inside'}")
        elif command == "inventory":            
            print(f"  Your inventory: {', '.join(player.inventory) if player.inventory else 'Nothing'}")
        elif command == "rooms":
            print(f"  Rooms: {', '.join(room for room in rooms)}")
        elif command == "am":
            print(player.current_room.describe())            
        elif command == "quit":
            print("\n** Thanks for playing! **\n")
            break
        else:
            print("\n** Invalid command.")
            print("   Try 'rooms', 'am', 'items', 'go to <room>', 'move to <room>', 'pick up <item>', 'use <item>', inventory, or quit.")

if __name__ == "__main__":
    start_game()