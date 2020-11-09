class Board():
    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

        # one more cell to get non null number coordinates

    def display(self):
        print("%s | %s | %s " % (self.cells[1], self.cells[2], self.cells[3]))
        print("----------")
        print("%s | %s | %s " % (self.cells[4], self.cells[5], self.cells[6]))
        print("---------")
        print("%s | %s | %s " % (self.cells[7], self.cells[8], self.cells[9]))

    def update_cell(self, cell_nb, player):
        if self.cells[cell_nb] == " ":
            self.cells[cell_nb] = player
        else:
            print('NOP')

    def check_rows(self, lastPlayer, choice):

        choice -= 1
        q = choice // 3 + 1
        cpt = 0
        for i in range(0, 3):
            if self.cells[i + q] == choice:
                cpt += 1
        if cpt == 3:
            return True
        else:
            return False

    def check_columns(self, lastPlayer, choice):
        """
        usage du mod pour déterminer la colonne
        """
        cpt = 0
        mod = choice % 3
        if mod == 0:
            mod = 3
        for i in range(0, 3):
            if self.cells[mod + i * 3] == choice:
                cpt += 1
        if cpt == 3:
            return True
        else:
            return False

    def check_diags(self, lastPlayer):
        """
        une seule diagonale à checker ici
        """
        if self.cells[5] == " ":
            return False
        # on s'intéresse à celles qui se croisent en 4
        if (self.cells[1] == lastPlayer
                and self.cells[5] == lastPlayer
                and self.cells[9] == lastPlayer):
            return True
        elif (self.cells[3] == lastPlayer
              and self.cells[5] == lastPlayer
              and self.cells[7] == lastPlayer):
            return True

    def is_winner(self, lastPlayer, choice):
        return (self.check_diags(lastPlayer) or self.check_rows(lastPlayer, choice) or self.check_columns(lastPlayer,
                                                                                                          choice))
        # make the script ignore the index outta bounds ?

    def tie(self):
        for i in range(1,10):
            if(self.cells[i] != " "):
                #game isn't finished yet
                return False
        #all cells are full and no winner ? it's a tie !
        return True