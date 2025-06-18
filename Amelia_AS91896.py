# imports and vairiables
import game_play
import random
senario_1 = False
senario_2 = False
player_health = 25
treats = 0
start_decision = False


def StatsMenu():
    # stats menu
        global player_health
        global treats
        playing_status = False
        print("{}".format(statistics.get("stats")))
        stats_decision = int(input())
        # eats treat and gives +5 health
        if stats_decision == 1 and treats > 0:
            treats -= 1
            player_health += 5
            decision = 8
        # if the user trys to eat a treat but doesnt have any it will print an error statement 
        elif stats_decision == 1 and treats == 0:
            print("You don't have enough treats for this!")
            decision = 8
        # continues on to game
        if stats_decision == 2:
            playing_status = False
            current_senario = True
senarios = {
    """
    ——————————————————————––––––––
    You come across a small cave.
    ——————————————————————––––––––
          Choose an option.

      1. Set up camp/sleep there
      2. Continue on.
    ——————————————————————––––––––""": "cave",

    """
    ——————————————————————––––––––
    As the path becomes more rugged 
    You start to feel eyes watching you…
    ——————————————————————––––––––
        A bandit has appeared!
          Choose an option.

      1. Try to befriend him
      2. Fight him
    ——————————————————————––––––––""": "bandit",

    """
    ——————————————————————––––––––
        You found a clearing!
    ——————————————————————––––––––
          Choose an option.

      1. Continue
      2. Explore
    ——————————————————————––––––––""": "clearing",}


# Stats menu
statistics = {
    "stats": """   
    ——————————————————————––––––––
             Stats Menu
    ——————————————————————––––––––
             You have:
        
     {} Treats   |   {}/25 Health

      1. Eat a treat (+5 Health)
      2. Continue/Close menu
    ——————————————————————––––––––""".format(treats, player_health)
}

# asks user if they want to play, if invalid awnser is said it loops and asks again
while start_decision == False:
    try:
        print(
        """
        ——————————————————————–
            Hi! Welcome to
        AS91896 Text Adventure! 
        ——————————————————————–
        Would you like to play?

        1 = Yes
        2 = No
        ——————————————————————–""")
        temp = int(input())

    except ValueError:
        print("Please enter a valid number!")

# if 1 is entered game starts, if 2 is entered game ends
    else:
        if temp == 1:
            playing_status = True
            start_decision = True
        elif temp == 2:
            start_decision = True
            playing_status = False

if playing_status == False:
    print("Thanks for playing!")
    quit()
# prints user manual with all the controls, if 9 is pressed game quits, if 8 is pressed stats are printed, if any other number is pressed game starts
while playing_status == True:
    try:  
        print("""
        ——————————————————————
             User Manual
        ——————————————————————
        Enter these letters to 
        use these functions at 
            any time.

            9 - Quit game
            8 -Check stats

        Good luck on your journey!
        Press Any Number to Continue.
        ——————————————————————""")
        decision = int(input())
    
    except ValueError:
        print("Please enter a valid number!")
# quit game
    if decision == 9:
        playing_status = False

# stats menu
    elif decision == 8:
        StatsMenu()
    # starts game
    else:
        current_senario = True
        playing_status = False

senario_1 = current_senario

# starts senario 1
while senario_1 == True:
    try:
        print("{}".format(game_play.start.get("start_senario")))
        decision = int(input())
        if decision == 2:
            senario_1 = False
            playing_status = False
        elif decision == 1:
            senario_1 = False
            senario_2 = True
        elif decision == 8:
            StatsMenu()
        else:
            print("Please enter a valid number!")
    except ValueError:
        print("Please enter a valid number!")

tempp = 0
current_senario = senario_2
while tempp <= 3 and decision == 1:
    while senario_2 == True:
        try:
            senario_number = random.randint(1,3)
            chosen_prompt = print("{}".format((random.choice(list(senarios)))))
            decision = int(input())
            senario_2 = False
            tempp += 1
        except ValueError:
            print("Please enter a valid number!")


if playing_status == False:
    print("Thanks for playing!")
    quit()

if decision == 9:
    playing_status = False
elif decision == 8:
    playing_status = False
    print("{}".format(statistics.get("stats")))
    decision = int(input())

    if decision == 1 and treats > 0:
        treats -= 1
        player_health += 5
        decision = 8
    elif decision == 1 and treats == 0:
        print("You don't have enough treats for this!")
        decision = 8
    if decision == 2:
        playing_status = False
        current_senario = True
    else:
        current_senario = True
        playing_status = False
