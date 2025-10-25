import copy
class State:

    # CLASS CONSTRUCTOR
    def __init__(self, tiles, parent=None, action=None):
        self.tiles = tiles            
        self.parent = parent      
        self.action = action
    # METHOD TO CHECK THE CURRENT STATE IS GOAL
    def isGoal(self):
        goal = [[0,1,2],[3,4,5],[6,7,8]]
        return self.tiles == goal
    # METHOD TO GET THE POSITION OF 0 TILE
    def getEmptyTilePosition(self):
        for i in range(3):
            for j in range(3):
                if self.tiles[i][j] == 0:
                    return i, j     
    # METHOD RETURNS A DEEP COPY OF THE STATE (with parent cleared, will be assigned later)
    def getCopy(self):
        return State(copy.deepcopy(self.tiles))
    # METHOD TO GET THE NEIGHBOURS OF THE CURRENT STATE
    def getNeighbours(self):
        neighbours = []
        i, j = self.getEmptyTilePosition()
        moves = {
            (1,0): "Down",
            (-1,0): "Up",
            (0,1): "Right",
            (0,-1): "Left"}
        for (di, dj), move in moves.items():
            row, col = i + di, j + dj
            # out of border checks
            if 0 <= row < 3 and 0 <= col < 3:
                new_state = self.getCopy()
                # swap tiles
                new_state.tiles[i][j], new_state.tiles[row][col] = new_state.tiles[row][col], new_state.tiles[i][j]
                # set parent and action
                new_state.parent = self
                new_state.action = move
                neighbours.append(new_state)
        return neighbours
    # EQUAL OPERATOR
    def __eq__(self, other):
        return self.tiles == other.tiles
    # TO USE SETS
    def __hash__(self):
        return hash(str(self.tiles))
