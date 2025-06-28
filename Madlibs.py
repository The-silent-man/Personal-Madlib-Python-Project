# Note that the Madlibs are not created by me there were done with ChatGPT.
# The code however, is mine 

# The A Day at the Zoo by chatGPT
def A_Day_at_the_Zoo():
    print("Tell me an Adjective, Ex. Blue (Description)")
    adjective_1 = input()
    print("tell me the name of an Animal, Ex. Cats")
    Animal_1 = input()
    print("tell me an verb in the past tense, Ex. Wrote (past action)")
    Verb_past_tense = input()
    print("tell me an Noun Ex. John (name), Computer (item), United States (place)")
    Noun_1 = input()
    print("tell me an Adjective")
    Adjective_2 = input()
    print("tell me an Plural Noun, Ex. Discs, Dogs,")
    Plural_noun_1 =input()
    print("tell me a Verb that ends with -ing")
    Verb_ending_in_ing_1 = input()
    print("tell me an Adjective")
    Adjective_3 = input()
    print("tell me an Verb Ex. Run, (action)")
    Verb_1 = input()
    print("tell me an Exclamation, Ex. GREAT SCOTT!")
    Exclamation_1 = input()
    print(f"""'-----------------------------------------------------------------------------------------------\n'
    'Today I went to the zoo, and it was the most {adjective_1} day ever!\n'
    'First, I saw a {Animal_1} that {Verb_past_tense} right in front of a {Noun_1}.\n'
    'Then I fed some {Adjective_2} {Plural_noun_1} while they were {Verb_ending_in_ing_1}.\n'
    'Later, I watched a {Adjective_3} monkey {Verb_1} across the cage.\n'
    'I couldn’t believe my eyes and shouted, “{Exclamation_1}!”\n'
    'Best. Zoo trip. Ever.\n'
    '-----------------------------------------------------------------------------------------------'""")
    return repeat_or_no()
# The My Crazy Family Story by chatGPT
def My_Crazy_Family():
    print("Tell me an Adjective, Ex. Blue (Description)")
    adjective1 = input()
    print("tell me the name for a relative, Ex. Uncle,Dad,Cousin,Sister")
    Relative = input()
    print("tell me a Verb that ends with -ing")
    Verb_ending_in_ing_1 = input()
    print("tell me an Noun Ex. John (name), Computer (item), United States (place)")
    Noun_1 = input()
    print("tell me an Adjective")
    Adjective_2 = input()
    print("tell me an Plural Noun, Ex. Discs, Dogs,")
    Plural_noun_1 = input()
    print("tell me an Adjective")
    Adjective_3 = input()
    print("tell me an Verb Ex. Run, (action)")
    Verb_1 = input()
    print("tell me the name of a Celebrity")
    Celebrity = input()
    print(f"""'-----------------------------------------------------------------------------------------------\n'
    'My family is totally {adjective1}\n'
    'My {Relative} is always {Verb_ending_in_ing_1} with a {Noun_1} on their head.\n'
    'We eat {Adjective_2} {Plural_noun_1} for dinner and then {Verb_1} until bedtime.\n'
    'Last weekend, we dressed up in {Adjective_3} costumes and pretended to be {Verb_1} while dancing on the kitchen. {Celebrity}.\n'
    'Even our dog thinks we're weird and hides under the {Noun_1}!”\n'
    'And honestly? I love it.\n'
    '-----------------------------------------------------------------------------------------------'""")
    return repeat_or_no()
# The The Weirdest Day Ever by chatGPT
def The_Weirdest_Day_Ever():
    print("Tell me a day of the Week)")
    Day_of_the_Week = input()
    print("tell me an Noun Ex. John (name), Computer (item), United States (place)")
    Noun_1 = input()
    print("tell me an verb in the past tense, Ex. Wrote (past action)")
    Verb_past_tense_1 = input()
    print("Tell me an Adjective, Ex. Blue (Description)")
    Adjective = input()
    print("tell me the name of an Animal, Ex. Cats")
    Animal = input()
    print("tell me a Verb that ends with -ing")
    Verb_ending_in_ing_1 = input()
    print("tell me an Exclamation, Ex. GREAT SCOTT!")
    Exclamation_1 = input()
    print("tell me an Noun")
    Noun_2 = input()
    print("tell me an Plural Noun, Ex. Discs, Dogs,")
    Plural_Noun = input()
    print("tell me another Noun")
    Noun_3 = input()
    print("tell me an adjective")
    Adjective_2 = input()
    print("tell me another adjective")
    Adjective_3 = input()
    print(f"""'-----------------------------------------------------------------------------------------------\n'
    'It all started on a {Day_of_the_Week} morning when I woke up and found a {Noun_1} in my bed\n'
    'I {Verb_past_tense_1} out of the room and ran into a  {Adjective} {Animal} {Verb_ending_in_ing_1} in the hallway.\n'
    '"{Exclamation_1}!" I shouted.\n'
    'I tripped over a {Noun_2}, landed in a pile of {Plural_Noun}, and somehow ended up in a {Adjective_2} costume\n'
    'When I finally made it outside, a stranger handed me a {Noun_3} and said, “You are our only hope!”\n'
    'Yeah… definitely the weirdest day ever.\n'
    '-----------------------------------------------------------------------------------------------'""")
    return repeat_or_no()

def repeat_or_no():
    print("Wanna do another/repeat the madlib?\n"
          "Yes or No?")
    response = input()
    if response == "Yes" or response == "no":
        pl_response()
    elif response =="No" or response == "no":
        print("Ah well, goodbye then.")
    else:
        print('I say again')
        repeat_or_no()
    
#chooses the madlib the player choses
def pl_response():
    print(
    "Hello Welcome to the game of mad libs!\n"
    "What Mad Lib do you want to play?\n"
    "A Day at the Zoo (1), My Crazy Family (2) or The Weirdest Day Ever (3)"
    )
    response = input()
    if response == "1":
        return A_Day_at_the_Zoo()
    elif response == "2":
        return My_Crazy_Family()
    elif response == "3":
        return The_Weirdest_Day_Ever()
    else:
        print("Hey you must have typed somthing wrong.\n"
        "type the mad lib that corresponds to the number\n"
        "next to it")
        pl_response()

pl_response()
