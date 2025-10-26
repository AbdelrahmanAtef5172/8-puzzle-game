import time
from State import State

# Depth-Limited Search (used inside IDDFS)
def depth_limited_search(state, limit, explored, parents, nodes_expanded):
    # Check if goal reached
    if state.isGoal():
        return state, nodes_expanded

    # Stop if depth limit reached
    if limit <= 0:
        return None, nodes_expanded

    explored.add(state)
    neighbours = state.getNeighbours()

    # Explore each neighbour
    for neighbour in neighbours:
        if neighbour not in explored:
            parents[neighbour] = (state, parents[state][1] + 1)
            nodes_expanded += 1
            result, nodes_expanded = depth_limited_search(neighbour, limit - 1, explored, parents, nodes_expanded)
            if result is not None:
                return result, nodes_expanded

    return None, nodes_expanded


# Iterative Deepening DFS algorithm
def iterative_deepening_dfs(initialState: State, max_depth=50):
    start_time = time.time()
    nodes_expanded = 0

    # Try increasing depth limit step by step
    for limit in range(max_depth + 1):
        explored = set()
        parents = {initialState: (None, 0)}
        nodes_expanded += 1

        result, nodes_expanded = depth_limited_search(initialState, limit, explored, parents, nodes_expanded)
        if result is not None:
            end_time = time.time()
            running_time = end_time - start_time

            # Reconstruct path
            path = []
            cur = result
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
            print(f"Search Depth: {len(path) - 1}")
            print(f"Nodes Expanded: {nodes_expanded}")
            print(f"Running Time: {running_time:.6f} seconds")
            return path , len(path) , len(path) - 1,nodes_expanded,running_time

    print("NO SOLUTION FOUND WITHIN DEPTH LIMIT")
    return None


# Run the algorithm (example)
if __name__ == "__main__":
    path ,path_length,depth,nodes,running_time= iterative_deepening_dfs(State([[1,2,3],[4,5,6],[7,8,0]]))
