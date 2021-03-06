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
        self.step = 3
        self.grid = pd.DataFrame(gridasadict)
        self.blocks = {0:(0,0),1:(0,3),2:(0,6),3:(3,0),4:(3,3),5:(3,6),6:(6,0),7:(6,3),8:(6,6)}  # row,col coordonate of  each block

    def whichblock(self,coord):
        """ returns block number depending on the cell coordinates
        input coord is a tuple (row number , col number )

        coordinates belong to interval [0,8]
        """
        x,y = coord

        for param in self.blocks.keys():
            if (x in range(self.blocks[param][0] , self.blocks[param][0] + self.step)) and (y in range(self.blocks[param][1] , self.blocks[param][1] + self.step)):
                return param

    def prioritizecells(self):
        """Sort each empty cell by decreasing complexity number """
        rowmax, colmax = self.grid.shape
        self.grade = pd.DataFrame()
        grades = []
        for col in range(0,colmax):
            for row in range(0,rowmax):
                if self.grid.loc[row,col] == 0:
                    self.grade.loc[row,col] = self.gradecell((row,col))
                    grades.append( self.gradecell((row,col)) )
                else:
                    self.grade.loc[row,col] = 0
        grades = set(grades)

        # Create a dict with rank oh each grades
        inc = 1
        gradesdict={}
        gradesdict[0] = 0
        for grade in set(grades) :
            gradesdict[grade] = inc
            inc += 1


        givengrade = 1
        self.gradetmp = pd.DataFrame()
        for col in range(0,colmax):
            for row in range(0,rowmax):
                for grade in grades:
                    if self.grade.loc[row,col] == grade:
                        print(self.grade.loc[row,col] , grade)
                        self.gradetmp.loc[row,col] = gradesdict[grade]
                        break
                    else:
                        self.gradetmp.loc[row,col] = 0



    def gradecell(self,coords):
        """ Returns how many blanks are to be filled based on a tuple of cell's cordinates
        cell's grade is called 'complexity number' """
        row , col = coords
        block_number = self.whichblock(coords)
        return self.existinblock(block_number) + self.existincol(col) + self.existinrow(row)

    def existincol(self,col_number):
        """ Returns how many unsolved cells in a column """
        values = self.grid.loc[:,col_number]
        return list(values).count(0)

    def existinrow(self,row_number):
        """ Returns how many unsolved cells in a row """
        values = self.grid.loc[row_number,:]
        return list(values).count(0)

    def existinblock(self,block_number):
        """ Returns how many unsolved cells in a block of cells """
        x_origin , y_origin = self.blocks[block_number]
        subset = self.grid.loc[range(x_origin , (x_origin + self.step)),:]
        subset = subset.loc[:,range(y_origin ,(y_origin + self.step))]
        values = []
        for col in subset.columns :
            for val in list(subset.loc[:,col]):
                values.append(val)
        return values.count(0)




if __name__ == '__main__':

    grille = {0:(9,0,8,0,0,0,2,0,0),1:(0,0,0,0,0,0,0,0,0),2:(0,5,0,0,0,0,0,0,1),3:(1,0,0,0,7,0,3,2,9),4:(0,9,4,8,0,2,0,0,0),5:(0,0,0,0,0,6,0,0,4),6:(0,2,0,0,0,0,0,9,5),7:(0,0,0,0,0,0,0,0,7),8:(5,1,7,0,0,9,6,0,0)}
    sudoku = Sudoku(grille)
    print(sudoku.grid)
    print(sudoku.whichblock((6,2)))
    print(sudoku.gradecell((4,4)))
    sudoku.prioritizecells()
    print(sudoku.grade)
    print(sudoku.gradetmp)
