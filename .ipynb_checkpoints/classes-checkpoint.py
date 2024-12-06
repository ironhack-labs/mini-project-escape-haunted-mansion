# Room Class
class Room:
    def __init__(self, name, description, connections, items=None, locked=False):
        """
        Initialize each room attributes
        Args:
            name (str): The room name.
            description (str): The room description.
            connections (list): The room connections to others rooms.
            items (list): The items inside the room.
            locked (bool): If rooms is locked (True or False).
        """
        self.name = name
        self.description = description
        self.connections = [] or connections # Connected rooms
        self.items = [] or items # Items inside the room
        self.locked = locked # If the room is locked

    def describe(self):
        """
        Initialize each room attributes
        Args:
            name (str): The room name.
            description (str): The room description.
            connections (list): The room connections to others rooms.
            items (list): The items inside the room.
            locked (bool): If rooms is locked (True or False).
        Returns:
            (str): A message with the current room information.
        """        
        return f"\nThe {self.name} is {self.description}\n   It's connected to: {', '.join(self.connections)}"

    def get_connetions(self):
        """
        Check if the room has connection to others rooms.
        Returns:
            (list): Return the a string list with the rooms names connected to current room.
        """           
        return self.connections

    def is_locked(self):
        """
        Check if the room is locked or not.
        Returns:
            (bool): True if room is locked, False if not.
        """           
        return self.locked
    
    def unlock(self):
        """
        Unlock the room, set locked property to false.
        """        
        self.locked = False

# Item Class
class Item:    
    def __init__(self, name, description, item_type):
        """
        Initialize each item attributes
        Args:
            name (str): The item name.
            description (str): The item description.
            item_type (str): The item type.
        """        
        self.name = name
        self.description = description
        self.item_type = item_type

    def use(self):
        """
        Simulate the action of move inside a room. Check if is locked.
        Returns:
            (str) : Return a message with the item used.
        """
        return f"\nYou used the {self.name}."

# Player Class
class Player:
    def __init__(self, current_room, inventory=[]):
        """
        Initialize the Player attributes to use inside the game.
        Args:
            current_room (obj): A player current room.
            inventory (obj list): A list of items that user get in his way.
        """            
        self.current_room = current_room
        self.inventory = inventory
        
    def move(self, room_name, rooms):
        """
        Simulate the action of move inside a room. Check if is locked.
        Args:
            room_name (str): The new room to enter.
            rooms (obj list): A list of posible rooms.
        Returns:
            (str): A message indicating if the player move inside the room or not.            
        """              
        if room_name in self.current_room.connections: # check if the new rooms is connected
            current_room = rooms[room_name]
            if current_room.is_locked(): # check if the new rooms is locked to enter
                return f"\nThe {room_name} is locked. You need a key to enter."
            self.current_room = current_room # set the new room if possible
            return f"\nYou moved to the {room_name}."
        return f"\nYou can't go to {room_name} from here."
    
    def pick_up_item(self, item_name):
        """
        Simulate the action of pick up an item inside a room. 
        Args:
            item_name (str): The item name to pick up.
        Returns:
            (str): A message indicating if the player pick up or not the item.
        """               
        if self.current_room.items: # Check if the room has items
            if item_name in self.current_room.items: # Check if the item is available
                self.inventory.append(item_name) # append the new item to player inventory
                self.current_room.items.remove(item_name) # remove the item from the room
                return f"\nYou picked up {item_name}."
        return f"\n{item_name} is not in this room."

    def use_item(self, item_name):
        """
        Check if the user have the item in inventory to use. 
        Returns:
            item_name (str): The item name to use.
        """                  
        return item_name in self.inventory






















