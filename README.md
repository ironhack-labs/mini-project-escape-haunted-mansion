![logo_ironhack_blue 7](https://user-images.githubusercontent.com/23629340/40541063-a07a0a8a-601a-11e8-91b5-2f13e4e6b441.png)

# Mini Project (Extra) | Escape from the Haunted Mansion

## Overview

In this project, you will develop a text-based adventure game called “Escape from the Haunted Mansion.” The game involves navigating through a mysterious mansion filled with puzzles, locked doors, hidden items, and eerie characters. Your objective is to find the keys to unlock the main gate and escape before time runs out.

This project will help you apply Python concepts such as lists, dictionaries, sets, functions, loops, and object-oriented programming in a practical and engaging way.

## Project Goals
 - Implement a structured game flow using Python programming constructs.
 - Utilize object-oriented programming to model game entities like rooms, items, and characters.
 - Apply control structures like loops and conditionals to manage game logic.
 - Enhance problem-solving skills by creating puzzles and challenges within the game.

## Game Structure

### Storyline

You find yourself trapped inside a haunted mansion on a stormy night. The main gate is locked, and the only way to escape is by finding the hidden keys scattered throughout the mansion. Along the way, you’ll encounter mysterious characters, solve puzzles, and collect items that will aid in your escape.

### Game Objectives
 - Explore Rooms: Navigate through different rooms in the mansion.
 - Collect Keys: Find all the hidden keys required to unlock the main gate.
 - Solve Puzzles: Overcome obstacles and challenges to access new areas.
 - Escape: Unlock the main gate and exit the mansion before time runs out or other in-game conditions occur.

### Tasks
1. Set Up the Game Environment

	- Define Rooms: Create a predefined set of rooms such as the Foyer, Library, Dining Room, Kitchen, Basement, and Attic.
	- Each room should have:
		- A name
 		- A description
 		- Connections to other rooms (e.g., the Foyer connects to the Library and Dining Room)
 		- Map Layout: Use dictionaries to map out the connections between rooms.

```
EXAMPLE: 

rooms = {
    'Foyer': {'description': 'A dimly lit entrance hall with a grand staircase.', 'connections': ['Library', 'Dining Room']},
    'Library': {'description': 'Walls lined with ancient books. A cold draft chills you.', 'connections': ['Foyer', 'Study']},
    # Add other rooms similarly
}
```
2. Implement Player Movement
 	- Create Movement Functions: Write functions that allow the player to move between connected rooms.
	- Validate moves to ensure the player can only go to rooms that are directly connected.
	- User Input: Prompt the player for commands like “go to Library” or “move to Dining Room.”
	- Current Location: Keep track of the player’s current room.

3. Introduce Items and Inventory
 	- Define Items: Place items in specific rooms.
	- Items include keys, clues, and tools.
	- Collect Items: Allow the player to pick up items and add them to their inventory.
	- Use a list or set to manage the inventory.
	- Use Items: Implement functionality for the player to use items from their inventory to solve puzzles or unlock doors.
```
EXAMPLE:
inventory = set()
items = {
    'Library': ['Silver Key'],
    'Kitchen': ['Flashlight'],
    # Other items in other rooms
} 
```

4. Create Puzzles and Challenges
	- Locked Doors: Some rooms are locked and require a key to enter.
	- Implement logic to check the player’s inventory for the correct key.
	- Riddles and Codes: Introduce simple puzzles that the player must solve to proceed.
		- Example: A code lock that requires solving a math puzzle.
	- Obstacles: Include obstacles like a broken staircase that requires a tool to fix.

5. Implement Game Mechanics
 - Game Loop: Use a while loop to keep the game running until the player escapes or loses.
 - Winning Conditions: The player wins by collecting all keys and unlocking the main gate.
 - Losing Conditions: The player loses if they trigger a trap or run out of time (if you implement a timer).

6. Apply Object-Oriented Programming
 - Create Classes:
 	- Room Class:
 		- Attributes: name, description, connections, items, locked
 		- Methods: describe(), get_connections(), is_locked(), unlock()
 	- Item Class:
 		- Attributes: name, description, type (e.g., key, tool)
 		- Methods: use()
 	- Player Class:
 		- Attributes: current_room, inventory
 		- Methods: move(), pick_up_item(), use_item()
 
 	- Instantiate Objects: Use these classes to create the game environment and manage game state.

7. Add Non-Player Characters (Optional but Recommended)
 	- Characters: Introduce NPCs like a ghostly figure or a mysterious cat.
		- Character Class:
	 		- Attributes: name, description, dialogue
	 		- Methods: speak(), interact()
	- Interactions: Allow the player to interact with NPCs to receive hints or items.

8. Implement a Simple Combat System (Optional)
	- Enemies: Introduce entities like haunted suits of armor or spiders.
	- Enemy Class:
		- Attributes: name, health, attack_power
		- Methods: attack(), take_damage()
 	- Combat Mechanics: Allow the player to engage in simple combat using items from their inventory.

9. Enhance the Game with Additional Features
	- Scoring System: Award points for actions like solving puzzles or collecting items.
	- Time Limit: Use the time module to impose a time limit on the game.
	- Random Events: Use the random module to trigger random events or item placements.

## Deliverables
 - Python Scripts: Submit all .py files containing your source code.
 - Game Execution: The game should run from a main script, typically main.py.
 - README File: Include instructions on how to run the game and a brief description of its features.
 - Comments and Documentation: Your code should be well-commented, explaining key sections and logic.
 - (Optional) Design Document: Provide a brief document outlining your game’s design, including class diagrams and flowcharts.


## Optional Bonus Features

### Graphical User Interface
 - Implement GUI: Use the tkinter library to create a simple interface for the game.
 - Visualize the player’s current room and inventory.
 - Provide buttons for movement and actions.

### Data Persistence
 - Save and Load Functionality: Allow the game state to be saved to a file and loaded later.
 - High Scores and Achievements: Record the player’s achievements or fastest escape times.

### Advanced OOP Concepts
 - Inheritance and Polymorphism: Create subclasses for different types of rooms or items.
 - Example: LockedRoom subclass of Room, Weapon subclass of Item.

### Enhanced Storytelling
 - Dynamic Story Elements: Change descriptions or available actions based on previous events.
 - Multiple Endings: Create different game endings based on player choices.

## Guidelines and Tips
 - **Start Simple**: Begin by implementing the core game mechanics before adding optional features.
	- Example: implement 3 rooms with a single item and test if you can win the game
 - Test Frequently: Regularly test each part of your code to ensure it works as expected.
 - Keep Code Modular: Use functions and classes to organize your code for readability and maintenance.
 - Use Version Control: Consider using Git to track changes and manage your code.
 - Ask for Help: If you encounter difficulties, don’t hesitate to reach out to instructors or peers.

## Resources
 - [Python Official Documentation:](https://docs.python.org/3/)
 - [Random Module Documentation](https://docs.python.org/3/library/random.html)
 - [Time Module Documentation](https://docs.python.org/3/library/time.html)
 - [Tkinter Tutorial](https://docs.python.org/3/library/tkinter.html)

By following this project outline, you’ll gain practical experience in Python programming while creating an engaging game. Focus on implementing the required features first, and then challenge yourself with the optional enhancements. Good luck, and enjoy your journey through the Haunted Mansion!