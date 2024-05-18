import random


def generate_title():
    with open('titles.txt') as f:
        lines = f.readlines()
        
    return random.choice(lines).strip()