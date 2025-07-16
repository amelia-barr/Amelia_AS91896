# imports and vairiables
import random
first_decision = False
scenario_2 = False
player_health = 25
treats = 0
start_decision = False
bandit_health = 10
scenario_counter = 0
boss_fight_check = False

# Quit game
def QuitGame(decision):
    if decision == 9:
        print("Thanks for playing!")
        quit()

# Stats menu
def StatsMenu():
    global player_health, treats, playing_status, current_scenario
    playing_status = False
    if player_health >= 25:
        player_health = 25
        
    print(f"""   
——————————————————————––––––––
         Stats Menu
——————————————————————––––––––
         You have:
    
 {treats} Treats   |   {player_health}/25 Health

  1. Eat a treat (+5 Health)
  2. Continue/Close menu
——————————————————————––––––––""")
    try:
        stats_decision = int(input())
        # eats treat and gives +5 health
        if stats_decision == 1 and treats > 0 and player_health < 25:
            treats -= 1
            player_health += 5
            if player_health >= 25:
                player_health = 25
            print("You ate a treat! +5 Health")
            StatsMenu()

        elif stats_decision == 1 and player_health >= 25:
            print("You are already healthy!")
            StatsMenu()

        # if the user trys to eat a treat but doesnt have any it will print an error statement 
        elif stats_decision == 1 and treats == 0:
            print("You don't have enough treats for this!")
            StatsMenu()
            
        # continues on to game
        if stats_decision == 2:
            playing_status = False
            current_scenario = True
    except ValueError:
        print("Please enter a valid number!")
        StatsMenu()

start = {
    "start_scenario": """
    ——————————————————————––––––––
      You find yourself at the 
          edge of a forest.
    ——————————————————————––––––––
          Choose one path.

    1. Continue through the forest
    2. Turn back
    ——————————————————————––––––––"""    
}

scenarios = {
    """
——————————————————————––––––––
You come across a small cave.
——————————————————————––––––––
      Choose an option.

  1. Continue on.
  2. Set up camp/sleep there
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
——————————————————————––––––––""": "clearing",
}

scenario_outcomes_clearing = {
    """
——————————————————————––––––––
   You tripped! -2 Health
——————————————————————––––––––
      Choose an option.

  1.  Continue
——————————————————————––––––––""" : "clearing_1",
    """
——————————————————————––––––––
    You found a squirrel!
——————————————————————––––––––
      Choose an option.

  1. Continue 
  2. Help it
——————————————————————––––––––""" : "clearing_2"
}

scenario_outcomes_bandit = {
    """
——————————————————————––––––––
  You befriended the bandit!
    He gave you 3 treats!
——————————————————————––––––––
      Choose an option.
    
  1. Continue
——————————————————————––––––––""" : "bandit_1",
    """
——————————————————————––––––––
You failed to befriend the bandit!
  He punches you and runs off
         -3 Health
——————————————————————––––––––
      Choose an option.
    
  1. Continue
  2. Chase after him
——————————————————————––––––––""": "bandit_2"
}

scenario_outcomes_cave = {
    """
——————————————————————––––––––
  You slept well and woke up 
      feeling refreshed.
          +1 Health
——————————————————————––––––––
       Choose an option.
    
  1. Continue
——————————————————————––––––––""": "cave_1",

    """
——————————————————————––––––––
While scouting out the cave to 
   gauge its safety you spot 
       large footprints.
——————————————————————––––––––
       Choose an option.
    
  1. Carry on your journey without sleep
  2. Ignore them and set up camp
——————————————————————––––––––""": "cave_2",
}

rare_outcomes = {
    "clearing": """
——————————————————————––––––––
   You helped the squirrel!
  The squirrel thanks you by 
   giving you some acorns!
          +2 treats
——————————————————————––––––––
       Choose an option.

  1. Continue 
——————————————————————––––––––""",

    "bandit": """
——————————————————————––––––––
   You trip and fall in a 
  ditch, breaking your ankle!
          -8 Health
——————————————————————––––––––
       Choose an option.

  1. Continue 
——————————————————————––––––––""",

    "cave": """
——————————————————————––––––––
Uh oh. While you were sleeping 
a bear cub came in and ate all 
   your snacks! And a chunk 
      of your leg too... 
    -2 treats   -3 Health
——————————————————————––––––––
       Choose an option.
    
  1. Continue
——————————————————————––––––––"""
}

def PlayerDeathCheck():
    if player_health <= 0:
            print("You were defeated. Game over.")
            quit()

def FinalFight():
    global player_health, treats, decision, boss_health
    TREE_DAMAGE = random.randint(0, 9)
    PLAYER_DAMAGE = random.randint(3, 10) 
    treats = random.randint(2, 8)
    try:

            chosen_prompt_outcome = random.choice(["tree_swing", "tree_defense", "tree_dodge"])

            if chosen_prompt_outcome == "tree_swing":
                player_health -= TREE_DAMAGE
                print(f"""
            ——————————————————————––––––––
               The Tree Elder swings a 
                    branch at you
                -{TREE_DAMAGE} Health
            ——————————————————————––––––––
            Tree Elder: {boss_health}/30
            You: {player_health}/25
            ——————————————————————––––––––
                Choose an option.

            1. Keep fighting
            2. Eat a treat
            ——————————————————————––––––––""")
                PlayerDeathCheck()
                
                decision = int(input())

                QuitGame(decision)

                if decision == 8:
                    StatsMenu()
                    FinalFight()
                    return

                elif decision == 1:
                    FinalFight()
                    return

                elif decision == 2:
                    if treats > 0:
                        player_health += 5
                        treats -= 1
                        FinalFight()
                        return
                    elif treats <= 0:
                        print("You don't have enough treats for that!")
                        FinalFight()
                        return
                    else:
                        print("Please enter a valid number!")
                        FinalFight()
                        return
                else:
                    print("Please enter a valid number!")
                    FinalFight()
                    return
            
            elif chosen_prompt_outcome == "tree_defense":
                boss_health -= PLAYER_DAMAGE

                # Check if the bandit is defeated
                if boss_health <= 0:
                    print(f"""
        ——————————————————————––––––––
        You defeated the Tree Elder!
        You beat the game well done!
        ——————————————————————––––––––
            Choose an option.

        1. Quit Game
        ——————————————————————––––––––
        """)
                    int(input())

                    quit()

                else:
                    print(f"""
        ——————————————————————––––––––
            You punch the Tree Elder.
        You deal {PLAYER_DAMAGE} damage.
        ——————————————————————––––––––
        Tree Elder: {boss_health}/30
        You: {player_health}/25
        ——————————————————————––––––––
            Choose an option.

        1. Keep fighting
        2. Eat a treat
        ——————————————————————––––––––""")
                    decision = int(input())
                    QuitGame(decision)

                    if decision == 8:
                        StatsMenu()
                        FinalFight()
                        return

                    elif decision == 1:
                        FinalFight()
                        return

                    elif decision == 2:
                        if treats > 0:
                            player_health += 5
                            treats -= 1
                            FinalFight()
                            return
                        elif treats <= 0:
                            print("You don't have enough treats for that!")
                            FinalFight()
                            return
                        else:
                            print("Please enter a valid number!")
                            FinalFight()
                            return
                    else:
                        print("Please enter a valid number!")
                        FinalFight()
                        return

            elif chosen_prompt_outcome == "tree_dodge":
                player_health -= TREE_DAMAGE
                print(f"""
        ——————————————————————––––––––
        You try to kick the Tree Elder.
        You miss and he lands a blow.
            -{TREE_DAMAGE} Health
        ——————————————————————––––––––
        Tree Elder: {boss_health}/30
        You: {player_health}/25
        ——————————————————————––––––––
            Choose an option.

        1. Keep fighting
        2. Eat a treat
        ——————————————————————––––––––""")
                PlayerDeathCheck()

                decision = int(input())
                QuitGame(decision)

                if decision == 8:
                    StatsMenu()
                    FinalFight()
                    return

                if decision == 1:
                    FinalFight()
                    return
                elif decision == 2:
                    if treats > 0:
                        player_health += 5
                        treats -= 1
                        FinalFight()
                        return
                    elif treats <= 0:
                        print("You don't have enough treats for that!")
                        FinalFight()
                        return
                else:
                    print("Please enter a valid number!")
                    FinalFight()
                    return

    except ValueError:
        print("Please enter a valid number.")
        FinalFight()
        return

def FinalFightStart():
    global player_health, treats, scenario_2, decision, boss_health
    boss_health = 30
    try:    
        print("""
        ——————————————————————––––––––
        You enter a dark clearing.
        A towering figure appears…
        ——————————————————————––––––––
            It's the Tree Elder!
            Choose an option.

        1. Fight it 
        ——————————————————————––––––––""")
        decision = int(input())
        if decision == 1:
            FinalFight()
        if decision == 8:
            StatsMenu()
            FinalFightStart()
            return
        else:
            print("Please enter a valid number.")

    except ValueError:
        print("Please enter a valid number.")
        
        

def ClearingLoop():
    global treats, scenario_2, decision
    try:
        chosen_prompt_outcome = random.choice(list(scenario_outcomes_clearing))
        print(chosen_prompt_outcome)
        decision = int(input())

        QuitGame(decision)

        if decision == 8:
            StatsMenu()
            ClearingLoop()
            return


        if scenario_outcomes_clearing.get(chosen_prompt_outcome) == "clearing_1":
            QuitGame(decision) 

            if decision == 1:
                scenario_2 = True
                PlayScenario()
            else:
                print("Please enter a valid number!")
                ClearingLoop()

        elif scenario_outcomes_clearing.get(chosen_prompt_outcome) == "clearing_2":
            QuitGame(decision)

            if decision == 1:
                scenario_2 = True
                PlayScenario()
            elif decision == 2:
                print(rare_outcomes.get("clearing"))
                treats += 2
                decision = int(input())
                QuitGame(decision)

                if decision == 8:
                    StatsMenu()
                    BanditFightLoop()
                    return

                elif decision == 1:
                    scenario_2 = True
                    PlayScenario()

                else:
                    print("Please enter a valid number!")
                    ClearingLoop()
            else:
                print("Please enter a valid number!")
                ClearingLoop()

    except ValueError:
        print("Please enter a valid number!")
        ClearingLoop()

def BanditBefriendLoop():
    global scenario_2, player_health, treats, decision
    try:
        chosen_prompt_outcome = random.choice(list(scenario_outcomes_bandit))
        print(chosen_prompt_outcome)
        decision = int(input())
        
        QuitGame(decision)

        if decision == 1:
            scenario_2 = True
            PlayScenario()
            return
        
        elif decision == 8:
            StatsMenu()
            return

        if scenario_outcomes_bandit.get(chosen_prompt_outcome) == "bandit_1":

            if decision == 1:
                scenario_2 = True
                treats += 3
                PlayScenario()
                return

            elif decision == 8:
                treats += 3
                StatsMenu()
                return
                
            else:
                print("Please enter a valid number!")
                BanditBefriendLoop()
                
        elif scenario_outcomes_bandit.get(chosen_prompt_outcome) == "bandit_2":
            PlayerDeathCheck()
            QuitGame(decision)

            if decision == 1:
                player_health -= 3
                scenario_2 = True
                PlayScenario()
                return

            elif decision == 2:
                player_health -= 3
                print(rare_outcomes.get("bandit"))
                player_health -= 8
                PlayerDeathCheck()
            
                decision = int(input())
                
                QuitGame(decision)

                if decision == 1:
                    player_health -= 3
                    scenario_2 = True
                    PlayScenario()
                    return

                elif decision == 8:
                    player_health -= 3
                    StatsMenu()
                    return
                
                else:
                    print("Please enter a valid number!")
                    BanditBefriendLoop()
                    return
        else:
            print("Please enter a valid number!")
            BanditBefriendLoop()
  
    except ValueError:
            print("Please enter a valid number!")

def BanditFightLoop():
    global scenario_2, player_health, treats, bandit_health, decision

    BANDIT_DAMAGE = random.randint(1, 7)
    PLAYER_DAMAGE = random.randint(3, 6)  

    try:
        chosen_prompt_outcome = random.choice(["bandit_kick", "bandit_defense", "bandit_dodge"])

        if chosen_prompt_outcome == "bandit_kick":
            player_health -= BANDIT_DAMAGE
            print(f"""
——————————————————————––––––––
    The bandit kicks you.
    -{BANDIT_DAMAGE} Health
——————————————————————––––––––
Bandit: {bandit_health}/10
You: {player_health}/25
——————————————————————––––––––
      Choose an option.

  1. Run away
  2. Keep fighting
——————————————————————––––––––""")
        PlayerDeathCheck()

        if chosen_prompt_outcome == "bandit_defense":
            bandit_health -= PLAYER_DAMAGE

            # Check if the bandit is defeated
            if bandit_health <= 0:
                print(f"""
——————————————————————––––––––
   You defeated the bandit!
     He droped 2 treats!
    +2 Treats   +8 Health
——————————————————————––––––––""")
                treats += 2
                player_health += 8
                bandit_health = 10  
                scenario_2 = True
                return  
            else:
                print(f"""
——————————————————————––––––––
    You punch the bandit.
    You deal {PLAYER_DAMAGE} damage.
——————————————————————––––––––
Bandit: {bandit_health}/10
You: {player_health}/25
——————————————————————––––––––
      Choose an option.

  1. Run away
  2. Keep fighting
——————————————————————––––––––""")

        elif chosen_prompt_outcome == "bandit_dodge":
            player_health -= BANDIT_DAMAGE
            print(f"""
——————————————————————––––––––
  You try to kick the bandit,
 you miss and he lands a blow.
   -{BANDIT_DAMAGE} Health
——————————————————————––––––––
Bandit: {bandit_health}/10
You: {player_health}/25
——————————————————————––––––––
      Choose an option.

  1. Run away
  2. Keep fighting
——————————————————————––––––––""")
        PlayerDeathCheck()

        # Ask what player wants to do next
        decision = int(input())
        QuitGame(decision)

        if decision == 8:
            StatsMenu()
            BanditFightLoop()
            return

        elif decision == 1:
            scenario_2 = True
        elif decision == 2:
            BanditFightLoop()
            return
        else:
            print("Please enter a valid number!")
            BanditFightLoop()

    except ValueError:
        print("Please enter a valid number!")
        BanditFightLoop()



def CaveLoop():
    global scenario_2, treats, player_health, decision
    try:
        chosen_prompt_outcome = random.choice(list(scenario_outcomes_cave))
        print(chosen_prompt_outcome)
        decision = int(input())
        QuitGame(decision)

        if decision == 8:
            StatsMenu()
            CaveLoop()
            return

        elif decision == 1:
            scenario_2 = True
            PlayScenario()
            
        elif decision == 2 and scenario_outcomes_cave.get(chosen_prompt_outcome) == "cave_2":
            treats -= 2
            player_health -= 3
            PlayerDeathCheck()
            print(rare_outcomes.get("cave"))
            decision = int(input())

            QuitGame(decision)

            if decision == 8:
                StatsMenu()
                return
            
            elif decision == 1:
                scenario_2 = True
                PlayScenario() 
                return
            
            else:
                print("Please enter a valid number!")

            scenario_2 = True
            PlayScenario()
            return
        
    except ValueError:
            print("Please enter a valid number!")
            CaveLoop()

def PlayScenario():
    global scenario_2, scenario_counter, boss_fight_check, decision

    if boss_fight_check == True:
        FinalFightStart()
        return

    while scenario_2 == True:

        chosen_prompt = random.choice(list(scenarios))
        print(chosen_prompt)

        if scenario_counter >= 6:
            scenario_2 = False
            boss_fight_check = True

        try:

            decision = int(input())
            QuitGame(decision)
        
            if decision == 8:
                StatsMenu()
                return

            if scenarios.get(chosen_prompt) == "cave":
                scenario_counter += 1
                if decision == 1:
                    scenario_2 = True
                    
                elif decision == 2:
                    scenario_2 = False
                    CaveLoop()
                    return
                else:
                    print("Please enter a valid number!")

            elif scenarios.get(chosen_prompt) == "bandit":
                scenario_counter += 1
                if decision == 1:
                    scenario_2 = False
                    BanditBefriendLoop()
                    return

                elif decision == 2:
                    scenario_2 = False
                    BanditFightLoop()
                    return
                else:
                    print("Please enter a valid number!")

            elif scenarios.get(chosen_prompt) == "clearing":
                scenario_counter += 1
                if decision == 1:
                    scenario_2 = True

                elif decision == 2:
                    scenario_2 = False
                    ClearingLoop()
                    return
                else:
                    print("Please enter a valid number!")
                    PlayScenario()
                    return

            else:
                print("Please enter a valid number!")
                decision = int(input(chosen_prompt))
                PlayScenario()

        except ValueError:
            print("Please enter a valid number!")
            decision = int(input(chosen_prompt))

# asks user if they want to play, if invalid awnser is said it loops and asks again
while start_decision == False:
    try:
        print(
        """
        ——————————————————————––––––––
               Hi! Welcome to
           AS91896 Text Adventure! 
        ——————————————————————––––––––
           Would you like to play?

          1 = Yes
          2 = No
        ——————————————————————––––––––""")
        temp = int(input())

    except ValueError:
        print("Please enter a valid number!")

# if 1 is entered game starts, if 2 is entered game ends
    else:
        if temp == 1:
            playing_status = True
            start_decision = True
        elif temp == 2:
            scenario_2 = False
            start_decision = True
            playing_status = False
            print("Thanks for playing!")
            quit()

# prints user manual with all the controls, if 9 is pressed game quits, if 8 is pressed stats are printed, if any other number is pressed game starts
while playing_status == True:
    try:  
        print("""
        ——————————————————————––––––––
                 User Manual
        ——————————————————————––––––––
            Enter these letters to 
            use these functions at 
                 any time.

          9 - Quit game
          8 - Check stats

          Good luck on your journey!
         Press Any Number to Continue
        ——————————————————————––––––––""")
        decision = int(input())
        
        # quit game
        QuitGame(decision)

        # stats menu
        if decision == 8:
            StatsMenu()
        # starts game
        else:
            current_scenario = True
            playing_status = False
    
    except ValueError:
        decision = None
        print("Please enter a valid number!")
        first_decision = False
        current_scenario = False

first_decision = current_scenario

# starts scenario 1
while first_decision == True:
    try:
        print(start.get("start_scenario"))
        decision = int(input())

        QuitGame(decision)

        if decision == 1:
            first_decision = False
            scenario_2 = False
            playing_status = False
        elif decision == 2:
            first_decision = False
            scenario_2 = False
            print("You got lost and perished. Thanks for playing!")
            quit()
        elif decision == 8:
            StatsMenu()
        else:
            print("Please enter a valid number!")

    except ValueError:
        print("Please enter a valid number!")

scenario_2 = current_scenario

if scenario_counter >= 6:
    scenario_2 = False
    FinalFightStart()

scenario_2 = True
while scenario_2:
    PlayScenario()


