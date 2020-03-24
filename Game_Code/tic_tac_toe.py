"""File Contains Class with functions to implement Player Enviroment"""
# pylint: disable-msg = C0103, R1705, R1710
import random


class TicTacToe:
    """Functions with Startgame() to start game and set Enviroment"""

    def __init__(self, name):
        """
        Initialize Board and Name
        :param name:
        """
        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]
        self.name = name

    def mark_choice(self):
        """
        Mark Player Choice
        :return:
        """
        print("Enter Your Choice")
        x = int(input("Enter Row Number : "))
        y = int(input("Enter Col Number : "))
        if (x not in range(1, 4)) or (y not in range(1, 4)):
            print("Invalid Choice !!")
            self.mark_choice()
            return
        if self.board[x - 1][y - 1] == ' ':
            self.board[x - 1][y - 1] = 'X'
            return
        else:
            print("Already Selected  !!")
            self.mark_choice()
            return

    def check_win(self, symbol):
        """
        Check Win Condition for Particular Symbol
        :param symbol:
        :return:
        """
        for i in range(0, 3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == symbol:
                return 1
        for j in range(0, 3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] == symbol:
                return 1
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] == symbol) or \
                (self.board[0][2] == self.board[1][1] == self.board[2][0] == symbol):
            return 1
        return 0

    @staticmethod
    def gen_no():
        """
        Static method to generate Random Number for CPU choice
        :return:
        """
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        return x, y

    def is_full(self):
        """
        Check if board is full
        :return:
        """
        count = 0
        for i in self.board:
            for j in i:
                if j == ' ':
                    count += 1
        if count == 0:
            return 1
        else:
            return 0

    def mark_comp_choice(self):
        """
        Function to mark CPU choice in board
        :return:
        """
        x, y = TicTacToe.gen_no()
        if self.board[x - 1][y - 1] == ' ':
            self.board[x - 1][y - 1] = 'O'
            return
        else:
            if self.is_full():
                return "Game Over"
            self.mark_comp_choice()

    def print_board(self):
        """
        Print Board
        :return:
        """
        print("-------------------------------------------------------\n")
        print("\t\t", self.board[0][0], " | ", self.board[0][1], " | ", self.board[0][2])
        print("\t\t", "--------------", )
        print("\t\t", self.board[1][0], " | ", self.board[1][1], " | ", self.board[1][2])
        print("\t\t", "--------------", )
        print("\t\t", self.board[2][0], " | ", self.board[2][1], " | ", self.board[2][2])
        print("\n-------------------------------------------------------")

    @staticmethod
    def start_game():
        """
        Function to start and set playing Enviroment
        :return:
        """
        print("-----------Welcome To The Game-----------\n")
        name = input("Enter Player Name : ")
        play = TicTacToe(name)
        print("Player 1 (X) : " + play.name + "\nPlayer 2 (O) : Computer")
        win = 0
        while win == 0:
            play.print_board()
            play.mark_choice()
            play.mark_comp_choice()
            win = (play.check_win('X')) or (play.check_win('O'))
            if play.is_full() and win == 0:
                play.print_board()
                print("\n\n----------------------------------------------------------------")
                print("It is a Draw")
                return
        play.print_board()
        if play.check_win('X') == 1:
            print("\n\n----------------------------------------------------------------")
            print("Congrats " + play.name + " You Won !!!")
        elif play.check_win('O') == 1:
            print("\n\n----------------------------------------------------------------")
            print("Hey " + play.name + " You Lost !!!")


if __name__== "__main__":
    TicTacToe.start_game()
