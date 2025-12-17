import csv
from src.utils import inside, around

SIZES = [4,3,3,2,2,2,1,1,1,1]

def input_ships():
    used = set()
    ships = []

    for size in SIZES:
        while True:
            print(f"Ship size {size}")
            coords = input("Enter cells (ex: 1,1 1,2 1,3): ").split()

            if len(coords) != size:
                print("Wrong size")
                continue

            cells = []
            ok = True
            for c in coords:
                r, col = map(int, c.split(","))
                if not inside(r, col):
                    ok = False
                for x,y in around(r,col):
                    if (x,y) in used:
                        ok = False
                cells.append((r,col))

            if ok:
                ships.append(cells)
                for c in cells:
                    used.add(c)
                break
            else:
                print("Invalid placement")

    with open("data/player_ships.csv","w",newline="") as f:
        csv.writer(f).writerows(ships)

    return ships
