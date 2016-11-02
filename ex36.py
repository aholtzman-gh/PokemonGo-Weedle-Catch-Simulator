import random
import os
from sys import exit

# Clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Starting message (to display once)
clear_screen()
print "Welcome to the Pokemon Go Weedle catching simulator."
print "Prepare for fun times!"
raw_input("OK")

# Set some basic starting numbers
pokeball_count = 5
starting_pokeball_count = pokeball_count
weedles_captured = 0
catch_probability = 0.75
escape_probability = 0.25

# Exit the program
def quit(pokeball_count, weedles_captured):
    clear_screen()
    print "You caught %d Weedle and have %d pokeballs left." % (weedles_captured, pokeball_count)
    print "Your catch rate was %r%%\n" % (round(float(weedles_captured) / (float(starting_pokeball_count) - float(pokeball_count)),2) * 100)
    exit(0)

# catch determination, throw in some rng
def catch(pokeball_count, weedles_captured):
    if random.random() <= catch_probability:
        clear_screen()
        print "You hit the Weedle with your pokeball!"
        raw_input("OK")

        if random.random() <= escape_probability:
            clear_screen()
            print "The weedle escaped and ran away!"
            raw_input("OK")
            new_pokeball_count = pokeball_count - 1
            new_weedles_captured = weedles_captured
        else:
            clear_screen()
            print "You caught it!"
            raw_input("OK")
            new_pokeball_count = pokeball_count - 1
            new_weedles_captured = weedles_captured + 1
    else:
        clear_screen()
        print "You missed! Try again?"
        retry_catch = raw_input("> ")

        if "Y" in retry_catch.upper():
            new_pokeball_count, new_weedles_captured = catch(pokeball_count - 1, weedles_captured)
        elif "N" in retry_catch.upper():
            new_pokeball_count = pokeball_count - 1
            new_weedles_captured = weedles_captured
        else:
            clear_screen()
            print "Expected yes or no, assuming you meant no."
            new_pokeball_count = pokeball_count - 1
            new_weedles_captured = weedles_captured

    return new_pokeball_count, new_weedles_captured

# Encountering a Weedle
def encounter(pokeball_count, weedles_captured):
    clear_screen()
    print "A wild Weedle appears! You have %d pokeballs and have caught %d Weedle." % (pokeball_count, weedles_captured)
    print "Will you attempt to catch it, look for a different Weedle, or quit?"

    while True:
        decision = raw_input("> ")

        if "CATCH" in decision.upper():
            pokeball_count, weedles_captured = catch(pokeball_count, weedles_captured)
            break
        elif "LOOK" in decision.upper():
            clear_screen()
            print "You decide this Weedle just isn't for you and move on."
            raw_input("OK")
            break
        elif "QUIT" in decision.upper():
            quit(pokeball_count, weedles_captured)
        else:
            clear_screen()
            print "That is not an option"

    return pokeball_count, weedles_captured

# Either the player finds nothing or they encounter a Weedle
def walk_or_encounter(pokeball_count, weedles_captured):
    if random.random() <= 0.5:
        clear_screen()
        print "You walk and find nothing."
        raw_input("OK")
    else:
        pokeball_count, weedles_captured = encounter(pokeball_count, weedles_captured)

    return pokeball_count, weedles_captured

# Keep playing forever until player runs out of pokeballs.
while True:
    if pokeball_count > 0:
        pokeball_count, weedles_captured = walk_or_encounter(pokeball_count, weedles_captured)
    else:
        quit(pokeball_count, weedles_captured)
