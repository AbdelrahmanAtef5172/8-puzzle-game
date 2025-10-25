import copy

class State:

    # CLASS CONSTRUCTOR
    # (Fixed: Added parent=None)
    def __init__(self, tiles, parent=None, g=0):
        self.tiles = tiles
        self.parent = parent  # <--- Parent is now formally defined
        self.g = g
        self.h = 0
        self.f = 0

    # METHOD TO CHECK THE CURRENT STATE IS GOAL
    def __lt__(self, other):
        if self.f == other.f:
            return self.h < other.h
        return self.f < other.f
    
    def isGoal(self):
        goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        return self.tiles == goal

    # METHOD TO GET THE POSITION OF 0 TILE
    def getEmptyTilePosition(self):
        for i in range(3):
            for j in range(3):
                if self.tiles[i][j] == 0:
                    return i, j

    # METHOD RETURNS A DEEP COPY OF THE STATE
    def getCopy(self):
        return State(copy.deepcopy(self.tiles))

    # METHOD GET THE NEIGHBOURS OF THE CURRENT STATE
    def getNeighbours(self):
        n = len(self.tiles)
        neighbours = []
        i, j = self.getEmptyTilePosition()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left
        
        for di, dj in directions:
            row, col = i + di, j + dj
            if 0 <= row < 3 and 0 <= col < 3:
                
                new_state = self.getCopy()
                new_state.g = self.g + 1  # <--- g-cost is set here
                new_state.parent = self  # <--- Parent is set here
                new_state.tiles[i][j], new_state.tiles[row][col] = new_state.tiles[row][col], new_state.tiles[i][j]
                neighbours.append(new_state)
                
        return neighbours

    # EQUAL OPERATOR
    def __eq__(self, other):
        return self.tiles == other.tiles

    # TO USE SETS
    def __hash__(self):
        # (Fixed: This is the standard, faster, and safer way to hash a 2D list)
        return hash(tuple(tuple(row) for row in self.tiles)) 
    
    def reverse_path(self):
        """
        Traces back the path from this node to the start.
        """
        path = []
        current = self
        # (Fixed: Simpler loop now that .parent is guaranteed)
        while current is not None:
            path.append(current)
            current = current.parent
        path.reverse()
        return path
    
    def __repr__(self):
        """
        Helper for printing the board nicely (Added for testing).
        """
        s = ""
        for row in self.tiles:
            for tile in row:
                s += f"{'_' if tile == 0 else tile:2} "
            s += "\n"
        return s