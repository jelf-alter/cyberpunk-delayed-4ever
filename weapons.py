#!/usr/bin/env python3


# calculates weapon damage for rapid fire
def rapid_fire():
    print()
    print("Starting rapid fire sequence")
    ref = input("Enter character's reflex stat: ")
    weapon_skill = input("Enter character's weapon skill: ")
    aiming_modifiers = input("Enter any aiming modifiers: ")
    
    print("todo")

def three_round():
    print("todo")

def suppresive_fire():
    print("todo")

attack_type = input("Input attack type: rapid file [1], three_rount[2], suppresive fire[3]\n")

if attack_type == "1":
    rapid_fire()
elif attack_type == "2":
    three_round()
elif attack_type == "3":
    suppresive_fire()
else:
    print("invalid input")
