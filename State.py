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
    
    

                       


