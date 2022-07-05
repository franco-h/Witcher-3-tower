#!/usr/bin/python3
import sys
import helper as h
import combat as c


def story_event_one():
    h.fprint('''
    Geralt uses the lamp and now he can watch the last moments of the peasants killed in the past and learns more about the events that transpired on the island during the massacre.
    ============================================================
    There are seven ghosts to be found with the lantern, three outside the tower and four inside the tower. One body is fairly fresh, having been killed recently by an unknown foe. Keira directs Geralt to find the mage's lab, which is at the top of the tower.
    ''')


def story_event_two():
    h.fprint('''
    Unlike the first floor where you can find a number of ghosts, you only see one ghost in this floor. However, as you approach the ghost, you see that it flys through the top ceiling. This makes you wonder if there is another room upstairs.
    ''')


def key_event():
    h.fprint('''
    Upon entering the secret room, you found the ghost of Annabelle. Unlike other ghosts that could not feel your presence, Annabelle was able to do so. You asked Annabelle what happened to her.
    ===========================================================
    She tells that how the mage, Alexander, had been experimenting with rats and infecting them with a disease called Catriona. One day, peasants came to the island and broke into the tower to kill everyone there. Terrified by this, she drank a potion that the mage had given her, thinking it'd kill her. Instead, it was a strong paralyzing potion that put her in a deathlike slumber to make the peasants think she had killed herself, so they left after killing everyone else. However, when she awoke, she was still paralyzed and the rats ate her alive.
    ===========================================================
    Geralt explains to her that the curse on the island is obviously centered around her and, as it was born from hate, only love can break it. He then suggests that to break the curse, she has to forgive her love, Graham, who left her alone on the isle, having believed she had died. She claims she is ready to forgive Graham, but only if Geralt brings her bones to Graham for him to bury.
    ===========================================================
    
    You, as Geralt, has to decide if you agree or refuse the request.
    ''')

    decision = input('Do you want to accept her request? (y/n)')
    # if the player accepts the request, then call event_two. If the player declines, then call event_one and enter combat.
    if decision == 'y':
        event_two()

    if decision == 'n':
        c.combat()


def event_one():
    h.fprint('''
    Keira Metz: What was that? It soundded for a monent like you'd join the wraiths yourself..
    Geralt: Had to fight a pesta.
    Keira Metz: A pesta? And did you learn how to lift the curse before you lunged at her, sword in hand?
    Geralt: Yeah, we talked a bit. Looks like I need to ger her beloved to the island. Fisherman named Graham.
    ===========================================================
    Keira advises Geralt to see Graham, who lives just north in Oreton, about lifting the curse. Geralt goes to Graham to inform him of the curse and about Anabelle becoming a pesta, explaining that if she forgives Graham the curse will be broken, but he needs to be there to prove his love to her.
    ===========================================================
    The two head back to the island where they are attacked by wraiths of the curse's victims, who blame Graham for their misery, before finally making it to the top of the tower where the pesta awaits. Graham explains to Anabelle that he didn't mean to leave her and that he still loves her so she asks him to prove it by kissing her. Graham kisses her and, as she returns to human form, he dies and is reunited with her in death, lifting the curse.
    ===========================================================
    ''')

    h.print_slow(
        '''Mission completed! You have successfully lifted the curse on the Fyke Island Tower! Mission completed''')
    # terminate the game
    sys.exit()


def event_two():
    h.fprint('''
    Once Geralt acquires the bones, he takes them to the fisherman, Graham. Graham admits his role in allowing the peasants access to the island that led to the massacre, but didn't know that his love was still alive when she drank the potion.
    ---------------------------------------------------------------
    Geralt gives her bones to Graham to bury and leaves. However, before he gets too far, Geralt hears a scream from Graham's cabin and rushes back in to find him dead, his body surrounded by rats with Anabelle floating over him in her true appearance as a plague maiden. Now that the bones are off the island, the curse is broken, but the pesta is now free to roam the world and spread the plague, almost ruining Kerack in the process.
    ''')

    h.print_slow(
        '''Mission Failed!''')
    # terminate the game
    sys.exit()
