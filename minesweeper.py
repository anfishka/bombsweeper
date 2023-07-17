import random

SIZE_BATTLE_FIELD = 8
LETTERS = ['A','B','C','D','E','F','G','H']
NUMS = ['1','2','3','4','5','6','7','8']
EMPTY = ' '
SQUARE = '■'
BOMB = 'ø'
BATTLE_FIELD_USER = []
BATTLE_FIELD_REAL = []

def createBattleField():
    for row in range(SIZE_BATTLE_FIELD):
        tmp = []
        tmp_1 = []

        for col in range(SIZE_BATTLE_FIELD):
                tmp.append(EMPTY)
                tmp_1.append(EMPTY)
        BATTLE_FIELD_USER.append(tmp)
        BATTLE_FIELD_REAL.append(tmp)


def printBattleFieldU():
    print(" ", LETTERS)
    for i, row in enumerate(BATTLE_FIELD_REAL):
        print(NUMS[i], row, NUMS[i])
    print(" ", LETTERS)
        # print(f'\x1b[32m{i}\033[0m')
        # green


def printBattleFieldR():
    print(" ",LETTERS)
    for i, row in enumerate(BATTLE_FIELD_REAL):
        print(NUMS[i], row, NUMS[i])
    print(" ", LETTERS)



def bombsSet(AMOUNT):
    for i in range(AMOUNT):
        while True:
            pos_h = random.randint(1, SIZE_BATTLE_FIELD-1)
            pos_v = random.randint(1, SIZE_BATTLE_FIELD-1)
            if BATTLE_FIELD_REAL[pos_h][pos_v] == EMPTY:
                BATTLE_FIELD_REAL[pos_h][pos_v] = BOMB
                break

def goTo():
    while True:
        your_pos_h = input("Enter horizontal position (from A to H) \n-> ")
        your_pos_v = input("Enter vertical position (from 1 to 8) \n-> ")

        if your_pos_h not in LETTERS or your_pos_v not in NUMS:
            print("Invalid inputs! Try again!")
            continue

        pos_h = LETTERS.index(your_pos_h)
        pos_v = int(your_pos_v) - 1

        if BATTLE_FIELD_USER[pos_v][pos_h] == EMPTY and BATTLE_FIELD_REAL[pos_v][pos_h] == EMPTY:
            BATTLE_FIELD_USER[pos_v][pos_h] = SQUARE
            BATTLE_FIELD_REAL[pos_v][pos_h] = SQUARE
            break

        if BATTLE_FIELD_REAL[pos_v][pos_h] == BOMB:
            BATTLE_FIELD_USER[pos_v][pos_h] = BOMB
            print("Game Over! You hit a bomb.")
            printBattleFieldU()
            return

        if BATTLE_FIELD_USER[pos_v][pos_h] != EMPTY:
            print("Position already selected. Please try again.")
    printBattleFieldU()



def startGame():
    createBattleField()
    printBattleFieldU()
    bombsSet(8)
    # printBattleFieldR()
    goTo()

