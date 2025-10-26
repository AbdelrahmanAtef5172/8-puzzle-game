
import time
import heapq # For the Priority Queue
from State import State # <-- Importing the class from your file

# --- Global Constants ---
# Define the goal state once
GOAL_TILES = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# --- Heuristic Function ---

def misplaced_tiles(state: State):
    """
    Calculates the 'Misplaced Tiles' heuristic (h-cost).
    Counts how many tiles are not in their correct final position.
    """
    count = 0
    n = len(state.tiles)
    for r in range(n):
        for c in range(n):
            current_tile = state.tiles[r][c]
            goal_tile = GOAL_TILES[r][c]
            
            # If the tile is not 0 AND it's not in its goal spot
            if current_tile != 0 and current_tile != goal_tile:
                count += 1
    return count

# --- Helper Function for Printing ---

def print_solution(path, nodes_expanded, time_taken):
    """
    Helper function to print the final solution and statistics.
    """
    print("THE GOAL IS FOUND!")
    print(f"Nodes Expanded: {nodes_expanded}")
    print(f"Search Depth (g-cost): {path[-1].g}") # Get g-cost from goal node
    print(f"Running Time: {time_taken:.6f} seconds")
    print(f"Cost of Path (Steps): {len(path) - 1}")
    print("\n--- Traceable Path ---")
    for state in path:
        print(state) # This uses the __repr__ method from State

# --- A* Search Function (Standalone) ---

def solve_astar(initial_tiles, heuristic_func):
    """
    Performs the A* search algorithm.
    :param initial_tiles: The 2D list of the starting board.
    :param heuristic_func: The heuristic function to use (e.g., misplaced_tiles).
    """
    
    # 1. Initialization
    print(f"--- Starting A* (Heuristic: {heuristic_func.__name__}) ---") 
    start = time.time()       # Get the start time
    nodes_expanded = 0        # Counter for expanded nodes
    
    # 2. Prepare the start node
    start_node = State(initial_tiles)
    start_node.g = 0                          # g-cost (path cost) is 0
    start_node.h = heuristic_func(start_node) # h-cost (heuristic)
    start_node.f = start_node.g + start_node.h  # f-cost (total)

    # 3. Initialize the Frontier (Priority Queue)
    frontier = []
    heapq.heappush(frontier, start_node)
    
    # 4. Initialize the Explored Set
    explored_hashes = set()
    # (This logic is fine, it adds to explored *before* checking)
    explored_hashes.add(hash(start_node))

    # 5. Main Search Loop
    while frontier:
        # 6. Get the best node
        current_state = heapq.heappop(frontier)

        # 9. Goal Check
        if current_state.isGoal():
            end_time = time.time()
            path = current_state.reverse_path() # This will work now
            print_solution(path, nodes_expanded, end_time - start)
            return path # Solution found!
        
        # 10. Increment node counter
        nodes_expanded += 1
        
        # 11. Expand and process Neighbours
        for neighbor in current_state.getNeighbours():
            neighbor_hash = hash(neighbor)
            
            # 12. Check if neighbour is new
            if neighbor_hash not in explored_hashes:
                # 13. Calculate costs and set parent
                # (Fixed: g and parent are now set by getNeighbours)
                # (We only need to calculate h and f)
                neighbor.h = heuristic_func(neighbor) # Calculate heuristic
                neighbor.f = neighbor.g + neighbor.h  # Calculate total f-cost
                
                # 14. Add to frontier
                heapq.heappush(frontier, neighbor)
                
                # 15. Mark as explored
                explored_hashes.add(neighbor_hash)
    
    # 16. No Solution
    print("NO SOLUTION FOUND")
    return None

# --- Main execution block ---
if __name__ == "__main__":
    
    # The starting puzzle from your assignment
    start_tiles = [[1,2,3],[4,5,6],[7,8,0]]
    solve_astar(start_tiles, misplaced_tiles)
