import random 
from new_game import Char


#---------------------------------------------------------------------------------------------------------------------------#
game_variables = {
    "selected_road": "",
    "selected_land": "",
    "selected_terrain": "",
    "current_enemy": None,
}
#---------------------------------------------------------------------------------------------------------------------------#




#---------------------------------------------------------------------------------------------------------------------------#
# Main Round Functions, loops everytime user ends the round. 
# How the user navigates through the game
# Loops until user dies
def main():
    while True:
        print("\nWhat do you want to do?")
        print("1. Go")
        print("2. Stay")
        choice = int(input("Select Option (1/2): "))
        if choice == 1:
            char_go()
        elif choice == 2:
            char_stay()
        else:
            print("\nINVALID INPUT WE NOW HAVE YER CREDIT CARD NUMBER\n")
        continue

if __name__ == "__main__":
    main()
#---------------------------------------------------------------------------------------------------------------------------#




#---------------------------------------------------------------------------------------------------------------------------#
# User chooses to go
def char_go():
    print("\nWhere would you like to go?")
    print("1. Follow the road.")
    print("2. Go to a nearby landmark.")
    print("3. Journey across the terrain.")
    go_choice = int(input("Select an option (1/2/3): "))
    if go_choice == 1:
        rand_road()
        print(f"\nYer at {game_variables['selected_road']}")
        enemy_encounter()
    elif go_choice == 2:
        rand_land()
        print(f"\nYer at {game_variables['selected_land']}")
        enemy_encounter()
    elif go_choice == 3:
        rand_terr()
        print(f"\nYer in the {game_variables['selected_terrain']}")
        enemy_encounter()
    else:
        print("\nINVALID INPUT WE NOW HAVE YER SSN\n")
        char_go()     
#---------------------------------------------------------------------------------------------------------------------------#




#---------------------------------------------------------------------------------------------------------------------------#
# Functions that generates places
# Add roads, landmarks, and terrains here:
def rand_road():
    road = ["an Abandoned City", "the Guarded City", "more Road"]
    game_variables["selected_road"] = random.choice(road)
    if game_variables["selected_road"] == "the Guarded City":
        Char.in_city = True
    else:
        Char.in_city = False
def rand_land():
    land = ["a Cave", "a Village", "a Temple"]
    game_variables["selected_land"] = random.choice(land)
    Char.in_city = False
def rand_terr():
    terrain = ["Woods", "Fields", "Desert"]
    game_variables["selected_terrain"] = random.choice(terrain)
    Char.in_city = False
#---------------------------------------------------------------------------------------------------------------------------#








#---------------------------------------------------------------------------------------------------------------------------#
# User Chooses to Stay
def char_stay():
    print("\nWhat would you like to do?")
    print("1. Rest")
    print("2. Explore")
    stay_choice = int(input("Select an option (1/2): "))

    if stay_choice == 1:
        char_rest()
    elif stay_choice == 2:
        char_explore()
    else:
        print("\nINVALID INPUT WE NOW HAVE YER ADDRESS\n")
        char_stay()

def char_rest():
    Char.health += 10
    print(f"\nYou have rested. Your health is now {Char.health}.")

def char_explore():
    print("\nWhat would you like to do?")
    print("1. Go to the Tavern")
    print("2. Go to the Keep")
    print("3. Go to the Temple")
    print("4. Go to the Witch")
    explore_choice = int(input("Select an option (1/2/3/4): "))
    if explore_choice == 1:
        print("\nYou go to the Tavern.")
        explore_tavern()
        Char.location = None
    elif explore_choice == 2:
        print("\nYou go to the Keep.")
        explore_keep()
        Char.location = None
    elif explore_choice == 3:
        print("\nYou go to the Temple.")
        explore_temple()
        Char.location = None
    elif explore_choice == 4:
        print("\nYou go to the Witch.")
        explore_witch()
        Char.location = None
    else:
        print("\nINVALID INPUT WE NOW HAVE YER MEDICAL RECORDS\n")
        Char.location = None
        char_explore()
#---------------------------------------------------------------------------------------------------------------------------#




#---------------------------------------------------------------------------------------------------------------------------#
# Exploring the City Functions:
# Tavern: Talk to bartender for a drink, or talk to the drunk (I need to add that the drunk can give you a quest)
def explore_tavern():
    print("\nYou enter the Tavern.")
    print("What would you like to do?")
    print("1. Talk to the Bartender")
    print("2. Talk to the Drunk")
    print("3. Leave")
    tavern_choice = int(input("Select an option (1/2/3/4): "))
    if tavern_choice == 1:
        print("\nYou talk to the Bartender.")
        print("Bartender: Welcome to the Tavern! What can I get you?")
        print("1. Ale")
        print("2. Water")
        print("3. Leave")
        bartender_choice = int(input("Select an option (1/2/3): "))
        if bartender_choice == 1:
            print("\nYou order an ale.")
            print("Bartender: That'll be 5 gold.")
            print("You pay the Bartender 5 gold.")
            Char.modify_gold(-5)
            print("You have: ", Char.gold, "gold.")
            print("Bartender: Here you go.")
            print("You drink the ale.")
            print("You feel refreshed.")
            Char.modify_health(10)
            print(f"Your health is now {Char.health}.")
        elif bartender_choice == 2:
            print("\nYou order some water.")
            print("Bartender: That'll be 2 gold.")
            print("You pay the Bartender 2 gold.")
            Char.modify_gold(-2)
            print("You have: ", Char.gold, "gold.")
            print("Bartender: Here you go.")
            print("You drink the water.")
            print("You feel refreshed.")
            Char.modify_health(10)
            print(f"Your health is now {Char.health}.")
        elif bartender_choice == 3:
            print("\nYou leave the Tavern.")
        else:
            print("\nINVALID INPUT WE NOW HAVE YER BANK ACCOUNT INFO\n")
            explore_tavern()
    elif tavern_choice == 2:
        print("\nYou talk to the Drunk.")
        print("Drunk: Hic! I'm drunk!")
        print("You leave the Drunk.")
    elif tavern_choice == 3:
        print("\nYou leave the Tavern.")




# Keep: Talk to the King for a quest
def explore_keep():
    if Char.type == "Knight":
        print("\nYou enter the Keep.")
        print("King: Welcome Knight!  Stay a while.")
        maybe_gold()
    elif Char.type == "Elf":
        print("\nYou enter the Keep.")
        print("King: GET THAT CREATURE OUT OF HERE!")
    elif Char.type == "Viking":
        print("\nYou enter the Keep.")
        print("King: What do you want?")
        maybe_gold()
    elif Char.type == "Dwarf":
        print("\nYou Enter the Keep.")
        print("King: Welcome.")
        maybe_gold()
    elif Char.type == "Assassin":
        print("\nYou enter the Keep.")
        print("King: What do you want?")
        maybe_gold()
    elif Char.type == "Archer":
        print("\nYou enter the Keep.")
        print("King: Welcome, what can we do for you?")
        maybe_gold()


def maybe_gold():
    rand_num = random.randint(1, 10)
    if rand_num == 1 or rand_num == 3 or rand_num == 7:
        print("\nKing: Thank you for your service.  Here is some gold.")
        Char.modify_gold(10)
        print("You have: ", Char.gold, "gold.")
    else:
        print("\nKing: Thank you for your service.")




# Temple: Talk to the Priest to pray or repent
def explore_temple():
    print("\nYou enter the Temple.")
    print("Priest: What would you like to do?")
    print("1. Pray")
    print("2. Repent")
    print("3. Leave")
    temple_choice = int(input("Select an option (1/2/3): "))
    if temple_choice == 1:
        print("\nYou pray.")
        print("Priest: May the Gods be with you.")
        print("You feel refreshed.")
        Char.modify_health(10)
        print(f"Your health is now {Char.health}.")
    elif temple_choice == 2:
        print("\nYou repent.")
        print("Priest: May the Gods be with you.")
        print("You feel refreshed.")
        Char.modify_health(10)
        print(f"Your health is now {Char.health}.")
    elif temple_choice == 3:
        print("\nYou leave the Temple.")
    else:
        print("\nINVALID INPUT WE NOW HAVE YER BANK ACCOUNT INFO\n")
        explore_temple()




# Witch: Talk to the Witch for a fortune or a curse
def explore_witch():
    print("\nYou enter the Witch's Hut.")
    print("Witch: Take a seat.")
    input("Press enter to continue.")
    gift_or_curse = random.randint(1, 2)
    if gift_or_curse == 1:
        print("\nWitch: I will give you a gift.")
        print("You feel refreshed.")
        Char.modify_health(10)
        print(f"Your health is now {Char.health}.")
    elif gift_or_curse == 2:
        print("\nWitch: I will curse you.")
        print("You feel cursed.")
        Char.modify_health(-10)
        print(f"Your health is now {Char.health}.")
    else:
        print("\nINVALID INPUT WE NOW HAVE YER BANK ACCOUNT INFO\n")
        explore_witch()
#---------------------------------------------------------------------------------------------------------------------------#




#---------------------------------------------------------------------------------------------------------------------------#
# Fighting Sequence Functions:
# Fighting Sequence: Triggers when the user encounters an enemy
# Enemy Object:
class Enemy:
    def __init__(self, name, type, health, attack):
        self.name = name
        self.type = type
        self.health = health
        self.attack = attack
    def modify_health(self, health_change):
        self.health += health_change
#---------------------------------------------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------------------------------------------#
# Add enemies and bosses here:
def generate_enemy():
    enemy_dict={
        "Daegon": Enemy("Daegon", "Demon", 40, 4),
        "Centaurith": Enemy("Centaurith", "Beast", 40, 4),
        "Aacalith": Enemy("Aacalith", "Vampire", 30, 3),
        "Zrython": Enemy("Zrython", "Beast", 30, 2),
        "Thraspinox": Enemy("Thraspinox", "Beast", 30, 2),  
        "Umbrafiend": Enemy("Umbrafiend", "Ghoul", 20, 2),      
    }
    enemy_boss = {
        "Vziathar": Enemy("Vziathar", "God", 100, 8)
    }
    random_enemy_key = random.choice(list(enemy_dict.keys()))
    game_variables["current_enemy"] = enemy_dict[random_enemy_key]
#---------------------------------------------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------------------------------------------#
def clear_current_enemy():
    game_variables["current_enemy"] = None
def current_enemy_check():
    if game_variables["current_enemy"] == None:
        print(" ")
    else:
        print(f"Current enemy: {game_variables['current_enemy'].name} \n{game_variables['current_enemy'].type} \n{game_variables['current_enemy'].health} \n{game_variables['current_enemy'].attack}")
#---------------------------------------------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------------------------------------------#
# Basic Fighting Sequence:
# Main fighting Function, triggers when the user enters a new location
def enemy_encounter():
    generate_enemy()
    print(f"\nYou've encountered {game_variables['current_enemy'].name}!")
    fight_or_flee = int(input("1. Fight\n2. Flee\n"))
    if fight_or_flee == 1:
        fight_sequence()
    elif fight_or_flee == 2:
        print("You fled!")
        clear_current_enemy()
    else:
        print("\nINVALID INPUT WE NOW HAVE YER BANK ACCOUNT INFO\n")
        fight_sequence()

# Fight sequence, triggers when the user chooses to fight
def fight_sequence():
    while game_variables["current_enemy"].health > 0 and Char.health > 0:
        print(f"\n{game_variables['current_enemy'].name}'s stats:\nHealth: {game_variables['current_enemy'].health}\nAttack: {game_variables['current_enemy'].attack}")
        print(f"\n{Char.type}'s stats:\nHealth: {Char.health}\nAttack: {Char.attack}")
        roll_result()
        print(f"\nYour health is {Char.health}")
        print(f"The enemy's health is {game_variables['current_enemy'].health}\n")
        print("---------------------------------------------------------------------------------------------------------------------------")
    if game_variables["current_enemy"].health <= 0:
        print(f"\n\nYou have defeated {game_variables['current_enemy'].name}!\n\n")
        clear_current_enemy()
        current_enemy_check()
    elif Char.health <= 0:
        print("\n\nYou have died!\n\n")
        exit()
#---------------------------------------------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------------------------------------------#
# Roll Result is the result of two functions: char_roll, enemy_roll
# Both Char and Enemy roll a d20, then add their attack stat to the roll, then establishes the difference between the two rolls
def roll_result():
    char_roll_result = char_roll()
    enemy_roll_result = enemy_roll()
    roll_difference = char_roll_result - enemy_roll_result
    if roll_difference > 0:
        print(f"\nYou dealt {roll_difference} damage!")
        game_variables["current_enemy"].modify_health(-roll_difference)
    elif roll_difference < 0:
        print(f"\nThe enemy dealt {-roll_difference} damage!")
        Char.modify_health( roll_difference)
    else:
        print("\nYou both missed!")
def char_roll():
    useless_var = input("Press enter to roll")
    char_roll_result = random.randint(1, 20)
    print(f"\nYou roll a {char_roll_result}")
    char_attack = Char.attack + char_roll_result
    print(f"Your attack this round is {char_attack}")
    return char_attack
def enemy_roll():
    enemy_roll_result = random.randint(1, 20)
    print(f"\nThe enemy rolls a {enemy_roll_result}")
    enemy_attack = game_variables["current_enemy"].attack + enemy_roll_result
    print(f"The enemy's attack this round is {enemy_attack}")
    return enemy_attack
#---------------------------------------------------------------------------------------------------------------------------#

