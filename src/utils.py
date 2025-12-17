SIZE = 10

def inside(r, c):
    return 0 <= r < SIZE and 0 <= c < SIZE

def around(r, c):
    return [(r+dr, c+dc) for dr in [-1,0,1] for dc in [-1,0,1]]

def empty_board():
    return [["." for _ in range(SIZE)] for _ in range(SIZE)]

def show(board, title):
    print("\n" + title)
    for row in board:
        print(" ".join(row))
