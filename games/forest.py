import time
from othercodes import othercodes


def startforestgame():

    # the list to store the places you went to already
    exploration = []
    # names of things
    oceanid = "oceanid"
    # final quest attempt, once it reaches 3, death
    puzzleattempts = 0

    print("Let your imagination go wild. (￢‿￢ )")
    time.sleep(3)
    print("You are an adventurer who has nothing equipped, nor a bag. It doesn't discourage you though, so \n"
          "you decide to explore a forest you've always been meaning \n"
          "to explore and it seems that no one has dared to set foot on it. Just lovely. \n"
          "You wonder why that's the case as you start to make your way inside the forest.")
    print("Which area would you like to go first?")
    while True:
        if "t" in exploration:
            if "w" and "l" and "c" in exploration:
                print("")
                print("Congrats on clearing the forest game! I hope you enjoyed it! ヽ(・∀・)ﾉ")
                othercodes.continuedialogue()
                print("You have successfully explored what the forest offered, and got some neat equipments to continue your journey! \n"
                      "It was fun, but all good things must come to an end. There's that, but all the things you saw inside the \n"
                      "forest is gone, it must be because of that big tree... \n"
                      "after you bid your bittersweet goodbye to the forest, you head back to your home sweet home and start planning \n"
                      "your next journey")
                exploration.clear()
                othercodes.continuedialogue()
                winner = input("(1) exit game \n")
                if winner == "1":
                    break
                else:
                    print("Wrong input, but I'll let this one slide :)")
                    othercodes.continuedialogue()
                    break
        else:
            forestinput = input("(1) Waterfalls \n"
                                "(2) Big Tree \n"
                                "(3) Lake \n"
                                "(4) Cliff\n")

            if forestinput == "1":
                if "w" not in exploration:
                    print("waterfalls")
                    print("you see a water humanoid-like figure of what appears to be an oceanid. \n"
                          "she starts humming a song that made you feel very relaxed. It's a soothing melody indeed.")
                    othercodes.continuedialogue()
                    oceanidchoice = input("(1) Approach the oceanid \n"
                                          "(2) Head back later \n")
                    if oceanidchoice == "1":
                        yourchoice = input("(1) tackle \n"
                                           "(2) sing along \n"
                                           "(3) speak \n")
                        if yourchoice == "1":
                            tacklechoice = input("(1) full on tackle \n"
                                                 "(2) shout a battle cry while tackling! \n")
                            if tacklechoice == "1":
                                print("you start to tackle the oceanid like there's no tomorrow. \n"
                                      "as expected, you go through the oceanid's body and plunge down the water. \n"
                                      "'what was I thinking?' you thought to yourself. With no time to react, the oceanid \n"
                                      "suddenly it grew tenfold its size and started to keep you in a ball of water until you drowned to your...")
                                othercodes.continuedialogue()
                                print("death.")
                                print("game over.")
                                othercodes.continuedialogue()
                                break
                            elif tacklechoice == "2":
                                print("you screamed at the top of your lungs as you hurl towards the oceanid.\n"
                                      "'DEMACIA!!!' \n"
                                      "the oceanid gets startled but dodged your attack with ease. \n"
                                      "the oceanid begins to laugh at you as you plunge down the water\n" +
                                      oceanid + ": AH↓HA↑HA↑AH↓HA↑HA↑ , what were you thinking? You really thought that measly move can work on me? \n")
                                othercodes.continuedialogue()
                                print("she starts to imprison your whole body with condensed water except your head so you have room to breath. \n"
                                      "you can't seem to move any muscle no matter how hard you tried. \n"+
                                      oceanid + ": choose your words wisely mortal, while I'm still in the mood to speak. why did you approach me in such a manner?")
                                oceanidDialogue1 = input("(1) I just wanted to hug you... \n"
                                                         "(2) You tell me (smirk) \n")
                                if oceanidDialogue1 == "1":
                                    print(oceanid + ": a perfect being such as me hugged by someone like you? you must have a valid reason for that.")
                                    oceanidDialoque2 = input("(1) Your song was soothing \n"
                                                             "(2) Okay you got me, it wasn't a hug now let's fight! \n")
                                    if oceanidDialoque2 == "1":
                                        print(oceanid + ": as expected. I'm glad to know you have fine tastes. Care for a few more?")
                                        othercodes.continuedialogue()
                                        print("you enjoy another song from the oceanid, every note that was sung cleansed your soul. \n"
                                              "the oceanid was scary... but you're glad your life didn't end there and then.")
                                        othercodes.continuedialogue()
                                        print("it seems like the oceanid gave you a glowing stone.")
                                        othercodes.continuedialogue()
                                        print("obtained \n"
                                              "pharsa's glowing stone necklace: press the button and it turns into a necklace and summons a mini oceanid \n"
                                              "the mini oceanid follows all your commands.")
                                        print("it seems like you got what you wanted in this area")
                                        exploration.append("w")
                                    elif oceanidDialoque2 == "2":
                                        print("as expected. well you shall learn your lesson and place. I do hope you're strong enough to endure this punishment :)")
                                        othercodes.continuedialogue()
                                        print("suddenly, you are high up above the clouds. You looked down and it seems like you were thrown so far up in the sky")
                                        othercodes.continuedialogue()
                                        print("you see the whole forest above you. There are things that caught your eye. A lake, a big tree, and a cliff")
                                        othercodes.continuedialogue()
                                        print("you realize that you're not getting any higher and you start to drop, fast.\n"
                                              "as you were about to hit the ground...")
                                        othercodes.continuedialogue()
                                        print("you have fallen down to where you started... still intact and healthy somehow...")
                                        othercodes.continuedialogue()
                                    else:
                                        print("wrong input, game over.")
                                        othercodes.continuedialogue()

                                elif oceanidDialogue1 == "2":
                                    print(oceanid + "You're a cheeky one aren't ya? Well, let's see if you can still hear my answer when you're way up in the heavens.")
                                    othercodes.continuedialogue()
                                    print("suddenly, you are high up above with the clouds. You looked down and it seems like you were thrown so far up in the sky so quickly")
                                    othercodes.continuedialogue()
                                    print("you see the whole forest above you, the things that caught your eyes were a big tree, the oceanid area, a lake, and a cliff.")
                                    othercodes.continuedialogue()
                                    print("you realize that you're not getting any higher and you start to drop, fast.\n"
                                          "as you were about to hit the ground...")
                                    othercodes.continuedialogue()
                                    print("you have fallen down to where you started... safe and healthy somehow...")
                                    othercodes.continuedialogue()
                                else:
                                    print("wrong input, game over")
                                    break
                            else:
                                print("wrong input, game over")
                                break
                        elif yourchoice == "2":
                            print("You sing along with the oceanid. \n"
                                  "The oceanid merrily accepts your offer to duet. \n"
                                  "you two share a nice moment together, dancing along with the music you two are making")
                            othercodes.continuedialogue()
                            print("it seems like the oceanid gave you a glowing stone.")
                            othercodes.continuedialogue()
                            print("obtained \n"
                                  "pharsa's glowing stone necklace: press the button and it turns into a necklace and summons a mini oceanid \n"
                                  "the mini oceanid follows all your commands.")
                            print("it seems like you got what you wanted in this area")
                            exploration.append("w")

                        elif yourchoice == "3":
                            speakchoice = input("(1) Eekum Bokum (Try to speak the language of the oceanids) \n"
                                                "(2) Um, hello (Try to speak casually) \n")
                            if speakchoice == "1":
                                print("you remembered you read a book about the language of the oceanids, hope this works \n"
                                      "the oceanid seem to have been startled and started approaching you"
                                      +oceanid+": Lorem ipsum?")
                                speakchoice2 = input("(1) koa koa ku"
                                                     "(2) I'll come clean, I don't speak oceanid")
                                if speakchoice2 == "1":
                                    print("the oceanid seems to not have liked what you said")
                                    othercodes.continuedialogue()
                                    print(oceanid+": fu ro dah.")
                                    othercodes.continuedialogue()
                                    print("the oceanid encloses you in a body of water, making you drown")
                                    othercodes.continuedialogue()
                                    print("you don't know what you said, but it made the oceanid very... upset")
                                    othercodes.continuedialogue()
                                    print("perhaps you shouldn't have trusted that book after all")
                                    othercodes.continuedialogue()
                                    print("death by drowning, game over")
                                    othercodes.continuedialogue()
                                    break
                                elif speakchoice2 == "2":
                                    print(oceanid+"oh, is that so. how did you come to know the language of the oceanids?")
                                    othercodes.continuedialogue()
                                    print("you explain that you read it in a book")
                                    othercodes.continuedialogue()
                                    print(oceanid+": consider yourself lucky. Creatures who know of this language are those of which don't belong to the mortal realm \n"
                                          +oceanid+": in any case, on with it. \n"
                                          +oceanid+": why did you come to see a magnificent being such as me?")
                                    speakchoice3 = input("(1) I've come to explore this forest and it's wonders \n")
                                    if speakchoice3 == "1":
                                        print(oceanid +": so it would seem. My waters also tell me you're not lying. \n"
                                              +oceanid+": rejoice for I have spared your life \n"
                                              +oceanid+": off with you then. don't come to me again \n"
                                              +oceanid+": oceanids are only to be bothered in dire times \n"
                                              +oceanid+": interrupt me again and you'll meet your journey's end. \n"
                                              "youhave made it out alive somehow...")
                                        othercodes.continuedialogue()
                                        print("the oceanid gave you a glowing stone.")
                                        othercodes.continuedialogue()
                                        print("obtained \n"
                                              "pharsa's glowing stone necklace: press the button and it turns into a necklace and summons a mini oceanid \n"
                                              "the mini oceanid follows all your commands.")
                                        print("it seems like you got what you wanted in this area")
                                        exploration.append("w")
                                    else:
                                        print("wrong input, game over")
                                        othercodes.continuedialogue()
                                        break
                                else:
                                    print("wrong input, game over")
                                    othercodes.continuedialogue()
                                    break
                            elif speakchoice == "2":
                                print("You muster up your confidence and strike up a normal conversation \n"
                                      "the oceanid ignored you and continues to sing her song")
                                patiencechoice = input("(1) wait for her to finish \n"
                                                       "(2) interrupt her singing by shouting like a banshee \n")
                                if patiencechoice == "1":
                                    print("you waited patiently until it finshed it's song. the whole song soothed you so much that it felt like you didn't wait. \n"
                                          +oceanid+": for patiently waiting for me to finish my song, I'll entertain you just this once. \n"
                                          "adventurer, why have you come here?")
                                    patiencechoice2 = input("(1) I've come to see what's inside this forest \n")
                                    if patiencechoice2 == "1":
                                        print(oceanid+": I see, well off you go then. Oceanids should only be bothered in dire times. \n"
                                              +oceanid+"the only thing here is this magnificent oceanid that's in front of you, other than that this place is but a body of water. \n")
                                        othercodes.continuedialogue()
                                        print("it seems like the oceanid gave you a glowing stone.")
                                        othercodes.continuedialogue()
                                        print("obtained \n"
                                              "pharsa's glowing stone necklace: press the button and it turns into a necklace and summons a mini oceanid \n"
                                              "the mini oceanid follows all your commands.")
                                        print("it seems like you got what you wanted in this area")
                                        exploration.append("w")
                                    else:
                                        print("wrong input, game over")
                                        break
                                elif patiencechoice == "2":
                                    print("you interrupted her singing, it's upset with what you did. \n"
                                          +oceanid+": you seem to not know that oceanids not be interrupted while they're singing... \n"
                                          +oceanid+": may this serve as a lesson for you in the after life\n"
                                          "before you knew it, you got enclosed inside a ball of water and you drowned. \n"
                                          "you really pissed her off.")
                                    othercodes.continuedialogue()
                                    print("game over")
                                    othercodes.continuedialogue()
                                    break
                                else:
                                    print("wrong input, game over")
                                    othercodes.continuedialogue()
                                    break
                            else:
                                print("Wrong input, game over")
                                othercodes.continuedialogue()
                                break
                        else:
                            print("wrong input")
                            othercodes.continuedialogue()
                    elif oceanidchoice == "2":
                        print("You decide to approach the oceanid later and see the other locations first")
                    else:
                        print("Wrong input.")
                        othercodes.continuedialogue()
                else:
                    print("You have already explored this area")
                    othercodes.continuedialogue()

            elif forestinput == "2":
                if "t" not in exploration:
                    print("big tree")
                    print("You come across a huge tree with a stone tablet that has three strangely shaped stone holes...")
                    othercodes.continuedialogue()
                    fairyChoice = input("(1) Approach the big tree \n"
                                            "(2) Head back later \n")
                    if (fairyChoice == "1") and ("w" and "l" and "c" in exploration):
                        print("you approach the big tree, and suddenly all the stones you got from the other areas\n"
                              "started to glow ever stronger. They started floating towards the stone tablet and \n"
                              "placed themselve inside the three strangely shaped holes \n")
                        othercodes.continuedialogue()
                        print("A sword appeared in front of the tree, but was sealed with chains \n")
                        othercodes.continuedialogue()
                        print("?: you've made it this far, this is the last and final challenge")
                        othercodes.continuedialogue()
                        print("?: answer this riddle, and you'll get the sword that can wound any living being...")
                        othercodes.continuedialogue()
                        print("?: Dvalin's greatsword")
                        othercodes.continuedialogue()
                        print("?: 'I crawl with 4 legs by morning, walk with 2 legs in the afternoon, move with 3 by night. What am I?'")
                        puzzleInput = input("write your answer. \n").lower().strip()
                        if puzzleInput == "human":
                            print("your answer, dear adventurer...")
                            othercodes.continuedialogue()
                            print("is correct!")
                            othercodes.continuedialogue()
                            print("rejoice for you have obtained one of the greatest weapons on this realm")
                            print("obtained Dvalin's greatsword")
                            othercodes.continuedialogue()
                            print("the big tree gives a bright glow, and before you knew it, you were back to where you started")
                            print("the good thing is, you still have all the stones and the sword on your being")
                            exploration.append("t")
                            othercodes.continuedialogue()
                        elif puzzleInput == "humans":
                            print("your answer, dear adventurer...")
                            othercodes.continuedialogue()
                            print("is correct!")
                            othercodes.continuedialogue()
                            print("rejoice for you have obtained one of the greatest weapons on this realm")
                            print("obtained Dvalin's greatsword")
                            othercodes.continuedialogue()
                            print("the big tree gives a bright glow, and before you knew it, you were back to where you started")
                            print("the good thing is, you still have all the stones and the sword on your being")
                            exploration.append("t")
                            othercodes.continuedialogue()
                        elif puzzleInput == "human race":
                            print("your answer, dear adventurer...")
                            othercodes.continuedialogue()
                            print("is correct!")
                            othercodes.continuedialogue()
                            print("rejoice for you have obtained one of the greatest weapons on this realm")
                            print("obtained Dvalin's greatsword")
                            othercodes.continuedialogue()
                            print("the big tree gives a bright glow, and before you knew it, you were back to where you started")
                            print("the good thing is, you still have all the stones and the sword on your being")
                            exploration.append("t")
                            othercodes.continuedialogue()
                        elif puzzleInput == "human being":
                            print("your answer, dear adventurer...")
                            othercodes.continuedialogue()
                            print("is correct!")
                            othercodes.continuedialogue()
                            print("rejoice for you have obtained one of the greatest weapons on this realm")
                            print("obtained Dvalin's greatsword")
                            othercodes.continuedialogue()
                            print("the big tree gives a bright glow, and before you knew it, you were back to where you started")
                            print("the good thing is, you still have all the stones and the sword on your being")
                            exploration.append("t")
                            othercodes.continuedialogue()
                        elif puzzleInput == "human beings":
                            print("your answer, dear adventurer...")
                            othercodes.continuedialogue()
                            print("is correct!")
                            othercodes.continuedialogue()
                            print("rejoice for you have obtained one of the greatest weapons on this realm")
                            print("obtained Dvalin's greatsword")
                            othercodes.continuedialogue()
                            print("the big tree gives a bright glow, and before you knew it, you were back to where you started")
                            print("the good thing is, you still have all the stones and the sword on your being")
                            exploration.append("t")
                            othercodes.continuedialogue()
                        elif puzzleInput == "person":
                            print("your answer, dear adventurer...")
                            othercodes.continuedialogue()
                            print("is correct!")
                            othercodes.continuedialogue()
                            print("rejoice for you have obtained one of the greatest weapons on this realm")
                            print("obtained Dvalin's greatsword")
                            othercodes.continuedialogue()
                            print("the big tree gives a bright glow, and before you knew it, you were back to where you started")
                            print("the good thing is, you still have all the stones and the sword on your being")
                            exploration.append("t")
                            othercodes.continuedialogue()
                        elif puzzleInput == "people":
                            print("your answer, dear adventurer...")
                            othercodes.continuedialogue()
                            print("is correct!")
                            othercodes.continuedialogue()
                            print("rejoice for you have obtained one of the greatest weapons on this realm")
                            print("obtained Dvalin's greatsword")
                            othercodes.continuedialogue()
                            print("the big tree gives a bright glow, and before you knew it, you were back to where you started")
                            print("the good thing is, you still have all the stones and the sword on your being")
                            exploration.append("t")
                            othercodes.continuedialogue()
                        else:
                            if puzzleattempts == 0:
                                print("?: your answer, adventurer, is not correct. I'll give you 2 more chances. come back here once you've \n"
                                      "?: pondered upon the right answer which I seek")
                                puzzleattempts += 1
                                othercodes.continuedialogue()

                            elif puzzleattempts == 1:
                                print("?: your answer, adventurer, is not correct. I'll give you 1 more chance. come back here once you've \n"
                                      "?: pondered upon the right answer which I seek")
                                puzzleattempts += 1
                                othercodes.continuedialogue()

                            elif puzzleattempts == 2:
                                print("?: your answer, adventurer, is not correct. You've used up all your chances, and thus I would have to \n"
                                      "?: wipe your existence here and now")
                                othercodes.continuedialogue()
                                print("the big tree started to shine so bright it burned you to a crisp 'til nothing's left of you.")
                                othercodes.continuedialogue()
                                print("death by burning, game over.")
                                othercodes.continuedialogue()
                                break
                            else:
                                print("")

                    elif fairyChoice == "1":
                        print("you haven't found all the stones yet")
                        print("(explore the other areas first to get the stones)")
                    elif fairyChoice == "2":
                        print("You decide to approach the big tree later and see the other locations first")
                    else:
                        print("Wrong input. game over.")
                        othercodes.continuedialogue()
                        break
                else:
                    print("You have already explored this area")
                    othercodes.continuedialogue()

            elif forestinput == "3":
                if "l" not in exploration:
                    print("lake")
                    print("As you approach the lake, you see a chest that's blocked by a strong aura. \n"
                          "you see three platforms at the center of the lake \n"
                          "suddenly, a pathway have risen up from the lake bed that points towards \n"
                          "the three platforms in the middle of the lake.")
                    othercodes.continuedialogue()
                    platformchoice = input("(1) Move towards the platforms \n"
                                           "(2) Head back later \n")
                    if platformchoice == "1":
                        print("'I don't know why a pathway appeared, but something good might happen if I\n"
                              "go on the right one...' ")
                        othercodes.continuedialogue()
                        print("you start walking towards the platforms and see a floating scroll")
                        othercodes.continuedialogue()
                        print("scroll: step where the clock strikes twelve")
                        othercodes.continuedialogue()
                        print("'this might be the clue for the right platform'")
                        platformchoice2 = input("(1) step on the left\n"
                                                "(2) step on the middle\n"
                                                "(3) step on the right\n")
                        if platformchoice2 == "1":
                            print("you stepped on the left platform")
                            othercodes.continuedialogue()
                            print("nothing happens for awhile, but you see a sword fall down from above")
                            othercodes.continuedialogue()
                            print("'that's weird' you said to yourself. After you uttered that word \n"
                                  "it started raining swords on the whole lake. \n")
                            othercodes.continuedialogue()
                            print("death by multiple lacerations, game over")
                            othercodes.continuedialogue()
                            break
                        elif platformchoice2 == "2":
                            print("you stepped on the middle platform")
                            othercodes.continuedialogue()
                            print("you see the aura over the chest slowly fade away \n"
                                  "it seems that you stepped over the right platform")
                            othercodes.continuedialogue()
                            print("just then the scroll rolled itself up and disappeared \n"
                                  "you start to go to the chest and open it")
                            othercodes.continuedialogue()
                            print("you see the chest full of gold and silver, but you didn't bring your bag \n"
                                  "so you can just take so many.")
                            othercodes.continuedialogue()
                            print("after a few seconds, a glowing stone seem to have floated out of the chest \n"
                                  "you grab and examine it. \n")
                            othercodes.continuedialogue()
                            print("obtained \n"
                                  "wander forest's stone shield: press the button and it will turn into a shield that can \n"
                                  "block any projectiles.")
                            othercodes.continuedialogue()
                            print("you kept it in your pocket, since it will help you with your adventures, especially \n"
                                  "with enemies that are long range.")
                            othercodes.continuedialogue()
                            print("it seems like you got what you wanted in this area")
                            exploration.append("l")
                            platformchoice3 = input("(1) exit \n")
                            if platformchoice3 == "1":
                                print("")
                            else:
                                print("wrong input, game over")
                                othercodes.continuedialogue()
                                break
                        elif platformchoice2 == "3":
                            print("you step on the right platform")
                            othercodes.continuedialogue()
                            print("the ground eats you up and the next thing you notice is you're underground, stuck and \n"
                                  "imprisoned for all eternity \n")
                            othercodes.continuedialogue()
                            print("imprisoned for life, game over")
                            othercodes.continuedialogue()
                            break
                    elif platformchoice == "2":
                        print("You decide to not go there yet and see the other locations instead")
                    else:
                        print("Wrong input. game over")
                        othercodes.continuedialogue()
                        break
                else:
                    print("You have already explored this area")
                    othercodes.continuedialogue()

            elif forestinput == "4":
                if "c" not in exploration:
                    print("cliff")
                    print("you went as high as you can and found yourself on top of a cliff")
                    othercodes.continuedialogue()
                    cliffchoice = input("(1) View the cliff \n"
                                        "(2) Head back later \n")
                    if cliffchoice == "1":
                        print("you see the forest in its entirety and it is breathtaking to look at.")
                        othercodes.continuedialogue()
                        print("you see three things that catch your eye.")
                        othercodes.continuedialogue()
                        print("a big tree, a lake with chest surrounded by aura, and a waterfall with a flying creature that's made up of water")
                        othercodes.continuedialogue()
                        print("'I'll definitely come here again just for this view'")
                        othercodes.continuedialogue()
                        print("after a while, a glowing stone came flying by in front of you")
                        print("you grab it...")
                        othercodes.continuedialogue()
                        print("obtained")
                        print("cliffside glowing stone cloak: press the button and the stone turns into a cloak that lets you \n"
                              "fly high into the sky, or make you turn invisible")
                        othercodes.continuedialogue()
                        print("after viewing the area and obtaining a very handy stone, you decide to go to the other areas.")
                        exploration.append("c")
                    elif cliffchoice == "2":
                        print("You decide to view the cliff later and see the other locations first")
                    else:
                        print("Wrong input.")
                        othercodes.continuedialogue()
                else:
                    print("You have already explored this area")
                    othercodes.continuedialogue()
            else:
                print("Wrong Input, choose again.")
                othercodes.continuedialogue()
