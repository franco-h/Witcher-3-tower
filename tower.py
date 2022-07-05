#!/usr/bin/python3

import sys
import os
import helper as h
import events as e
import combat as c

"Witcher 3: Wild Hunt - A Towerful of Mice"


def showInstructions():
    # print a main menu and the commands
    h.fprint('''
Witcher 3: Wild Hunt - A Towerful of Mice
===============================
Background: To defend Kaer Morhen from the Wild Hunt, you need to enlist the help of Keira Metz. However, Keira only agrees to do so if you can lift the curse on the Fyke Island Tower. You hopped into Keira's boat and sailed to Fyke Island. After you cleared out the Drowners, Ghouls, and Rotfriends in the nearby area, you entered the tower at the ground floor and sensed a presence of a powerful evil force..........
-------------------------------
Commands:
    GO [up, down]
    GET [item, spell]
    USE [item, spell]
    LOOK
    INV/INVENTORY
Type 'help' at any time! Type 'q' to quit!''')


def playerinfo():
    #    print('')
    #    print('YOU ARE IN THE ' + currentRoom + '.')
    print('=================================')
    print('Inventory :', str(c.inventory))
    print('Spells :', str(c.signbook))
    print('=================================')


def showStatus():  # display the player's status
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print the current inventory
    print('Inventory : ' + str(c.inventory))
    if 'item' in rooms[currentRoom]:
        # print all items in the room

        print('You see a ' + rooms[currentRoom]['item'] + "." +
              rooms[currentRoom]['item_status'] + '.')


rooms = {
    'FIRST FLOOR': {
        'access': True,
        'up': 'SECOND FLOOR',
        'item': 'magic lamp',
        'item_status': ' Keira Metz has teleported the magic lamp to the first floor. You can use it to communicate with the ghosts.'
    },
    'SECOND FLOOR': {
        'access': True,
        'item': 'specter oil',
        'item_status': 'You see a bottle of specter oil on a desk. You sense that it is a powerful potion that can be used to fight a pesta.',
        'desc': 'Looks like this is the top floor of the tower. Yet, you see a pull level which makes you thinking if the current room is a false top.',
        'down': 'FIRST FLOOR',
        'up': 'SECRET ROOM'
    },
    'SECRET ROOM': {
        'down': 'SECOND FLOOR',
        'access': False,
        'event': True
    }
}

currentRoom = 'FIRST FLOOR'

showInstructions()

while True:
    playerinfo()
    showStatus()
    # ask the player what they want to do
    move = ''
    while move == '':
        move = input('>')  # so long as the move does not
        # have a value. Ask the user for input

    # make everything lower case because directions and items require it, then split into a list
    move = move.lower().split()
    os.system('clear')  # clear the screen
    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
            if 'desc' in rooms[currentRoom]:
                print(rooms[currentRoom]['desc'])

                # if 'access' is false, the player can't go that way.
            if 'access' in rooms[currentRoom]:
                if rooms[currentRoom]['access'] == False:
                    print('You can\'t go that way!')
                    currentRoom = rooms[currentRoom]['down']

            if 'event' in rooms[currentRoom]:
                e.key_event()

        else:
            print("YOU CAN'T GO THAT WAY!")
    else:
        print("YOU CAN'T GO THAT WAY!")

    if move[0] == 'use':
        if (move[1] + ' ' + move[2]).lower() == 'specter oil' and 'specter oil' in c.inventory:
            print("You applied the specter oil to your silver sword. It would cause a lot of damage to any specter")
            # add 10 to the armory's silver sword damage
            c.armory['silver sword']['damage'] += 10

        if (move[1] + ' ' + move[2]).lower() == 'magic lamp' and 'magic lamp' in c.inventory:
            # Change all rooms[currentRoom]['event'] to True

            print(
                "You are using the magic lamp now. It would allow you to see and communicate with the ghosts.")
            # Ask if the player wants to investigate the communication between the ghosts
            print("Do you want to investigate the communication between the ghosts?")
            decision = input("(y/n)")
            if decision == 'y':
                # if the current room is first floor, call story_event_one()
                if currentRoom == 'FIRST FLOOR':
                    e.story_event_one()
                # if the current room is second floor, call story_event_two()
                elif currentRoom == 'SECOND FLOOR':
                    e.story_event_two()
            else:
                continue

        if (move[1] + ' ' + move[2]).lower() == 'pull level':
            # Check if the current room is the second floor
            if currentRoom == 'SECOND FLOOR':
                # Change the acess of secret room to True
                rooms['SECRET ROOM']['access'] = True
                print(
                    "You pulled the pull level. You can now see the entrance of the secret room.")

    if move[0] == 'get':
        # if there is an item in the room, and the the combination of move[1] and move[2] is in the room
        if 'item' in rooms[currentRoom] and (move[1] + ' ' + move[2]) in rooms[currentRoom]['item']:
            # if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add item to inv
            c.inventory.append(move[1]+' '+move[2])
            # msg saying you received the item
            print((move[1] + ' ' + move[2]).capitalize() + ' received!')
            # deletes that item from the dictionary
            del rooms[currentRoom]['item']
        else:
            print('YOU CANNOT GET ' + (move[1].upper()) + '!')

    if move[0] == 'look':
        # If 'event' is true in the current room, run the event
        if 'desc' in rooms[currentRoom]:
            print(rooms[currentRoom]['desc'])  # print the look description
        else:
            print('You can\'t see anything.')

    elif move[0] == 'help':
        showInstructions()

    elif move[0] in ['q', 'quit]']:
        print("Are you sure you want to quit? Yes/No")
        quit_query = input('>')
        if quit_query.lower() in ['y', 'yes']:
            print("Thanks for playing!")
            sys.exit()
        else:
            pass
