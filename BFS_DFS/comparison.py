import pandas
from BFS_DFS.BFS  import breadth_first_search
from BFS_DFS.DFS  import depth_first_search
import State
path,moves,path_length,depth,nodes,running_time = breadth_first_search(State([[1,2,3],[4,5,6],[7,8,0]]))
path,moves,path_length,depth,nodes,running_time = depth_first_search(State([[1,2,3],[4,5,6],[7,8,0]]))

