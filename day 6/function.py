import sys
import random

def check_arrangement(braces):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for char in braces:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return len(stack) == 0

def tell_a_fun_fact():
    facts = [
        "Honey never spoils. Archaeologists have found edible honey in ancient Egyptian tombs.",
        "Bananas are berries, but strawberries are not.",
        "A group of flamingos is called a 'flamboyance'.",
        "Octopuses have three hearts.",
        "There are more possible iterations of a game of chess than atoms in the observable universe.",
        "Wombat poop is cube-shaped.",
        "The Eiffel Tower can be 15 cm taller during hot days.",
        "A snail can sleep for three years.",
        "The unicorn is the national animal of Scotland.",
        "There are more stars in the universe than grains of sand on Earth.",
        "Some turtles can breathe through their butts.",
        "The inventor of the frisbee was turned into a frisbee after he died.",
        "A group of crows is called a murder.",
        "Hot water freezes faster than cold water under certain conditions (the Mpemba effect).",
        "Venus is the only planet that spins clockwise.",
        "The shortest war in history lasted 38 minutes.",
        "Sloths can hold their breath longer than dolphins can.",
        "The dot over the letter 'i' is called a tittle.",
        "Mosquitoes are attracted to people who just ate bananas.",
        "A jiffy is an actual unit of time: 1/100th of a second."
    ]
    print("Fun Fact:", random.choice(facts))

if __name__ == "__main__":
    tell_a_fun_fact()
    if len(sys.argv) < 2:
        print("Usage: python function.py '<braces_string>'")
        sys.exit(1)
    input_str = sys.argv[1]
    print(f'user given input: {input_str}')
    if check_arrangement(input_str):
        print("Arrangement of braces is properly done.")
    else:
        print("Arrangement of braces is NOT properly done.")

