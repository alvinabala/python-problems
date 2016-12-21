#!/usr/bin/python
import random

def twist():
    fin = open("planets.txt")
    planets =   [line.strip() for line in fin]
    fin.close()

    choice = random.randint(0,len(planets))
    chosen = [i for i in planets[choice]]

    jumbled = [];

    chosen_len = len(chosen)
    chosen_len = chosen_len-1

    while chosen_len >= 0:
        jumbled.append(chosen.pop(random.randint(0, chosen_len)))
        chosen_len = chosen_len - 1

    chosen = planets[choice]

    tries = 3

    while tries > 0:
        print "You have", tries, "tries left"
        print "The jumbled word is:"
        print str(jumbled)
        attempt = raw_input("Enter your attempt:")

        if attempt == chosen:
            print "CORRECT!"
            break;
        else:
            print "wrong..."
            tries = tries - 1

    print "Game Over."
