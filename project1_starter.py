"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Your Name Here]
Date: [Date]

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""
def create_character(name, character_class):
    level = 1
    strength, magic, health = calculate_stats(character_class, level)
    character = {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": 100
    }
    return character
# Creates a new character starting at level 1 and establishes the stats that it will need to be included. Then establishes a dictionary set up how the info is formatted. 

def calculate_stats(character_class, level):
    character_class = character_class.lower()
    if character_class == "warrior":
        strength = 10 + (level * 5)
        magic = 2 + (level * 1)
        health = 120 + (level * 10)
# Since warriors have high strength and health, those stats are increased compared to other classes.
    elif character_class == "mage":
        strength = 4 + (level * 2)
        magic = 12 + (level * 6)
        health = 80 + (level * 6)
# Since mages have higher magic, that stat is increased compared to other classes.
    elif character_class == "rogue":
        strength = 7 + (level * 3)
        magic = 7 + (level * 3)
        health = 90 + (level * 7)
# Since rogues have high strength/magic but lower health, those stats are changed compared to other classes.
    elif character_class == "cleric":
        strength = 6 + (level * 2)
        magic = 10 + (level * 4)
        health = 100 + (level * 8)
# Since clerics higher magic and slightly higher strength, those stats are increased compared to other classes.
    else:
        strength = 5 + (level * 2)
        magic = 5 + (level * 2)
        health = 100 + (level * 5)
# if none of the roles above are input, the class is given default stats.  
    return (strength, magic, health)
# Takes different classes and establishes the stats the character will get based on what is chosen.
def save_character(character, filename):
    file = open(filename, 'test.txt')

    file.write("Character Name: " + character["name"] + "\n")
    file.write("Class: " + character["class"] + "\n")
    file.write("Level: " + str(character["level"]) + "\n")
    file.write("Strength: " + str(character["strength"]) + "\n")
    file.write("Magic: " + str(character["magic"]) + "\n")
    file.write("Health: " + str(character["health"]) + "\n")
    file.write("Gold: " + str(character["gold"]) + "\n")

    file.close()
    return True
# Saves the character and stats from the dictionary into a text file, writes each on a separate line, then closes it. 

def load_character(filename):
    import os
    if not os.path.exists(filename):
        return None

    file = open(filename, 'r')
    lines = file.readlines()
    file.close()

    character = {}

    for line in lines:
        key, value = line.strip().split(": ")
        if key == "Character Name":
            character["name"] = value
        elif key == "Class":
            character["class"] = value
        elif key == "Level":
            character["level"] = int(value)
        elif key == "Strength":
            character["strength"] = int(value)
        elif key == "Magic":
            character["magic"] = int(value)
        elif key == "Health":
            character["health"] = int(value)
        elif key == "Gold":
            character["gold"] = int(value)

    return character
# Loads the saved character from its file and writes all attributes on separate lines. 

def display_character(character):
    print("=== CHARACTER DETAILS ===")
    print("Name: " + character["name"])
    print("Class: " + character["class"])
    print("Level: " + str(character["level"]))
    print("Strength: " + str(character["strength"]))
    print("Magic: " + str(character["magic"]))
    print("Health: " + str(character["health"]))
    print("Gold: " + str(character["gold"]))
    print("=========================")
# AI organized how everything is displayed, since at first things did not match the order it needed to. 
# Prints out the current character details to the user, str() changes numbers to strings so it can be added to the file.
def level_up(character):
    character["level"] += 1
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health
    return character
# Determines what stats change as the character levels up based on the selected class. 

if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")

    name = input("Enter character name: ")
    char_class = input("Enter character class (warrior, mage, rogue, cleric): ")

    char = create_character(name, char_class)
    display_character(char)

    filename = name.lower() + "_char.txt"
    save_character(char, filename)
    print(f"Character saved to {filename}")

    loaded = load_character(filename)
    if loaded is not None:
        print("Character loaded successfully!")
        display_character(loaded)
    else:
        print("Error: File not found.")
# AI fixed any indentation issues, made sure functions were organized so the code waws easy to read and formatted correctly.
# Allows input to be written, creates the character and gives stats, saves to a file, then loads the file's contents to be displayed again.
# AI gave me the understanding as to what role each different set of code does.
