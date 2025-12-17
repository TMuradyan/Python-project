import csv, random
from src.utils import empty_board, show, around

def load(path):
    ships = []
    with open(path) as f:
        for row in csv.reader(f):
            ships.append([eval(x) for x in row])
    return ships


def game():
    player = load("data/player_ships.csv")
    bot = load("data/bot_ships.csv")

    pb = empty_board()
    bb = empty_board()

    bot_shots = set()
    bot_targets = []

    turn = 1

    with open("data/game_state.csv","w",newline="") as log:
        writer = csv.writer(log)
        writer.writerow(["turn","player","bot"])

        while player and bot:

            while True:
                show(bb,"BOT")
                r,c = map(int,input("Your shot r,c: ").split(","))

                hit = False
                for s in bot:
                    if (r,c) in s:
                        s.remove((r,c))
                        bb[r][c] = "X"
                        hit = True
                        if not s:
                            bot.remove(s)
                            for x,y in around(r,c):
                                if 0<=x<10 and 0<=y<10 and bb[x][y]==".":
                                    bb[x][y]="o"
                        break

                if not hit:
                    bb[r][c]="o"

                writer.writerow([turn,f"{r,c} {hit}","-"])
                turn += 1

                if not hit:
                    break 

            while player:
                if bot_targets:
                    br, bc = bot_targets.pop(0)
                else:
                    while True:
                        br,bc = random.randint(0,9), random.randint(0,9)
                        if (br,bc) not in bot_shots:
                            break

                bot_shots.add((br,bc))

                hit2 = False
                for s in player:
                    if (br,bc) in s:
                        s.remove((br,bc))
                        pb[br][bc] = "X"
                        hit2 = True

                        if len(s) > 0:
                            for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                                nr,nc = br+dr, bc+dc
                                if 0<=nr<10 and 0<=nc<10:
                                    if (nr,nc) not in bot_shots and (nr,nc) not in bot_targets:
                                        bot_targets.append((nr,nc))

                        if not s:
                            player.remove(s)
                            bot_targets.clear()
                            for x,y in around(br,bc):
                                if 0<=x<10 and 0<=y<10 and pb[x][y]==".":
                                    pb[x][y]="o"
                        break

                if not hit2:
                    pb[br][bc]="o"

                show(pb,"YOU")
                writer.writerow([turn,"-",f"{br,bc} {hit2}"])
                turn += 1

                if not hit2:
                    break 

    print("GAME OVER")
