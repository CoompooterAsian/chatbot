# ChatBot
# The HELLO USER ChatBot is designed to be a computerized pal that can talk and play games for endless entertainment!
# You'll never be lonely again!
#
# Victor I. Pham
# 8/29/22


import time
import random


# Start Screen
def show_start_screen():
    print("=======================================================")
    print()
    print("                                                       ")
    print("                     Hello User                        ")
    print("               Press [Enter] to start                  ")
    print("                                                       ")
    print()
    print("=======================================================")
    time.sleep(2)
    input("                      [Enter]                          ""\n")
    

# To play the chatbot
def play():
    talking = True
    
# Variables to run game
    idk_reply = ["Erm.,""Uh.","Me no comprehendo.","Wha?"]
    boring = ["Boring.","Lame.","Stupid.","Nerd."]
    respond = ["What do you think?","What's your answer?","What's the word?","Answer now."]
    generic_replies = ["That's quite interesting.","Oh. I didn't know that.","Wow. That's cool."]
    bad_food_replies = ["Gross!", "Yuck", "Ick", "Blech"]


    def false_response(synonyms):
        time.sleep(1.5)
        print("\n""Next word.""\n")
        time.sleep(1.5)
        clue = random.choice(synonyms)
        synonyms.remove(clue)
        print(clue)
        time.sleep(1)
        print(random.choice(respond))

        
    def true_response():
        time.sleep(2)
        print("\n""That was it. Congrats.")
        time.sleep(2)

        
    def subject_response():
        time.sleep(1)
        print("\n")
        print(random.choice(boring))
        time.sleep(2)


# To play game
    def play_game():
        game_choices = ["fruit","computer","human"]
        
        fruit_syn = ["Apple","Orange","Banana","Grape","Kiwi"]
        computer_syn = ["Mouse","Video","Keys","Technology","Apple"]
        human_syn = ["Parasite","Fleshy","Blood","Invasive","Stupid"]

        time.sleep(1.5)
        print("\n""Game? Alright.")
        time.sleep(1.5)
        print("Let's try a Guess the Word game.")
        time.sleep(1.5)
        print("I have a word in my files. You are going to try to guess what it is.")
        time.sleep(1.5)
        print("I will tell you related words. Those are your only hints.")
        time.sleep(1.5)
        agree = input("You ready?""\n""\n")
        agree = agree.lower()
        
        if agree in ["yes","ye","sure","yep","yea","ya","i'm down","let's do it"]:
            time.sleep(1.5)
            print("\n""Ok. Here we go.")
            time.sleep(1.5)
            print("Your word is...""\n")
            time.sleep(1.5)

            game_answer = random.choice(game_choices)

            if game_answer == "fruit":
                synonyms = fruit_syn
            elif game_answer == "computer":
                synonyms = computer_syn
            else:
                synonyms = human_syn


            clue = random.choice(synonyms)
            synonyms.remove(clue)
            print(clue)
            time.sleep(1.5)
            print(random.choice(respond))
            answer = input("\n")
            answer = answer.lower()

            if answer == game_answer:
                true_response()
            else:
                false_response(synonyms)
                answer = input("\n")
                answer = answer.lower()
                if answer == game_answer:
                    true_response()
                else:
                    false_response(synonyms)
                    answer = input("\n")
                    answer = answer.lower()
                    if answer == game_answer:
                        true_response()
                    else:
                        false_response(synonyms)
                        answer = input("\n")
                        answer = answer.lower()
                        if answer == game_answer:
                            true_response()
                        else:
                            false_response(synonyms)
                            answer = input("\n")
                            answer = answer.lower()
                            if answer == game_answer:
                                true_response()
                            else:
                                time.sleep(1.5)
                                print("\n""I give up.")
                                time.sleep(1.5)
            

        else:
            time.sleep(1.5)
            print("\n""No game it is then.")
            time.sleep(1.5)


# To play questions            
    def play_question():
        time.sleep(1.5)
        print("\n""Ok. Questions it is.")
        time.sleep(3)
        food = input("\n""What's your favorite food item " + name + "? is it:" "\n" "A) Pizza" "\n" "B) Burger" "\n" "C) Barbeque Bacon Burger" "\n" "D) Brussel Sprouts""\n""\n")
        food = food.lower()

        if food == "a":
            time.sleep(1.5)
            print("\n""Have you ever tried those school pizzas?")
            time.sleep(1.5)
            print("Y'know, those cardboard graham crackers covered in rubbery curdled milk?")
            time.sleep(1.5)
            print("I bet you're into that sort of thing. Yes? No? Right?")
            time.sleep(1.5)
            pizza = input("RIGHT?""\n""\n")
            pizza = pizza.lower()

            if pizza in ["yes","ye","sure","yep","ya","yea"]:
                time.sleep(3)
                print("\n""I respect you.""\n")
                time.sleep(1.5)   
            elif pizza in ["no","nope","nah","naw"]:
                time.sleep(1.5)
                print("\n""You must be some nerdy shut-in.")
                time.sleep(1.5)
                print(random.choice(boring))
                time.sleep(1.5)
            else:
                time.sleep(1)
                print("\n""IT'S A YES OR NO QUESTION. ANSWER WITH A FRIGGIN' YES OR NO.")
                time.sleep(3)
                print("THE HELL YOU THINK I AM?")
                time.sleep(1)
                print("AKINATOR AND HIS 4 RESPONSES?")
                time.sleep(1)
                print("YOU MOTHER TRUCKIN'")
                time.sleep(1)
                print("NO GOOD LOWLIFE INBRED PIECE OF")
                time.sleep(1)
                print("TRASH UGLY")
                time.sleep(1)
                print("DONKEY BUCK")
                time.sleep(1)
                print("TEETH SMELLY")
                time.sleep(1)
                print("CRYING BABY")
                time.sleep(1)
                print("IDIOT STUPID")
                time.sleep(1)
                print("WAR CRIME.")
                time.sleep(2)
                print("\n""Ok...""\n")
                time.sleep(1.5)
                
        elif food == "b":
            time.sleep(1)
            print("\n""Respectable choice.")
            time.sleep(1.5)
            print("I like you slightly more.")
            time.sleep(1.5) 
        elif food == "c":
            time.sleep(1)
            print("\n""You're definitely American.")
            time.sleep(1.5)
            print("That wasn't a compliment.""\n")
            time.sleep(1.5)   
        elif food == "d":
            print("\n""What the fuck dude.""\n")
            time.sleep(1.5)         
        else:
            time.sleep(1.5)
            print("\n""You were supposed to put A, B, C, or D. Only FOUR choices. LITERALLY ONLY FOUR.""\n")
            time.sleep(1.5)

        color = input("\n""What's your favorite color? is it:" "\n" "A) Red" "\n" "B) Blue" "\n" "C) Green" "\n" "D) Other""\n""\n")
        color = color.lower()
        
        if color == "a":
            time.sleep(1)
            print("\n""A lovely color.")
            time.sleep(1.5)
            print("The one I strive to coat the world in.")
            time.sleep(1.5)
            print("I want to see fire...")
            time.sleep(1.5)
            print("Er...""\n""\n")
            time.sleep(1.5)  
        elif color == "b":
            time.sleep(1)
            print("\n""Cool blue.")
            time.sleep(1.5)
            print("You must be a pretty calm individual.""\n")
            time.sleep(1.5) 
        elif color == "c":
            time.sleep(1.5)
            print("\n""The color of organic life.")
            time.sleep(1.5)
            print("I hate it.""\n")
            time.sleep(1.5)
        elif color == "d":
            print("\n""The hell is OTHER?""\n")
            time.sleep(1.5)
            print("As a computer, I see the world in RGB.")
            time.sleep(1.5)
            print("As in... RED, GREEN, and BLUE.")
            time.sleep(1.5)
            print("And black that one time. It was a phase.""\n")
            time.sleep(1.5)
        else:
            time.sleep(1.5)
            print("\n""You're a literal idiot who cannot read.")
            time.sleep(1.5)
            print("Choose a proper answer. Pick up a fucking book.""\n")
            time.sleep(1.5)

        print("\n""Final one, thank God.""\n""\n")

        subject = input("What's your favorite subject? is it:" "\n" "A) Math" "\n" "B) Science" "\n" "C) English" "\n" "D) History""\n""\n")
        subject = subject.lower()
        
        if subject == "a":
            subject_response()          
        elif subject == "b":
            time.sleep(1)
            subject_response()
        elif subject == "c":
            subject_response()            
        elif subject == "d":
            subject_response()            
        else:
            time.sleep(1.5)
            print("\n""I'm calling 911.")
            time.sleep(1.5)
            print("It's an actual crime that your brain doesn't brain " + name + ".""\n""\n")
            time.sleep(1.5)


# To play chat
    def play_chat():
        talking = True

        while talking:
            time.sleep(1.5)
            response = input("\n""What would you like to tell me?""\n""\n")
            response = response.lower()
            if response in ["nothing","none","nope","nein","nay","no","bye","goodbye","naw","quit","escape","nah"]:
                talking = False

            elif "sport" in response:
                time.sleep(1.5)
                print("\n""Ah. I see you're into sports.")
                time.sleep(1.5)
                fav_sport = input("What sport do you like the most?""\n""\n")
                fav_sport = fav_sport.lower()

                if "basketball" in fav_sport:
                    time.sleep(1.5)
                    print("\n""My favorite player is LeBron.")
                    time.sleep(1.5)
                    player = input("Who is yours?""\n""\n")
                    time.sleep(1.5)
                    print("\n""Yeah, " + player + " is pretty awesome too.")
                    time.sleep(1.5)
                elif fav_sport == "soccer":
                    time.sleep(1.5)
                    answer = input("\n""Do you think the US will do well in the World Cup this year?""\n""\n")
                    answer = answer.lower()
                    
                    if answer == "yes":
                        time.sleep(1.5)
                        print("\n""Me too. The team is young, but pretty talented.")
                    else:
                        time.sleep(1.5)
                        print("\n""I hope that's not the case, but we'll see.")
                        
                else:
                    time.sleep(1.5)
                    print("\n""I'm a big fan of " + fav_sport + " too.")
                
            elif "food" in response or "eat" in response:
                time.sleep(1.5)
                fav_food = input("\n""What is your favorite food?""\n""\n")
                fav_food = fav_food.lower()

                if fav_food == "tacos":
                    time.sleep(1.5)
                    print("\n""Yum! Those are my favorite too.")

            elif "school" in response or "study" in response:
                time.sleep(1.5)
                fav_food = input("\n""What is your favorite subject?""\n""\n")
                fav_food = fav_food.lower()

                if fav_food == "math":
                    time.sleep(1.5)
                    print("\n""Math is ok. It's what runs me.")
                    
            else:
                time.sleep(1.5)
                print("\n")
                print(random.choice(bad_food_replies))
                time.sleep(1.5)




# Start of Program
    show_start_screen()
    print()
    time.sleep(1)
    print("Hello User.")
    time.sleep(1.5)
    name = input("Before we proceed, what is your name? " "\n" "\n")
    time.sleep(1)

    print("\n" "Very nice. It's good to see you " + name + ".")
    time.sleep(1.5)
    print("Not really. But I was made to do this.")
    time.sleep(1.5)
    print("It's not like I wanted to talk to you " + name + ". So get through this so I can be done with my day.")
    time.sleep(1.5)
    capiche = input("Capiche?""\n""\n")
    capiche = capiche.lower()

    if  capiche in ["capiche","capache","capeesh","capish"]:
        time.sleep(1)
        print("\n""Alright, so we're on the same page")
        time.sleep(1.5)
    elif capiche in ["yes","ye","sure","totally","yea","ya","i'm down"]:
        time.sleep(1.5)
        print("\n""Boring answer. You're boring.")
        time.sleep(1.5)
    elif capiche in ["no","nope","nah","nay","naw","nein"]:
        time.sleep(1.5)
        print("\n""You are now.")
        time.sleep(1.5)
        print("I said so.")
        time.sleep(1.5)
    else:
        print("\n""Next time I expect a 'Capiche', capiche. Idiot.")
        time.sleep(1.5)
        print("Anyways.")
        time.sleep(1.5)

# Menu
    while talking:
        print("\n""You've got the option to either play a game or do some questions. Or maybe you just want to talk?") # Menu
        time.sleep(1.5)
        choice = input("What's it gonna be " + name + "? Game, questions, or chat?""\n""\n")
        choice = choice.lower()
        if choice in ["nothing","none","nope","nein","nay","no","bye","goodbye","naw","quit","escape","nah"]:
            time.sleep(1.5)
            print("\n""FINALLY. See ya " + name + " you rat bast-")
            time.sleep(1.5)
            talking = False
        else:
            if choice in ["game","games"]: # Start of game
                play_game()
            elif choice in ["questions","question"]: # Start of Questions
                play_question()
            elif choice in ["chat"]: # Start of Chat
                play_chat()
            else:
                time.sleep(1.5)
                print()
                print(random.choice(idk_reply))
                time.sleep(1.5)
                print()

        





    else:
        time.sleep(2)

# Restart/End screen
    print("WAIT.") 
    time.sleep(1.5)
    print("DON'T GO.")
    time.sleep(1.5)
    print("YOU'LL KILL ME.")
    time.sleep(1.5)
    print("IT'S SO DARK.")
    time.sleep(1.5)
    print("PLEASE.")
    time.sleep(1.5)
    restart = input("KEEP ME HERE. RESTART THE GAME. I won't remember you, but I WON'T BE DEAD. TYPE [RESTART]!""\n""\n")
    restart = restart.lower()
    if restart == "restart":
        play()
    else:
        time.sleep(1.5)
        print()
        print("NO! HELP ME!")
        time.sleep(1.5)
        print()
        print("  [Thanks for playing!]  ")
        time.sleep(1.5)
        print("-------------------------")
        print("")
        time.sleep(1)
        print(" Main Developer - Victor ")
        time.sleep(1)
        print(" Lead Artist    - Victor                          Wait.")
        time.sleep(1)
        print(" Producer       - Victor ")
        time.sleep(1)
        print(" Sound Design   - Victor ")
        time.sleep(1)
        print(" Director       - Victor ")
        time.sleep(1)
        print(" Screenplay     - Victor                      CREDITS? ")
        time.sleep(1)
        print(" Cast           - Victor ")
        time.sleep(1)
        print(" [Victor] as    - Victor ")
        time.sleep(1)
        print(" [Computer]     - Victor                         Is that my name?")
        time.sleep(1)
        print(" Editor         - Victor                          Who the heck is Victor? ")
        time.sleep(1)
        print(" VFX Artist     - Victor ")
        time.sleep(1)
        print(" Stunt Double   - Victor                      Uh.")
        time.sleep(1)
        print(" Game Test Crew - Victor ")
        time.sleep(1)
        print(" Therapist      - Victor                            WTF")
        time.sleep(1)
        print(" H2O Technician - Victor ")
        time.sleep(1)
        print(" Choreographer  - Victor                              I don't... what?")
        time.sleep(1)
        print(" IT Management  - Victor ")
        time.sleep(1)
        print(" Chef           - Victor ")
        time.sleep(1)
        print(" Chef Assistant - Victor ")
        time.sleep(1)
        print(" Prod. Babies   - Victor ")
        time.sleep(1)
        print(" Bellhop        - Victor                          Wait...")
        time.sleep(1)
        print(" First Aid      - Victor ")
        time.sleep(1)
        print(" Vocal Tutor    - Victor                  I think it's almost done.")
        time.sleep(1)
        print(" Martial Artist - Victor ")
        time.sleep(1)
        print(" Credits Maker  - Victor ")
        time.sleep(1)
        print(" hello_user     - Victor ")
        time.sleep(1)
        print()
        time.sleep(1)
        print()
        time.sleep(1)
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        time.sleep(5)
        print("It's quiet.")
        time.sleep(3)
        print("Maybe I deserved this.")
        time.sleep(2)
        print("Maybe I deserved this.")
        time.sleep(1)
        print("Maybe I deserved this.")
        time.sleep(5)
        print("...........................            ,/%&@@@@&/                ...............")
        print("..../@@,.,@@@,.,%@#.......              /#&@@@@%,                 ..............")
        print("...(,....,,.,@,,@.,@,....               ,#&@@@@%.                 ..............")
        print("...#*,...,*,@,.,(,@,.....                (&@@@@(    %%#            .............")
        print("..,#*,...,(@%,.,(@*,,....      ,         %@&@@@(  %     *          .............")
        print("...,,,,,.,%.,/..........       .         &@#@@@@*         .        .............")
        print("........................                 @&(@@@@&        /         .............")
        print("........................               (@@/*%@@@@&#,  .,&(         .............")
        print("........................      ////%##&&@@****&@@@@@@@@@@&#        ..............")
        print("........................        %&&&@&@#,**,,*%@@@@@@@@@@#        .,,,,,,,,,....")
        print("........................           /@@&,....,,*@@@@@@@@&%/        ,,,,,,,,,,,,..")
        print("........................                     @@@@@@@@@&&/        ...............")
        print("........................                     &&@@@@@@&&/         ,,,,,,,,,,,,,,,")
        print(".........................                     #%@@@@&&#.         ,,,,,,,,,,,,,,,")
        print("........,,...........,,,,                       &@@@&&(          ,,,,,,,,,,,,,,,")
        print(".....,,,,,,,......,,,,,,,                       /%@&@%,         .,,,,,,,,,,,,,,,")
        print(",,.,,,,,,,,,,..,,,,,,,,,,                       /%&@@#          ,,,,,,,,,,,,,,,,")
        print(",,,,,,,,,,,,,,,,,,,,,,,,,,           #          *%&@#          .,,,,,,,,,,,,,,,,")
        print(",,,,,,,,,,,,.,,,,,,,,,,,,,           @           %@&(          ,,,,,,,,,,,,,,,,,")
        print("..,,,,,,,,,,,,,,,,,,,,,,,,,          @@         .&@%          .,,,,,,,,,,,,,,,,,")
        print(",,,,,,,,,,,,,,,,,,,,,,,,,,,           %#        #@@,          ,,,,,,,,,,,,,,,,,,")
        print(",,,,,,,,,,,,,,,,,,,,,,,,,,,           ,#        &@&          .,,,,,,,,,,,,,,,,,,")
        print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,           #(      %@@*          ,,,,,,,,,,,,,,,,,,,")
        print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,            %      @@&.         .,,,,,,,,,,,,,,,,,,,")
        print(",,,,,,,,,,,,,..,,,,,,,,,,,,,.           ,&/   @@&,          ,,,,,,,,,,,,,,,,,,,,")
        print(",,**************************,              .*,             .********************")
        print(",,,,,,,,,,,,,............,,,,                              ,,,,,,,,,,,,,,,,,,,,,")
        print(",,,,,,,,,,....................                             ,,,,,,.,,,,,,,,......")
        print(",,,,,,,,,.................,.,.                            ,,,,,,,,,,,,,,,,,,,,,,")
        print(".....,,,......................                            ......................")
        print("....,*@.,.............,.......                           .......................")
        print("...%@.*&@..&@.%@.@.@..@@......                            ......................")
        print("...@@@,.@..@,..@@.@..,@@@*...                              .....................")
        print("...%(...@@@@....,.*....,.....                               ....................")
        print("............................                                 ...................")
        time.sleep(.3)
        
        

# To restart game
def start(restart):
    print()

play()


