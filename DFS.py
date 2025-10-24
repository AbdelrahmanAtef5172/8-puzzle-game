import time
from State import State

def depth_first_search(initialState: State):
    start_time = time.time()        
    #INITIALIZING THE VARIABLES
    # current state # depth #parent  
    frontier = [(initialState, 0, None)]  
    explored = set()
    nodes_expanded = 0
    #DICTIONARY TO HOLD THE PARENT OF EACH STATE
    parents = {}   
    #LOOPING UNTIL THE FRONTIER IS EMPTY OR YOU REACH THE GOAL
    while frontier:
        state, depth, parent = frontier.pop()
        if state in explored:
            continue
        explored.add(state)
        parents[state] = (parent, depth)
        nodes_expanded += 1

        if state.isGoal():
            end_time = time.time()
            #CALCULATING THE RUNNING TIME TAKEN
            running_time = end_time - start_time
            #GETTING THE PATH FROM THE STATE TO THE ROOT
            path = []
            cur = state
            while cur is not None:
                path.append(cur)
                cur, _ = parents[cur]
            path.reverse()
            print("THE GOAL IS FOUND ")
            for tile in path:
                for row in tile.tiles:
                    print(row)
                print("\n")

            print(f"Cost of Path: {len(path)}")
            print(f"Search Depth: {depth}")
            print(f"Nodes Expanded: {nodes_expanded}")
            print(f"Running Time: {running_time:.6f} seconds")

            return path

        #EXPANDING THE NEIGHBOURS IF GOAL NOT FOUND
        neighbours = state.getNeighbours()
        for neighbour in neighbours:
            if neighbour not in explored:
                frontier.append((neighbour, depth+1, state))

    print("NO SOLUTION ")
    return None

path = depth_first_search(State([[1,2,3],[4,5,6],[7,8,0]]))