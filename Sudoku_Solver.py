# Sudodu Solver
# Author : François Lebrun


import pandas as pd

class Sudoku:
    """Sudoku template :
        - editing a Sudoku grid
        - methods :
            o existinrow
            o existincol
            o exisinblock
    """
    def __init__(self,gridasadict):
        #number of element to guess default = 9
        self.sdim = len(gridasadict.keys())
        self.grid = pd.DataFrame(gridasadict)
        self.blocks = {0:(0,0),1:(0,3),2:(0,6),3:(3,0),4:(3,3),5:(3,6),6:(6,0),7:(6,3),8:(6,6)}  # row,col coordonate of  each block

    def whichblock(self,coord):
        """ returns block number depending on the cell coordinates
        input coord is a tuple (row number , col number )"""
        x,y = coord

        for param in self.blocks.keys():
            print (x,y)
            print(self.blocks[param])

            if (x > self.blocks[param][0]) and (y > self.blocks[param][1]):
                print("next")
                next
            else:
                print("stop")
                return param


    def existincol(self,coord):
        pass

    def existinrow(self,coord):
        pass

    def exisinblock(self,coord):
        pass



if __name__ == '__main__':

    grille = {0:(9,0,8,0,0,0,2,0,0),1:(0,0,0,0,0,0,0,0,0),2:(0,5,0,0,0,0,0,0,1),3:(1,0,0,0,7,0,3,2,9),4:(0,9,4,8,0,2,0,0,0),5:(0,0,0,0,0,6,0,0,4),6:(0,2,0,0,0,0,0,9,5),7:(0,0,0,0,0,0,0,0,7),8:(5,1,7,0,0,9,6,0,0)}
    sudoku = Sudoku(grille)
    print(sudoku.sdim)
    print(sudoku.grid)
    print(sudoku.whichblock((4,3)))
