#!/usr/bin/python3
import sys
from random import randint
import events as e

plague_maiden = {'name': 'Plague Maiden', 'human': False,
                 'type': 'spectre', 'health': 500, 'damage': 30}

armory = {'steel sword': {'damage': 20},
          'silver sword': {'damage': 20}}

offense_signs = {'aard': {'damage': 30},
                 'igni': {'damage': 50},
                 'yrden': {'damage': 0}}

defense_signs = {'quen': {'shield': 100}}

player_health = 100
player_shield = 0
inventory = ['steel sword', 'silver sword']
signbook = ['aard', 'igni', 'yrden', 'quen']


def combat():

    global player_health, inventory, armory, plague_maiden, player_shield, signbook
    round = 1
    monster_health = plague_maiden['health']

    print(
        f"Because you refused to help Annabelle to find Graham. Her anger had turned her into {plague_maiden['name']}. You have no choice but to defeat her! COMBAT HAS BEGUN!\n")
    while True:
        print(f"ROUND {round}")
        print("Player Health: [" + str(player_health) + "]")
        print("Player Sheild: [" + str(player_shield) + "]")
        print("Monster Health: [" + str(monster_health) + "]")
        # print all inventory and signbook
        print("Inventory: " + str(inventory))
        print("Signbook: " + str(signbook))

        # gotta write code for cast
        print("Type: DODGE, CAST [spell], or USE [weapon]")
        # converts move into a lower-case list to deal with each item in list separately
        move = input().lower().split()
        monster_damage = plague_maiden['damage']
        print("\n=========================")

        if move[0] == 'use':
            # If "steel sword" is in the inventory, then the player can use it
            # If moive[1] is steel sword
            # checks if steel sword is in your inventory
            if (move[1] + ' ' + move[2]) == 'steel sword':
                # Check if plague_maiden is human. If it is true, then the damage of the steel sword is 100%. If it is false, the the damage of the steel sword is 0%
                if plague_maiden['human'] == False:
                    player_damage = 0
                    print(
                        f"Steel weapon only works on human enemies. You have to use silver sword. As the result, you hit a {plague_maiden['name']} for {player_damage} damage only!")

                else:
                    player_damage = armory[(
                        move[1] + ' ' + move[2])]['damage']
                    print(
                        f"You hit a {plague_maiden['name']} for {player_damage} damage!")
            # checks if silver sword is in your inventory
            if (move[1] + ' ' + move[2]) == 'silver sword':
                # Check if plague_maiden is human. If it is true, then the damage of the steel sword is 0%. If it is false, the the damage of the steel sword is 100%
                if plague_maiden['human'] == True:
                    player_damage = 0
                    print(
                        f"Silver weapon only works on non-human enemies. You have to use steel sword. As the result, you hit a {plague_maiden['name']} for {player_damage} damage only!")
                else:
                    player_damage = armory[(
                        move[1] + ' ' + move[2])]['damage']
                    print(
                        f"You hit a {plague_maiden['name']} for {player_damage} damage!")

        # Sign abilities
        if move[0] == 'cast':
            # Aard
            if move[1].lower() == 'aard':
                player_damage = offense_signs[move[1]]['damage']
                print(
                    f"You launched a telekinetic thrust that stun the {plague_maiden['name']} for {player_damage} damage!")
            # Igni
            if move[1].lower() == 'igni':
                player_damage = offense_signs[move[1]]['damage']
                print(
                    f"You launched a pyrokinetic burst that ignite the {plague_maiden['name']} for {player_damage} damage!")
            # Yrden
            if move[1].lower() == 'yrden':
                # Check if plague_maiden is human. If it is false, then the damage of the plague_maiden is reduced to 20.
                if plague_maiden['human']:
                    print(f"This only slow down the {plague_maiden['name']}!")
                else:
                    # reduce the damage of the plague_maiden to 20
                    monster_damage = plague_maiden['damage'] - 20
                    print(
                        f"The {plague_maiden['name']} has been weakened to 20 damage!")
            # Quen
            if move[1].lower() == 'quen':
                # Increase the shield of the player
                player_shield = defense_signs[move[1]]['shield']
                print("You have increased your shield to 100!")

        if move[0] == 'dodge':

            dodge_chance = randint(1, 2)

            if dodge_chance == 2:
                # monster_damage = 0 for that round
                monster_damage = 0
                print("You successfully dodge an attack!")

            else:
                # If the player's shield is 0, then the player loses health
                if player_shield == 0:
                    player_health -= int(monster_damage)
                else:
                    # If the player's shield is not 0, then the player loses shield
                    player_shield -= int(monster_damage)
                    if player_shield < 0:
                        player_shield = 0
                print(
                    f"The {plague_maiden['name']} out-maneuvers you and attacks! You took full damager.")

        try:
            monster_health -= int(player_damage)
        except:
            pass
        if monster_health <= 0:
            e.event_one()

        print(
            f"A {plague_maiden['name']} hits you for {monster_damage} damage!")
        print("=========================\n")
        round += 1
        # if the player's shield is less than or equal to 0, then the player's health is reduced by the monster's damage
        if player_shield <= 0:
            player_health -= int(monster_damage)
        else:
            player_shield -= int(monster_damage)
            # player_shield cannot be less than 0
            if player_shield < 0:
                player_shield = 0

        if player_health <= 0:
            print("You have been vanquished! You are dead.")
            sys.exit()
