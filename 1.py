import time
import random
# variable to change the enemy each time the player chooces play again
enemy=["cerberus", "typhon", "hydra","cyclops"]
enemy_random=random.choice(enemy)
#variable to display different random message each time when the player wins
win=['congratultions for winning', 'you won', 'winer', 'you are the best you won']
win_random=random.choice(win)
#variable to display different random message each time when the player loses
lose=['you lost', 'sorry for losing', 'you did it wrong', 'you didn’t do it']
lose_random=random.choice(lose)
# primts the text while stopping for 1.5 seconds
def print_pause(message):
    print(message)
    time.sleep(1.5)
# make sure the player doesn’t enter unvalid choice
def get_valid_input (prompt, valid_choices):
    user_input = int(input(prompt))
    while user_input not in valid_choices:
        print(f"{user_input} is not a valid choice.Please enter one of the valid choices: {valid_choices}")
        user_input = int(input(prompt))
    return user_input
# making score variable
score = 10
# calculate the score and displays it using the def display_score()
def score_updated( amount ):
    global score 
    score += amount
    display_score(score)
    win_lose()
# shows the score
def display_score(score):
    print(f"Score: {score}")
# makes play again option
def play_again() :
    global score, enemy_random
    play_again_input = input("Do you want to play again? (yes/no): ")
    if play_again_input == "yes":
        score = 10
        enemy_random=random.choice(enemy)
        main_game()
    elif play_again_input == "no":
        print("Thank you for playing!")
    else:
        while play_again_input != "yes" and play_again_input != "no" :
            print(f"{play_again_input} is not a valid choice.Please enter yes or no")
            play_again_input = input("Do you want to play again? (yes/no): ")
        if play_again_input == "yes":
           score = 10
           main_game()
        elif play_again_input == "no":
           print("Thank you for playing!")
# clarify when does the player loses or wins thw game with play again option
def win_lose():
    if score == 0 :
        print (lose_random)
        play_again()
    elif score == 25 :
        print("you won")
        play_again()
# the main story of the game 
def island():
    print_pause("Now you are preparing yourself to get down from the ship with 50 men to find food.")
    print_pause("On the island, you found people and asked them to exchange food")
    print_pause("with a bottle of unordinary juice Athena had given you.")
    print_pause("They accepted but told you that there is a place near a cave ")
    print_pause("containing tons of food and a river of water.")
    return get_valid_input("\n1. Go to the place\n2. Refuse and exchange food with them\n", [1, 2])

def keep_way():
    print_pause("The ship kept going, now you don’t have any food or water, ")
    print_pause("and you are in the middle of the sea.")
    print_pause("The soldiers kept falling one after another, and ")
    print_pause("when you reached your destination, you only had 350 men left.")
    print_pause(f"You got to the island where the {enemy_random} lived. ")
    print_pause("You found food, water, and sheep on its island.")
    print_pause(f"You found a cave and knew that the {enemy_random} is inside it.")
    return get_valid_input("\n1. Go into the cave\n2. Get some food and go train\n", [1, 2])

def go_place():
    print_pause("You went to that place after they took you and your followers there.")
    print_pause("You all were dazzled by the place: green pastures, sheep, ")
    print_pause("and trees decorated with all the beloved fruits.")
    print_pause(f"You killed a sheep. What!!! There's a {enemy_random} right there!")
    return get_valid_input("\n1. Fight\n2. Run away with your 50 soldiers\n", [1, 2])

def exchange_food():
    print_pause("You said no thanks, I don’t want to waste time and ")
    print_pause("exchanged some food and water with that bottle of juice.")
    print_pause("You went back to the ship, confused between training or taking rest")
    print_pause("until you reach your destination.")
    return get_valid_input("\n1. Training\n2. Rest\n", [1, 2])

def training():
    print_pause
    ("You trained, and the final step has come. You reached your destination.")
    print_pause(f"You got to the island where the {enemy_random} lived.")
    print_pause("You found food, water, and sheep on its island.")
    print_pause(f"You found a cave and knew that the {enemy_random} is inside it.")
    print_pause(f"You went into the cave and woke the {enemy_random} up.")
    return get_valid_input(f"\n1Fight the {enemy_random} \n2.Get your men and run for your lives\n", [1, 2])

def rest():
    print_pause("You rested, and the final step has come. You reached your destination.")
    print_pause(f"You got to the island where the {enemy_random} lived. ")
    print_pause("You found food, water, and sheep on its island.")
    print_pause(f"You found a cave and knew that the {enemy_random} is inside it.")
    print_pause(f"You went into the cave and woke the {enemy_random} up.")
    return get_valid_input(f"\n1. Fight the {enemy_random} \n2. Get your men and run for your lives\n", [1, 2])

def go_cave():
    print_pause(f"You woke up the {enemy_random} and now you have two choices:")
    return get_valid_input("\n1. Fight\n2. Run\n", [1, 2])

def get_food():
    print_pause(f"You tried to get food, but the {enemy_random} woke up. Now you have two choices:")
    return get_valid_input("\n1. Fight\n2. Run\n", [1, 2])

def fight_place():
    print_pause("You lost and the 50 soldiers died.")

def run_place():
    print_pause("You and 10 soldiers escaped with your lives.")
    print_pause("You felt that you are not ready enough.")
    print_pause("You decided to go back to Athena and get more training.")

def fight_training():
    print_pause("You win with your soldiers.")

def run_training():
    print_pause("You weren’t confident enough to fight and you tried to run,")
    print_pause(f"but the {enemy_random} ate you and your men.")

def fight_rest():
    print_pause(f"You win against the {enemy_random}, ")
    print_pause("but a lot of your men died because of lack of training.")

def run_rest():
    print_pause(f"The {enemy_random} ate you and most of your soldiers.")

def fight_cave():
    print_pause("You win but only 100 men survived.")

def run_cave():
    print_pause("You couldn’t run because of lack of healthy nutrition and you have been eaten.")

def fight_food():
    print_pause("You couldn’t fight well because of lack of nutrition and you lost.")

def run_food():
    print_pause("You and your soldiers ran with some food that will be enough for a week.")
    print_pause(f"After a week of training, you went and fought {enemy_random}.")
    print_pause("Congratulations, you won and passed the test!")
# to but the game in a function call it when i need
def main_game():
   print_pause("You are a Greek from ancient Greece. You are a student of ")
   print_pause("Athena, goddess of wisdom and master of war.")
   print_pause(f"You are going for your first test to fight a {enemy_random}, ")
   print_pause("and you have been given 600 men under your command.")
   print_pause(f"You and your followers are on a ship to go and fight the {enemy_random},")
   print_pause ("and you are running out of food and water.")
   print_pause("You saw an island not very far from the ship,")
   print_pause("but if you want to go to this island, you have to change the ship’s course.")
   print_pause("\n \n note : your score is 10 now when your score becomes0 0 you loose ")
   print_pause("and when it is 25 you win \n")
   user_input = get_valid_input("\nchoose \n1. Not to change the ship’s course and keep in your direction\n2. Go to the island\n", [1, 2])
# the games loop 
   if user_input == 1:
        score_updated(-5)
        user_input = keep_way()
        
        if user_input == 1:
            score_updated(-5)
            user_input = go_cave()
            
            if user_input == 1:
                score_updated(5)
                fight_cave()
                
            elif user_input == 2:
                score_updated(-5)
                run_cave()
                
        elif user_input == 2:
            score_updated(5)
            user_input = get_food()
            
            if user_input == 1:
                score_updated(-5)
                fight_food()
            elif user_input == 2:
                score_updated(5)
                run_food()
                
   elif user_input == 2:
        score_updated(5)
        user_input = island()
        
        if user_input == 1:
            score_updated(-5)
            user_input = go_place()
            
            if user_input == 1:
                score_updated(-5)
                fight_place()
                
            elif user_input == 2:
                score_updated(5)
                run_place()
               
        elif user_input == 2:
            score_updated(5)
            user_input = exchange_food()
            
            if user_input == 1:
                score_updated(5)
                user_input = training()
                
                if user_input == 1:
                    score_updated(5)
                    fight_training()
                    
                elif user_input == 2:
                    score_updated(-5)
                    run_training()
                   
            elif user_input == 2:
                score_updated(-5)
                user_input = rest()
                
                if user_input == 1:
                    score_updated(5)
                    fight_rest()
                    
                elif user_input == 2:
                    score_updated(-5)
                    run_rest()
                    
   print("Game over")
   play_again()
main_game()


 