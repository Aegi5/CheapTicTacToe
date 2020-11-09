#Set term environment variable in Run/Debug conf

#Ideas
# board
# display board
# play game
# handle turn
# check win
    #check last movement, rows, columns , diags
# check tie, if entire board is full and no winner
# change player

import os
from Board import Board
from Player import Player
os.system("clear")

board = Board()
player = Player()
def print_header():
    print("Welcome to Tic-Tac-Toe\n")

def refresh_screen():
    #clear screen
    os.system("clear")

    #print header
    print_header()

    #show the board
    board.display()


while True:
    refresh_screen()

    #get X/O input
    #take input and convert to int
    choice = int(input("\n {}) Choose 1 - 9. >".format(player.cur_player)))

    #update board
    board.update_cell(choice, "{}".format(player.cur_player))

    #check for win
    if board.is_winner(player.cur_player, choice):
        print("{} est le vainqueur !" .format(player.cur_player))
        board.display()
        break

    #check tie
    if board.tie():
        print("INSANE PLAY FROM BOTH PARTIES ! Match ended in a tie !")
        break
    player.next_player()

