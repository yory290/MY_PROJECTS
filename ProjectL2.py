import time
def print_pause(message):
    print(message)
    time.sleep(1.5)
def island():
    print_pause("now you are preparing yourself to get down from the ship with 50 men to find food")
    print_pause("in the island you found people and you asked them to exchange food with bottel of an unordinary juic Athena has gave you ")
    print_pause("they accepted but told you that there is a place near into a cave contains tons of food and a river of water")
    print_pause("\n 1 go to the place")
    print_pause("\n 2 to refuse and exchange food with them")
def keep_way():
    print_pause("the ship kept going now you don’t have any food or water and you are in the middle of the sea ")
    print_pause("the soldiers kept falling one after one and when you reached your destinantion you only had 350 men")
    print_pause("you got to the island where the cyclops lived you found food, water and sheeps on its island ")
    print_pause("you found a cave and you knew that the cyclops is inside it")
    print_pause("\n 1 go into the cave")
    print_pause("\n 2 get some food and go train")
def go_place():
    print_pause("you went to that place after they took you and your followers to that place and immediately go ")
    print_pause("you all were dazaled by the place green pastures, sheeps and trees decorated with all the beloved fruits ")
    print_pause("you killed a sheep what!!! their is a cyclops right their ")
    print_pause("\n 1 fight \n 2 run away with your 50 soldiers")
def exchange_food():
    print_pause("you said no thanks i don’t wanna to waste time and you exchanged some food and water with that bottle of juice")
    print_pause("you went back to the ship and you were confused between training or take rest until you reach your destination")
    print_pause("\n 1 training \n 2 rest")
def training():
   print_pause("you trained and the final step has come and you reached your destination")
   print_pause("you got to the island where the cyclops lived you found food, water and sheeps on its island ")
   print_pause("you found a cave and you knew that the cyclops is inside it")
   print_pause("\n you went into the cave and woke the cyclops up ")
   print_pause("\n 1 fight the cyclops \n 2 get your men and run for your lives")
def rest():
   print_pause("you rested and the final step has come and you reached your destination")
   print_pause("you got to the island where the cyclops lived you found food, water and sheeps on its island ")
   print_pause("you found a cave and you knew that the cyclops is inside it")
   print_pause("\n you went into the cave and woke the cyclops up ")
   print_pause("\n 1 fight the cyclops \n 2 get your men and run for your lives")
def go_cave():
    print_pause("you woke up the cyclops and now you have two choices \n \n 1 fight \n 2 run")
def get_food():
    print_pause("you tried to get food but the cyclopes woke up now you have two choices \n \n 1 fight \n 2 run ")
def fight_place():
   print_pause("you loose and the 50 soldeirs died")
def run_place():
   print_pause("you and 10 soldiers escaped with your lives") 
   print_pause ("you felt that you are not ready enough") 
   print_pause("you decided to go back to Athena and get more training")
def fight_training():
   print_pause("you win with your soldiers")
def run_training():
   print_pause("you weren’t confident enough to fight and you treid to run but the syclops ate you and your men")
def fight_rest():
   print_pause("you win against the syclops but a lot of your men died because of lack of training")
def run_rest():
   print_pause("the syclops ate you and most of your soldiers")
def fight_cave():
   print_pause("you win but only 100 men survived")
def run_cave():
   print_pause("you couldn’t run because lack of healthy nutrition and you have been eaten")
def fight_food():
   print_pause("you couldn’t fight well becouse of lack of nutrition and you loose")
def run_food():
   print_pause("you and your soldier ran with some food that will be enough for a week")
   print_pause("after a week of training you went and fought the cyclops")
   print_pause("congratulations you won and passed the test ")
   

print_pause ("you are a greek from the ancient greece you are the student of Athena goddess of wisdom and master of war")
print_pause ("you are going for your first test to fight a cyclops and you were given 600 men with you under your command ")
print_pause("you and your followers were on a ship to go and fight the cyclops and you were running out of food and water")
print_pause("you saw an island not very far from the ship but if you want to get into this island you gotta change the ship’s course ")
print_pause("\n 1 not to change the ship’s course and keep in your direction")
print_pause("\n 2 to go to the island")

user_input = int(input("please enter 1 or 2: "))
if user_input == 1 :
    keep_way()
    user_input = int(input("please enter 1 or 2: "))
    if user_input == 1:
        go_cave()
        user_input = int(input("please enter 1 or 2: "))
        if user_input == 1:
           fight_cave()
        elif user_input == 2:
           run_cave()
        else:
          while user_input != 1 and user_input != 2:
            print(f"{user_input} is not a valid choice. Please enter 1 or 2: ")
            user_input = int(input("Please enter 1 or 2: "))
    
          if user_input == 1:
              fight_cave()
          elif user_input == 2:
             run_cave()
    elif user_input == 2:
        get_food()
        user_input = int(input("please enter 1 or 2: "))
        if user_input == 1 :
           fight_food()
        elif user_input == 2 :
           run_food()
        else:
           while user_input != 1 and user_input != 2 :
              print(f"{user_input} is not a valid choice. Please enter 1 or 2: ")
           if user_input == 1 : 
              fight_food()
           elif user_input == 2 : 
              run_food()
    else :
      while user_input != 1 and user_input != 2:
        print(f"{user_input} is not a valid choice. Please enter 1 or 2: ")
        user_input = int(input("Please enter 1 or 2: "))
    
      if user_input == 1:
         go_cave()
      elif user_input == 2:
         get_food()

elif user_input == 2 :
    island()
    user_input = int(input("please enter 1 or 2: "))
    if user_input == 1:
        go_place()
        user_input = int(input("please enter 1 or 2: "))
        if user_input == 1 :
           fight_place()
        elif user_input == 2 :
           run_place()
        else :
           while user_input != 1 and user_input != 2 :
              print(f"{user_input} is not a valid choice. Please enter 1 or 2: ")
              user_input = int(input("please enter 1 or 2: "))
           if user_input == 1 :
              fight_place()
           elif user_input == 2 :
              run_place()
    elif user_input == 2:
        exchange_food()
        user_input = int(input("please enter 1 or 2: "))
        if user_input == 1 :
           training()
           user_input = int(input("please enter 1 or 2: "))
           if user_input == 1 :
              fight_training()
           elif user_input == 2 :
              run_training()
           else :
              while user_input != 1 and user_input != 2:
               print(f"{user_input} is not a valid choice. Please enter 1 or 2: ")
               user_input = int(input("Please enter 1 or 2: "))
               if user_input == 1:
                  fight_training()
               elif user_input == 2:
                  run_training()
        elif user_input == 2 :
           rest()

        else :
           while user_input != 1 and user_input != 2:
            print(f"{user_input} is not a valid choice. Please enter 1 or 2: ")
            user_input = int(input("Please enter 1 or 2: "))
    
           if user_input == 1:
               training()
           elif user_input == 2:
               rest()
               user_input = int(input("please enter 1 or 2: "))
               if user_input == 1 :
                  fight_rest()
               elif user_input == 2 :
                  run_rest()
               else :
                   while user_input != 1 and user_input != 2:
                     print(f"{user_input} is not a valid choice. Please enter 1 or 2: ")
                     user_input = int(input("Please enter 1 or 2: "))
                   if user_input == 1:
                     fight_rest()
                   elif user_input == 2:
                     run_rest()
    else :
      while user_input != 1 and user_input != 2:
        print(f"{user_input} is not a valid choice. Please enter 1 or 2: ")
        user_input = int(input("Please enter 1 or 2: "))
      if user_input == 1:
         go_place()
      elif user_input == 2:
         exchange_food()
else :
    while user_input != 1 and user_input != 2:
        print(f"{user_input} is not a valid choice. Please enter 1 or 2: ")
        user_input = int(input("Please enter 1 or 2: "))
    
    if user_input == 1:
       keep_way()
    elif user_input == 2:
        island()
    

       