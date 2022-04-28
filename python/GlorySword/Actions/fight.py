#!/usr/bin/python3
""" fighting plateform"""
import random


def fight(player1):
    """ fight func:
        args:
            player1: Take player 1 from class Player as parameter
            (to get infos on hp, manaa, defense and attack)
    """
    hp1 = 100
    manaa1 = 0
    hp2 = 100
    manaa2 = 0
    ActionHistory = []

    while hp1 != 0 or hp2 != 0:
        print("hp1 =", hp1, "hp2 =", hp2, "\nmanaa1 =", manaa1, "manaa2 =", manaa2)
        if manaa1 >= 30:
            action = input("Heal\nAttack\nPass\nSuperAttack\n")
            if manaa1 >= 30 and action == "SuperAttack":
                hp2 -= 30
                manaa1 -= 30
            elif action == "Attack":
                hp2 -= 10
            elif action == "Heal" and manaa1 >= 5:
                if hp1 == 100:
                    pass
                elif hp1 == 90:
                    hp1 += 10
                else:
                    hp1 += 20
                manaa1 -= 5
            elif action == "Pass":
                pass
            print(action)
            print("hp1 =", hp1, "hp2 =", hp2, "\n", "manaa1 =", manaa1, "manaa2 =", manaa2)
        else:
            action = input("Heal\nAttack\nPass\n")
            if action == "Attack":
                hp2 -= 10
            elif action == "Heal" and manaa1 >= 5:
                if hp1 == 100:
                    pass
                elif hp1 == 90:
                    hp1 += 10
                else:
                    hp1 += 20
                manaa1 -= 5
            elif action == "P":
                pass
            print(action)
            print("hp1 =", hp1, "hp2 =", hp2, "\n", "manaa1 =", manaa1, "manaa2 =", manaa2)

        if manaa2 >= 30:
            action2 = ["Attack2", "Heal2", "Pass2", "SuperAttack2"]
            act2 = random.choice(action2)
            if act2 == "Attack2":
                hp1 -= 10
            elif manaa2 == 30 and act2 == "SuperAttack2":
                hp1 -= 30
                manaa2 -= 30
            elif act2 == "Pass2":
                pass
            elif act2 == "Heal2" and manaa2 >= 5:
                if hp2 == 100:
                    pass
                elif hp2 == 90:
                    hp2 += 10
                else:
                    hp2 += 20
                manaa2 -= 5
        else:
            action2 = ["Attack2", "Heal2", "Pass2"]
            act2 = random.choice(action2)
            if act2 == "Attack2":
                hp1 -= 10
            elif act2 == "Pass2":
                pass
            elif act2 == "Heal2" and manaa2 >= 5:
                if hp2 == 100:
                    pass
                elif hp2 == 90:
                    hp2 += 10
                else:
                    hp2 += 20
                manaa2 -= 5
        if hp1 <= 0:
            print("Player 2 won !")
            return
        elif hp2 <= 0:
            print("Player 1 won !")
            return
        if manaa1 <= 50:
            manaa1 += 10
        if manaa2 <= 50:
            manaa2 += 10
        print(act2)
        print("---------------------------")

if __name__ == "__main__":
    player1 = 1
    player2 = 2
    fight(player1)
