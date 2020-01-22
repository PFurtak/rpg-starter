import random


class Hero:
    health = 10
    power = 5

    def __init__(self, health, power):
        self.health = health
        self.power = power

    def attack(self, greens):
        # Hero attacks goblin
        critical = random.random() > .8
        russle.crit = russle.power * 2
        if critical:
            print('Critical!')
            greens.health -= russle.crit
            print("You do %d damage to the goblin." % russle.crit)
        else:
            greens.health -= russle.power
            print("You do %d damage to the goblin." % russle.power)
        if greens.health <= 0:
            print("The goblin is dead.")

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False


class Goblin:
    health = 6
    power = 2

    def __init__(self, health, power):
        self.health = health
        self.power = power

    def attack(self, russle):
        if greens.health > 0:
            russle.health -= greens.power
        print("The goblin does %d damage to you." % greens.power)
        if russle.health <= 0:
            print("You are dead.")

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False


russle = Hero(10, 5)
greens = Goblin(6, 2)


def main():

    while greens.alive() and russle.alive():
        print("You have %d health and %d power." %
              (russle.health, russle.power))
        print("The goblin has %d health and %d power." %
              (greens.health, greens.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            russle.attack(greens)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print('Good Bye.')
            break

        else:
            print("Invalid input %r" % user_input)


main()
