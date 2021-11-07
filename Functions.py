import tkinter as tk
from tkinter import messagebox

import pygame


def run_again(group, board):
    for sprite in group:
        sprite.is_x = False
        sprite.was_clicked = False
        sprite.image = pygame.Surface((150, 150))
    for i in range(3):
        for j in range(3):
            board[i][j] = 0
    clicked = False

def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


def check(board):
    sum_horizontal = 0
    sum_vertical = 0
    for i in range(3):
        for j in range(3):
            sum_horizontal += board[i][j]
            sum_vertical += board[j][i]
        if sum_horizontal == 3 or sum_vertical == 3:
            return 1
        elif sum_horizontal == -3 or sum_vertical == -3:
            return -1
        sum_vertical, sum_horizontal = 0, 0
    j = 2
    for i in range(3):
        sum_horizontal += board[i][i]
        sum_vertical += board[i][j - i]

    if sum_horizontal == 3 or sum_vertical == 3:
        return 1
    elif sum_horizontal == -3 or sum_vertical == -3:
        return -1

    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return 0
    return 2