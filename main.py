import random
import json

# ================
# DEFINE VARIABLES
# ================

track = False
bypass = False
times_three = []
times_two = []
times_four = []
times_five = []
times_pyra = []
times_skewb = []
times_megaminx = []

# ==============
# OPEN SAVE DATA
# ==============
try:
    with open('Json/3x3 Solves.json', 'r') as f:
        times_three = json.load(f)
except json.JSONDecodeError as e:
    print(f"Invalid JSON In File. {e}")
    bypass = True
except FileNotFoundError as e:
    print(e)
    bypass = True
try:
    with open('Json/2x2 Solves.json', 'r') as f:
        times_two = json.load(f)
except json.JSONDecodeError as e:
    print(f"Invalid JSON In File. {e}")
    bypass = True
except FileNotFoundError as e:
    print(e)
    bypass = True
try:
    with open('Json/4x4 Solves.json', 'r') as f:
        times_four = json.load(f)
except json.JSONDecodeError as e:
    print(f"Invalid JSON In File. {e}")
    bypass = True
except FileNotFoundError as e:
    print(e)
    bypass = True
try:
    with open('Json/5x5 Solves.json', 'r') as f:
        times_five = json.load(f)
except json.JSONDecodeError as e:
    print(f"Invalid JSON In File. {e}")
    bypass = True
except FileNotFoundError as e:
    print(e)
    bypass = True
try:
    with open('Json/Pyraminx Solves.json', 'r') as f:
        times_pyra = json.load(f)
except json.JSONDecodeError as e:
    print(f"Invalid JSON In File. {e}")
    bypass = True
except FileNotFoundError as e:
    print(e)
    bypass = True
try:
    with open('Json/Skewb Solves.json', 'r') as f:
        times_skewb = json.load(f)
except json.JSONDecodeError as e:
    print(f"Invalid JSON In File. {e}")
    bypass = True
except FileNotFoundError as e:
    print(e)
    bypass = True

# ================
# DEFINE FUNCTIONS
# ================

def save():
    with open('Json/3x3 Solves.json', 'w') as file:
        json.dump(times_three, file)
    with open('Json/2x2 Solves.json', 'w') as file:
        json.dump(times_two, file)
    with open('Json/4x4 Solves.json', 'w') as file:
        json.dump(times_four, file)
    with open('Json/5x5 Solves.json', 'w') as file:
        json.dump(times_five, file)
    with open('Json/Pyraminx Solves.json', 'w') as file:
        json.dump(times_pyra, file)
    with open('Json/Skewb Solves.json', 'w') as file:
        json.dump(times_skewb, file)


def error(code):
    if code == 1:
        print("Option Not Recognized. Please Try Again.")
    elif code == 2:
        print("You Must Import A Number Or 'DnF'.")


def three_by_three():
    print(times_three)
    moves = ["U", "D", "F", "B", "R", "L"]
    modifiers = ["", "'", "2"]
    last_move = ""
    second_last_move = ""
    repeatable = True
    repeated = 0
    scramble = ""

    while repeatable:
        invalid = False
        move = random.choice(moves)
        modifier = random.choice(modifiers)
        if move == last_move:
            invalid = True
        if move == "U":
            if second_last_move == "D":
                invalid = True
        if move == "D":
            if second_last_move == "U":
                invalid = True
        if move == "F":
            if second_last_move == "B":
                invalid = True
        if move == "B":
            if second_last_move == "F":
                invalid = True
        if move == "R":
            if second_last_move == "L":
                invalid = True
        if move == "L":
            if second_last_move == "R":
                invalid = True
        if not invalid:
            scramble = scramble + move + modifier + " "
            repeated += 1
            second_last_move = last_move
            last_move = move
        if repeated == 25:
            repeatable = False
            print(scramble)
            if not track:
                input()


def two_by_two():
    moves = ["U", "F", "R"]
    modifiers = ["", "'", "2"]
    last_move = ""
    repeatable = True
    repeated = 0
    scramble = ""

    while repeatable:
        invalid = False
        move = random.choice(moves)
        modifier = random.choice(modifiers)
        if move == last_move:
            invalid = True
        if not invalid:
            scramble = scramble + move + modifier + " "
            repeated += 1
            last_move = move
        if repeated == 12:
            repeatable = False
            print(scramble)
            if not track:
                input()


def four_by_four():
    moves = ["U", "D", "F", "B", "R", "L"]
    modifiers = ["", "'", "2"]
    last_move = ""
    second_last_move = ''
    repeatable = True
    repeated = 0
    scramble = ""

    while repeatable:
        invalid = False
        move = random.choice(moves)
        modifier = random.choice(modifiers)
        if move == last_move or move == second_last_move:
            invalid = True
        if move == "U":
            if second_last_move == "D":
                invalid = True
        if move == "D":
            if second_last_move == "U":
                invalid = True
        if move == "F":
            if second_last_move == "B":
                invalid = True
        if move == "B":
            if second_last_move == "F":
                invalid = True
        if move == "R":
            if second_last_move == "L":
                invalid = True
        if move == "L":
            if second_last_move == "R":
                invalid = True
        if not invalid:
            if random.randint(0, 2) == 1:
                scramble = scramble + move + "w" + modifier + " "
                repeated += 1
                second_last_move = last_move
                last_move = move
            else:
                scramble = scramble + move + modifier + " "
                repeated += 1
                second_last_move = last_move
                last_move = move
        if repeated == 40:
            repeatable = False
            print(scramble)
            if not track:
                input()


def five_by_five():
    moves = ["U", "D", "F", "B", "R", "L"]
    modifiers = ["", "'", "2"]
    last_move = ""
    second_last_move = ''
    repeatable = True
    repeated = 0
    scramble = ""

    while repeatable:
        invalid = False
        move = random.choice(moves)
        modifier = random.choice(modifiers)
        if move == last_move or move == second_last_move:
            invalid = True
        if move == "U":
            if second_last_move == "D":
                invalid = True
        if move == "D":
            if second_last_move == "U":
                invalid = True
        if move == "F":
            if second_last_move == "B":
                invalid = True
        if move == "B":
            if second_last_move == "F":
                invalid = True
        if move == "R":
            if second_last_move == "L":
                invalid = True
        if move == "L":
            if second_last_move == "R":
                invalid = True
        if not invalid:
            layer = random.randint(2, 3)
            if random.randint(0, 2) == 1:
                scramble = scramble + str(layer) + move + "w" + modifier + " "
                repeated += 1
                second_last_move = last_move
                last_move = move
            else:
                scramble = scramble + move + modifier + " "
                repeated += 1
                second_last_move = last_move
                last_move = move
        if repeated == 60:
            repeatable = False
            print(scramble)
            if not track:
                input()


def pyraminx():
    moves = ["U", "R", "L", "B"]
    modifiers = ["", "'"]
    last_move = ""
    repeatable = True
    repeated = 0
    scramble = ""

    while repeatable:
        invalid = False
        move = random.choice(moves)
        modifier = random.choice(modifiers)
        if move == last_move:
            invalid = True
        if not invalid:
            scramble = scramble + move + modifier + " "
            repeated += 1
            last_move = move
        if repeated == 10:
            while repeatable:
                move = random.choice(moves).lower()
                modifier = random.choice(modifiers)
                if move == last_move:
                    invalid = True
                if not invalid:
                    scramble = scramble + move + modifier + " "
                    repeated += 1
                    last_move = move
                if repeated == 14:
                    repeatable = False
            print(scramble)
            if not track:
                input()

def skewb():
    moves = ["U","R","L","B"]
    modifiers = ["", "'"]
    last_move = ""
    repeatable = True
    repeated = 0
    scramble = ""

    while repeatable:
        invalid = False
        move = random.choice(moves)
        modifier = random.choice(modifiers)
        if move == last_move:
            invalid = True
        if not invalid:
            scramble = scramble + move + modifier + " "
            repeated += 1
            last_move = move
        if repeated == 11:
            repeatable = False
            print(scramble)
            if not track:
                input()
def megaminx():
    moves = ["U","R","L","F","RD","LD"]
    modifiers = ["", "'", "++","--"]
    last_move = ""
    repeatable = True
    repeated = 0
    scramble = ""

    while repeatable:
        invalid = False
        move = random.choice(moves)
        modifier = random.choice(modifiers)
        if move == last_move:
            invalid = True
        if not invalid:
            scramble = scramble + move + modifier + " "
            repeated += 1
            last_move = move
        if repeated == 25 or repeated == 50 or repeated == 75:
            scramble = scramble + "\n"
        if repeated == 77:
            repeatable = False
            print(scramble)
            if not track:
                input()
# ======
# INPUTS
# ======

ans = input("1: Patterns\n2: Scramble\n")
if ans == '1':
    ans = input("1: 3x3\n2: 2x2\n3: 4x4\n5: 5x5\n")
    if ans == '1':
        print("1: Checkerboard\n"
                    "2: Superflip\n"
                    "3: Speedsolving.com logo\n"
                    "4: 3 Sides solved\n"
                    "5: All flags & crests\n"
                    "6: Wire\n"
                    "7: Checkerboard in the cube\n"
                    "8: Perfect scramble\n"
                    "9: Minority cross\n"
                    "10: Perpendicular lines\n"
                    "11: Flipped tips\n"
                    "12: Plus minus\n"
                    "13: Tablecloth\n"
                    "14: Deckerboard\n"
                    "15: Spiral pattern\n"
                    "16: Fruit bowl\n"
                    "17: Flower\n"
                    "18: Vertical stripes\n"
                    "19: Gift box\n"
                    "20: Opposite corners\n"
                    "21: Cross\n"
                    "22: 4 Crosses\n"
                    "23: Union Jack\n"
                    "24: Cube in the cube\n"
                    "25: Cube in a cube in a cube\n"
                    "26: Anaconda\n"
                    "27: Python\n"
                    "28: Black mamba\n"
                    "29: Green mamba\n"
                    "30: Tangled\n"
                    "31: 4 spots\n"
                    "32: 6 spots\n"
                    "33: Twister\n"
                    "34: Kilt\n"
                    "35: Tetris\n"
                    "36: Don't cross line\n"
                    "37: Hi\n"
                    "38: Hi all around\n"
                    "39: Displaced motif\n"
                    "40: Are you high?\n"
                    "41: C U around\n"
                    "42: Order in chaos\n"
                    "43: Evenly distributed\n"
                    "44: The hole\n"
                    "45: No entry\n"
                    "46: Plus\n"
                    "47: 3C3W\n"
                    "48: Pong\n")
        while True:
            ans = input()
            print("")
            if ans == '1':
                print("M2 E2 S2\n")
                print("Inverse: M2 E2 S2")
            elif ans == '2':
                print("U R2 F B R B2 R U2 L B2 R U' D' R2 F R' L B2 U2 F2\n")
                print("Inverse: F2 U2 B2 L' R F' R2 D U R' B2 L' U2 R' B2 R' B' F' R2 U'")
            elif ans == '3':
                print("R' L' U2 F2 D2 F2 R L B2 U2 B2 U2\n")
                print("Inverse: U2 B2 U2 B2 L' R' F2 D2 F2 U2 L R")
            elif ans == '4':
                print("U2 D R' D B' L2 B D' R L2 U2 B2 L2 B2 D R2 L2 D R2\n")
                print("Inverse: R2 D' L2 R2 D' B2 L2 B2 U2 L2 R' D B' L2 B D' R D' U2")
            elif ans == '5':
                print("B2 U' B2 L2 U B2 U R2 B2 U' L' R' B D U' L2 F2 R'\n")
                print("Inverse: R F2 L2 U D' B' R L U B2 R2 U' B2 U' L2 B2 U B2")
            elif ans == '6':
                print("R L F B R L F B R L F B R2 B2 L2 R2 B2 L2\n")
                print("Inverse: L2 B2 R2 L2 B2 R2 B' F' L' R' B' F' L' R' B' F' L' R'")
            elif ans == '7':
                print("B D F' B' D L2 U L U' B D' R B R D' R L' F U2 D\n")
                print("Inverse: D' U2 F' L R' D R' B' R' D B' U L' U' L2 D' B F D' B'")
            elif ans == '8':
                print("U F' L' U' R2 F' R2 B' U' R F' U F D' L2 F2 L2 U'\n")
                print("Inverse: U L2 F2 L2 D F' U' F R' U B R2 F R2 U L F U'")
            elif ans == '9':
                print("L2 D' B2 L2 B2 D' F2 D U' B2 L B2 F' L B' F U' F' U L2\n")
                print("Inverse: L2 U' F U F' B L' F B2 L' B2 U D' F2 D B2 L2 B2 D L2")
            elif ans == '10':
                print("R2 U2 L2 R2 U2 L2 M2\n")
                print("Inverse: M2 L2 U2 R2 L2 U2 R2")
            elif ans == '11':
                print("U B D' F2 D B' U' R2 D F2 D' R2 D F2 D' R2\n")
                print("Inverse: R2 D F2 D' R2 D F2 D' R2 U B D' F2 D B' U'")
            elif ans == '12':
                print("U2 R2 L2 U2 R2 L2\n")
                print("Inverse: L2 R2 U2 L2 R2 U2")
            elif ans == '13':
                print("R L U2 F' U2 D2 R2 L2 F' D2 F2 D R2 L2 F2 B2 D B2 L2\n")
                print("Inverse: L2 B2 D' B2 F2 L2 R2 D' F2 D2 F L2 R2 D2 U2 F U2 L' R'")
            elif ans == '14':
                print("U D R L' F' B U D' R2 U R2 L2 D2 F2 B2 D\n")
                print("Inverse: D' B2 F2 D2 L2 R2 U' R2 D U' B' F L R' D' U'")
            elif ans == '15':
                print("L' B' D U R U' R' D2 R2 D L D' L' R' F U\n")
                print("Inverse: U' F' R L D L' D' R2 D2 R U R' U' D' B L")
            elif ans == '16':
                print("B2 L2 F2 R2 F2 R2 D U B2 U2 B' F' L' R' D' U\n")
                print("Inverse: U D R L F B U2 B2 U' D' R2 F2 R2 F2 L2 B2")
            elif ans == '17':
                print("R2 D2 R2 U2 R2 F2 U2 D2 F2 U2\n")
                print("Inverse: U2 F2 D2 U2 F2 R2 U2 R2 D2 R2")
            elif ans == '18':
                print("F U F R L2 B D' R D2 L D' B R2 L F U F\n")
                print("Inverse: F' U' F' L' R2 B' D L' D2 R' D B' L2 R' F' U' F'")
            elif ans == '19':
                print("U B2 R2 B2 L2 F2 R2 D' F2 L2 B F' L F2 D U' R2 F' L' R'\n")
                print("Inverse: R L F R2 U D' F2 L' F B' L2 F2 D R2 F2 L2 B2 R2 B2 U'")
            elif ans == '20':
                print("R L U2 F2 D2 F2 R L F2 D2 B2 D2\n")
                print("Inverse: D2 B2 D2 F2 L' R' F2 D2 F2 U2 L' R'")
            elif ans == '21':
                print("R2 L' D F2 R' D' R' L U' D R D B2 R' U D2\n")
                print("Inverse: D2 U' R B2 D' R' D' U L' R D R F2 D' L R2")
            elif ans == '22':
                print("U2 R2 L2 F2 B2 D2 L2 R2 F2 B2\n")
                print("Inverse: B2 F2 R2 L2 D2 B2 F2 L2 R2 U2")
            elif ans == '23':
                print("U F B' L2 U2 L2 F' B U2 L2 U\n")
                print("Inverse: U' L2 U2 B' F L2 U2 L2 B F' U'")
            elif ans == '24':
                print("F L F U' R U F2 L2 U' L' B D' B' L2 U\n")
                print("Inverse: U' L2 B D B' L U L2 F2 U' R' U F' L' F'")
            elif ans == '25':
                print("U' L' U' F' R2 B' R F U B2 U B' L U' F U R F'\n")
                print("Inverse: F R' U' F' U L' B U' B2 U' F' R' B R2 F U L U")
            elif ans == '26':
                print("L U B' U' R L' B R' F B' D R D' F'\n")
                print("Inverse: F D R' D' B F' R B' L R' U B U' L'")
            elif ans == '27':
                print("F2 R' B' U R' L F' L F' B D' R B L2\n")
                print("Inverse: L2 B' R' D B' F L' F L' R U' B R F2")
            elif ans == '28':
                print("R D L F' R L' D R' U D' B U' R' D'\n")
                print("Inverse: D R U B' D U' R D' L R' F L' D' R'")
            elif ans == '29':
                print("R D R F R' F' B D R' U' B' U D2\n")
                print("Inverse: D2 U' B U R D' B' F R F' R' D' R'")
            elif ans == '30':
                print("F B U D F B U D F B U D F2 B2\n")
                print("Inverse: B2 F2 D' U' B' F' D' U' B' F' D' U' B' F'")
            elif ans == '31':
                print("M2 E M2 E'\n")
                print("Inverse: E M2 E' M2")
            elif ans == '32':
                print("E M' E' M\n")
                print("Inverse: M' E M E'")
            elif ans == '33':
                print("F R' U L F' L' F U' R U L' U' L F'\n")
                print("Inverse: F L' U L U' R' U F' L F L' U' R F'")
            elif ans == '34':
                print("U' R2 L2 F2 B2 U' R L F B' U F2 D2 R2 L2 F2 U2 F2 U' F2\n")
                print("Inverse: F2 U F2 U2 F2 L2 R2 D2 F2 U' B F' L' R' U B2 F2 L2 R2 U")
            elif ans == '35':
                print("L R F B U' D' L' R'\n")
                print("Inverse: R L D U B' F' R' L'")
            elif ans == '36':
                print("F2 L2 R2 B2 E2\n")
                print("Inverse: E2 B2 R2 L2 F2")
            elif ans == '37':
                print("M2 U2 M2 U2\n")
                print("Inverse: U2 M2 U2 M2")
            elif ans == '38':
                print("U2 R2 F2 U2 D2 F2 L2 U2\n")
                print("Inverse: U2 L2 F2 D2 U2 F2 R2 U2")
            elif ans == '39':
                print("L2 B2 D' B2 D L2 U R2 D R2 B U R' F2 R U' B' U'\n")
                print("Inverse: U B U R' F2 R U' B' R2 D' R2 U' L2 D' B2 D B2 L2")
            elif ans == '40':
                print("L R' U2 D2 L' R U2 D2 R2 L2\n")
                print("Inverse: L2 R2 D2 U2 R' L D2 U2 R L'")
            elif ans == '41':
                print("U' B2 U L2 D L2 R2 D' B' R D' L R' B2 U2 F' L' U'\n")
                print("Inverse: U L F U2 B2 R L' D R' B D R2 L2 D' L2 U' B2 U")
            elif ans == '42':
                print("B L2 B' U2 B F2 U L U B U' R U' B F U' R D R B' U'\n")
                print("Inverse: U B R' D' R' U F' B' U R' U B' U' L' U' F2 B' U2 B L2 B'")
            elif ans == '43':
                print("D' B2 D' L2 R2 D B2 L2 D' B2 L R' F' L2 D U' F2 R' D' U'\n")
                print("Inverse: U D R F2 U D' L2 F R L' B2 D L2 B2 D' R2 L2 D B2 D")
            elif ans == '44':
                print("R L' F' B D U'\n")
                print("Inverse: U D' B' F L R'")
            elif ans == '45':
                print("U' L' B R L' D' L B' U F2 R2 B2 D2 B2 R2 B2 D B2\n")
                print("Inverse: B2 D' B2 R2 B2 D2 B2 R2 F2 U' B L' D L R' B' L U")
            elif ans == '46':
                print("B2 F2 R2 U2 B2 F2 R2 U2 R2 U2\n")
                print("Inverse: U2 R2 U2 R2 F2 B2 U2 R2 F2 B2")
            elif ans == '47':
                print("D L B' L L F L' B' U D' R L' F B D L'\n")
                print("Inverse: L D' B' F' L R' D U' B L F' L' L' B L' D'")
            elif ans == '48':
                print("U R2 F2 B2 L2 U2 D R2 F2 B2 L2\n")
                print("Inverse: L2 B2 F2 R2 D' U2 L2 B2 F2 R2 U'")
            elif ans == 'q':
                quit()
            else:
                error(1)
    elif ans == '2':
        print("1: Checkerboard\n"
              "2: Superflip\n"
              "3: Cube in the cube\n"
              "4: Volleyball\n"
              "5: Displaced motif\n"
              "6: 2 Pillars")
        while True:
            ans = input()
            print("")
            if ans == '1':
                print("F2 R2 F2 U2")
            elif ans == '2':
                print("U R F2 U R F2 R U F' R")
            elif ans == '3':
                print("U2 F L F' U F' U L' F' L2")
            elif ans == '4':
                print("R2 U2 B2 R2")
            elif ans == '5':
                print("U R U' R2 U' R' F' U F2 R F'")
            elif ans == '6':
                print("U F2 U2 R2 U")
            else:
                error(1)
    elif ans == '3':
        print("")
        while True:
            ans = input()
            print("1: Parallel stripes\n"
                  "2: Stripes\n"
                  "3: Dots\n"
                  "4: Checkered dot\n"
                  "5: Opposite boxes\n"
                  "6: Cube in the cube\n"
                  "7: 3-Cube in the cube\n"
                  "8: Corner wrapper\n"
                  "9: Rings\n"
                  "10: Color peak\n")
            if ans == '1':
                print("d 2-3Rw2 d2 2-3Fw2 d 2-3Rw2 b2 r2 B2 2F2\n")
            elif ans == '2':
                print("F R2 2-3Dw' R2 B 2-3Dw R D2 B 2-3Rw 2-3Dw' F' R2 U' B2 u2 r2 U2 R2 f2 r2 2U2\n")
            elif ans == '3':
                print("U D' R L' F B' U D'\n")
            elif ans == '4':
                print("2-3Dw' 2-3Rw' 2U' 2D2 2F' 2D' 2U' 2B 2U 2-3Fw 2-3Rw \n")
            elif ans == '5':
                print("Bw2 Rw' Dw Rw Dw' Rw' Dw Rw Uw Rw' Dw' Rw Dw Rw' Dw' Rw Uw' Bw2\n")
            elif ans == '6':
                print("F L F U' R U F2 L2 U' L' B D' B' L2 U\n")
            elif ans == '7':
                print("B' 2R2 2L2 U2 2R2 2L2 B F2 R U' R U R2 U R2 F' U F' u l u' f2 d r' u f d2 r2\n")
            elif ans == '8':
                print("L U B' U' R L' B R' F B' D R D' F'\n")
            elif ans == '9':
                print("B' M2 U2 M2 B F2 R U' R U R2 U R2 F' U F' u l u' f2 d r' u f d2 r2\n")
            elif ans == '10':
                print("F U2 L F L' B L U B' R' L' U R' D' F' B R2\n")
            else:
                error(1)
    elif ans == '3':
        print("")
        while True:
            ans = input()
            print("1: Checkerboard\n"
                  "2: Half Superflip\n"
                  "3: Dots\n"
                  "4: Cube in the cube\n"
                  "5: Superflip\n"
                  "6: Flipped edges\n"
                  "7: Tri-Checkerboard\n")
            if ans == '1':
                print("R2 Rw2 L2 Lw2 U2 Uw2 D2 Dw2 B2 Bw2 F2 Fw2\n")
            elif ans == '2':
                print("m' U)x4 (x' y') (m' U)x4 (x' y') (m' U)x4 (x' y') (M' Uw)x4 (x' y') (M' Uw)x4 (x' y') (M' Uw)x4")
            elif ans == '3':
                print("U D' R L' F B' U D' Uw Dw' Rw Lw' Fw Bw' Uw Dw'\n")
            elif ans == '4':
                print("F U' B L U' F2 U2 F U F' U2 D' B D L2 B2 U Fw' Uw' Bw Lw Uw' Fw2 Uw2 Fw Uw Fw' Uw2 Dw' Bw Dw Lw2 Bw2 Uw")
            elif ans == '5':
                print("(m' U)x4 (x y') (m' U)x4 (x y') (m' U)x4 (x y') (M' Uw)x4 (x y') (M' Uw)x4 (x y') (M' Uw)x4)\n")
            elif ans == '6':
                print("F B2 R' D2 B R U D' R L' D' F' R2 D F2 B'\n")
            elif ans == '7':
                print("F B2 R' D2 B R U D' R L' D' F' R2 D F2 B' Fw Bw2 Rw' Dw2 Bw Rw Uw Dw' Rw Lw' Dw' Fw' Rw2 Dw Fw2 Bw'\n")
            else:
                error(1)
if ans == '2':
    if not bypass:
        while True:

            ans = input("Would you like to track times as you do solves? (Y/N) ").lower()
            if ans == "y":
                track = True
                break
            elif ans == "n":
                break
            else:
                error(1)

    while True:
        save()
        ans = input("1: 3x3 \n2: 2x2 \n3: 4x4 \n4: 5x5\n5: Pyraminx\n6: Skewb\n7: Megaminx\n").lower()

        if ans == "1":
            three_by_three()
            if track:
                while True:
                    try:
                        time = input("Input solve time: ")
                        if not time == "dnf":
                            time = int(time)
                            times_three.append(time)
                            break
                        else:
                            times_three.append("DnF")
                            break
                    except ValueError:
                        error(2)
        elif ans == "2":
            two_by_two()
            if track:
                while True:
                    try:
                        time = input("Input solve time: ")
                        if not time == "dnf":
                            time = int(time)
                            times_two.append(time)
                            break
                        else:
                            times_two.append("DnF")
                            break
                    except ValueError:
                        error(2)
        elif ans == "3":
            four_by_four()
            if track:
                while True:
                    try:
                        time = input("Input solve time: ")
                        if not time == "dnf":
                            time = int(time)
                            times_four.append(time)
                            break
                        else:
                            times_four.append("DnF")
                            break
                    except ValueError:
                        error(2)

        elif ans == "4":
            five_by_five()
            if track:
                while True:
                    try:
                        time = input("Input solve time: ")
                        if not time == "dnf":
                            time = int(time)
                            times_five.append(time)
                            break
                        else:
                            times_five.append("DnF")
                            break
                    except ValueError:
                        error(2)
        elif ans == "5":
            pyraminx()
            if track:
                while True:
                    try:
                        time = input("Input solve time: ")
                        if not time == "dnf":
                            time = int(time)
                            times_pyra.append(time)
                            break
                        else:
                            times_pyra.append("DnF")
                            break
                    except ValueError:
                        error(2)
        elif ans == "6":
            skewb()
            if track:
                while True:
                    try:
                        time = input("Input solve time: ")
                        if not time == "dnf":
                            time = int(time)
                            times_skewb.append(time)
                            break
                        else:
                            times_skewb.append("DnF")
                            break
                    except ValueError:
                        error(2)
        elif ans == "7":
            megaminx()
            if track:
                while True:
                    try:
                        time = input("Input solve time: ")
                        if not time == "dnf":
                            time = int(time)
                            times_megaminx.append(time)
                            break
                        else:
                            times_megaminx.append("DnF")
                            break
                    except ValueError:
                        error(2)

        else:
            error(1)
else:
    error(1)