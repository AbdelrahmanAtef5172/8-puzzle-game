import time
from collections import deque
from State import State

def breadth_first_search(initialState: State):

    start_time = time.time()    
    # INITIALIZING THE VARIABLES
    # frontier holds (current state, depth)
    frontier = deque([(initialState, 0)])
    explored = set()
    nodes_expanded = 0

    # LOOPING UNTIL THE FRONTIER IS EMPTY OR YOU REACH THE GOAL
    while frontier:
        state, depth = frontier.popleft()
        # IF STATE ALREADY EXPLORED THEN SKIP
        if state in explored:
            continue
        #ADDING THE CURRENT STET TO EXPLORED SET
        explored.add(state)
        nodes_expanded += 1
        # CHECKING IF THE CURRENT STATE IS GOAL
        if state.isGoal():
            end_time = time.time()
            # CALCULATING THE RUNNING TIME TAKEN
            running_time = end_time - start_time
            # GETTING THE PATH FROM THE STATE TO THE ROOT USING PARENT
            path = []
            moves= []
            cur = state
            while cur is not None:
                path.append(cur)
                moves.append(cur.action)
                cur = cur.parent
            path.reverse()
            moves.reverse()

            print("THE GOAL IS FOUND ")
            for tile in path:
                for row in tile.tiles:
                    print(row)
                print("\n")
            print(f"Cost of Path: {len(path)-1}")  
            print(f"Search Depth: {len(path)-1}")
            print(f"Nodes Expanded: {nodes_expanded}")
            print(f"Running Time: {running_time:.6f} seconds")
            return path , moves,len(path)-1,len(path)-1,nodes_expanded,running_time

        # EXPANDING THE NEIGHBOURS IF GOAL NOT FOUND
        neighbours = state.getNeighbours()
        for neighbour in neighbours:
            if neighbour not in explored:
                # ADDING NEIGHBOUR TO THE FRONTIER WITH UPDATED DEPTH
                frontier.append((neighbour, depth+1))

    print("NO SOLUTION")
    return None


path,moves,path_length,depth,nodes,running_time = breadth_first_search(State([[1,2,3],[4,5,6],[7,8,0]]))
