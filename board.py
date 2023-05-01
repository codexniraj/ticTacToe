class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"

    def make_move(self, position):
        if self.board[position] == " ":
            self.board[position] = self.current_player
            if self.current_player == "X":
                self.current_player = "O"
            else:
                self.current_player = "X"

    def check_win(self):
        return ((self.board[0] != " " and self.board[0] == self.board[1] == self.board[2]) or
                (self.board[3] != " " and self.board[3] == self.board[4] == self.board[5]) or
                (self.board[6] != " " and self.board[6] == self.board[7] == self.board[8]) or
                (self.board[0] != " " and self.board[0] == self.board[3] == self.board[6]) or
                (self.board[1] != " " and self.board[1] == self.board[4] == self.board[7]) or
                (self.board[2] != " " and self.board[2] == self.board[5] == self.board[8]) or
                (self.board[0] != " " and self.board[0] == self.board[4] == self.board[8]) or
                (self.board[2] != " " and self.board[2] == self.board[4] == self.board[6]))

    def check_tie(self):
        return " " not in self.board and not self.check_win()
