class Player():
    O = "O"
    X = "X"

    def __init__(self):
        self.cur_player = self.O

    def next_player(self):
        if self.cur_player == Player.O:
            self.cur_player = Player.X
        else:
            self.cur_player = Player.O

    def __str__(self):
        return self.cur_player



