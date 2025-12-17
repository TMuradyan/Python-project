import random, csv
from src.utils import inside, around

SIZES = [4,3,3,2,2,2,1,1,1,1]
DIRS = [(1,0),(0,1)]

def bot_ships():
    used = set()
    ships = []

    for size in SIZES:
        while True:
            r,c = random.randint(0,9), random.randint(0,9)
            dr,dc = random.choice(DIRS)
            cells = [(r+i*dr, c+i*dc) for i in range(size)]

            if not all(inside(x,y) for x,y in cells):
                continue

            bad = False
            for x,y in cells:
                for a,b in around(x,y):
                    if (a,b) in used:
                        bad = True
            if bad:
                continue

            ships.append(cells)
            for c in cells:
                used.add(c)
            break

    with open("data/bot_ships.csv","w",newline="") as f:
        csv.writer(f).writerows(ships)

    return ships
