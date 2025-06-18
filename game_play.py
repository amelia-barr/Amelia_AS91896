
start = {
    "start_senario": """
    ——————————————————————––––––––
      You find yourself at the 
          edge of a forest.
    ——————————————————————––––––––
          Choose one path.

    1. Continue through the forest
    2. Turn back
    ——————————————————————––––––––"""    
}

senarios = {
    "cave": """
    ——————————————————————––––––––
    You come across a small cave.
    ——————————————————————––––––––
          Choose an option.

      1. Set up camp/sleep there
      2. Continue on.
    ——————————————————————––––––––""",

    "bandit": """
    ——————————————————————––––––––
    As the path becomes more rugged 
    You start to feel eyes watching you…
    ——————————————————————––––––––
        A bandit has appeared!
          Choose an option.

      1. Try to befriend him
      2. Fight him
    ——————————————————————––––––––""",

    "clearing": """
    ——————————————————————––––––––
        You found a clearing!
    ——————————————————————––––––––
          Choose an option.

      1. Continue
      2. Explore
    ——————————————————————––––––––""",}
key_senarios = list(senarios.keys())

clearing = {
    "outcome1":"""
    ——————————————————————
    You tripped! -1 Health
    ——————————————————————
       Choose an option.

      1.  Continue

    ——————————————————————""",
    
}