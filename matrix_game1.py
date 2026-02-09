import numpy as np
import random

#Note, much of the logic is zero indexed, but I try to keep anything that interacts with the user to be 1-indexed
n = 4    #matrix size
TOL = 1e-8  #tolerance for determinant since floating point errors mean the determinant may not exactly equal zero

HUMAN = 0         
BOT   = 1      

board = np.full((n, n), -1, dtype=int)    #makes the matrix, -1 means that entry is currently empty

def print_board():
    print("Board:")
    for r in range(n):
        row = []
        for c in range(n):
            v = board[r, c]
            row.append("-" if v == -1 else str(v))
        print(" ".join(row))
    print()

def is_full():
    return np.all(board != -1)

def is_singular(A):
    return abs(np.linalg.det(A)) < TOL

def verify(r, c):
    return 0 <= r < n and 0 <= c < n and board[r, c] == -1

def bot_random_move():
    empties = []
    for r in range(n):
        for c in range(n):
            if board[r, c] == -1:
                empties.append((r, c))
    return random.choice(empties)



def game(player):
    global board

    print_board()

    if is_full():
        d = np.linalg.det(board)
        print(f"Final determinant ~ {d:.3e}")
        if is_singular(board):
            print("HUMAN WON (det = 0)")
        else:
            print("BOT WON (det ≠ 0)")
        return

    if player == HUMAN:   #human turn
        try:
            r, c = map(int, input("Your move (row col, 1-indexed): ").split())
            r -=1
            c-=1
        except:
            print("Invalid input. Use: row col")
            return game(HUMAN)

        if not verify(r, c):
            print("Illegal move. Try again.")
            return game(HUMAN)

        board[r, c] = 0
        return game(BOT)

    if player == BOT:   #bot turn
        r, c = bot_random_move()
        print(f"BOT plays at ({r+1}, {c+1})")
        board[r, c] = 1
        return game(HUMAN)

game(BOT)    #Plays the game
