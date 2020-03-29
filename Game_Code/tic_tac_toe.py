"""File Contains Class with functions to implement Player Enviroment"""
# pylint: disable-msg = W0702, C0103, R1705, R1710
import random


class TicTacToe:
    """Functions with Startgame() to start game and set Enviroment"""

    def __init__(self, name, level):
        """
        Initialize Board and Name
        :param name:
        """
        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]
        self.name = name
        self.level = level

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
        else:
            print("Already Selected  !!")
            self.mark_choice()
            return
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

    def gen_no_tough(self):
        """
        Static method to generate Number for CPU choice as per the Algorithm
        :return:
        """
        max_fill = 0
        symbol = 'O'
        for i in range(0, 3):
            if self.board[i].count(symbol) > max_fill:
                try:
                    x = i + 1
                    y = self.board[i].index(' ') +1
                    max_fill = self.board[i].count(symbol)
                except:
                    continue
        for j in range(0, 3):
            if [self.board[0][j], self.board[1][j], self.board[2][j]].count(symbol) > max_fill:
                try:
                    x = i+1
                    y = self.board[i].index(' ')+1
                    max_fill = [self.board[0][j], self.board[1][j], self.board[2][j]].count(symbol)
                except:
                    continue
        if [self.board[0][0], self.board[1][1], self.board[2][2]].count(symbol) > max_fill:
            try:
                x = y = self.board[i].index(' ') + 1
                max_fill = [self.board[0][j], self.board[1][j], self.board[2][j]].count(symbol)
            except:
                pass
        if [self.board[0][2], self.board[1][1], self.board[2][0]].count(symbol) > max_fill:
            try:
                x = y = self.board[i].index(' ') + 1
                max_fill = [self.board[0][j], self.board[1][j], self.board[2][j]].count(symbol)
            except:
                pass
        if max_fill == 0:
            return self.gen_random_no()
        else:
            return x, y

    def gen_random_no(self):
        """
        Static method to generate Random Number for CPU choice
        :return:
        """
        avai_index = list()
        for i in [0, 1, 2]:
            for j in [0, 1, 2]:
                if self.board[i][j] == ' ':
                    avai_index.append([i, j])
        indx = random.randint(0, len(avai_index)-1)
        return avai_index[indx][0], avai_index[indx][1]

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

    def mark_comp_choice(self, itr=0):
        """
        Function to mark CPU choice in board
        :param itr:
        :return:
        """
        if self.is_full() == 0:
            if self.level == 1:
                x, y = self.gen_random_no()
            else:
                x, y = self.gen_no_tough()
            if self.board[x - 1][y - 1] == ' ':
                self.board[x - 1][y - 1] = 'O'
            else:
                if itr <= 1:
                    itr += 1
                    self.mark_comp_choice(itr)
                    return
                else:
                    return "Unexpected Error"
        else:
            return "Game Over"
        return

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
        level = int(input("Enter Level Easy/Tough (1/2) : "))
        play = TicTacToe(name, level)
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


if __name__ == "__main__":
    TicTacToe.start_game()
