import copy
class State :

    # CLASS CONSTRUCTOR
    def __init__ (self , tiles):
        self.tiles = tiles

    # CHECK IF THIS STATE IS GOAL STATE
    def isGoal(self):
        number_comparing = 0
        # looping through the 2d array
        for i in range(3):
           for j in range(3) :
               # checking the first tile
               if i==0 and j==0 :
                   if(self.tiles[i][j]!=" "):
                       return False
               else :
                   number_comparing+=1
                   if(self.tiles[i][j]!= number_comparing):
                       return False
        return True
    
    # Get the positon of the empty tile in 2d array
    def getEmptyTilePosition(self):
        for i in range(3):
            for j in range(3):
                if(self.tiles[i][j]==" "):
                    return i , j
    
    # get copy of current state
    def getCopy(self):
        return copy.deepcopy(self.tiles)    

    # Get the neighbours of the state
    def getNeighbours(self):
        neighbours=[]
        i , j = self.getEmptyTilePosition()
        for row , column in [[i+1,j],[i,j+1],[i-1,j],[i,j-1]]:
            if ( 3>row>=0 and 3>column>=0):
                copiedArray = self.getCopy()
                temp = copiedArray[i][j]
                copiedArray[i][j]= copiedArray[row][column]
                copiedArray[row][column] = temp
                neighbours.append(copiedArray)
        return neighbours
    

    

                       


