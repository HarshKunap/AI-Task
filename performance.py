# performance.py

import time
from bfs import bfs
from dfs import dfs

start_state = (3, 3, 1)
goal_state = (0, 0, 0)

print("===== BFS =====")
start_time = time.time()
path_bfs, nodes_bfs = bfs(start_state, goal_state)
end_time = time.time()

print("Solution Path:", path_bfs)
print("Nodes Expanded:", nodes_bfs)
print("Time Taken:", end_time - start_time)

print("\n===== DFS =====")
start_time = time.time()
path_dfs, nodes_dfs = dfs(start_state, goal_state)
end_time = time.time()

print("Solution Path:", path_dfs)
print("Nodes Expanded:", nodes_dfs)
print("Time Taken:", end_time - start_time)