##############################################A* main function#########################################
import matplotlib.pyplot as plt
from copy import deepcopy
import astar
    
world_grid = [[0, 0, 0, 0, 0, 0],
             [0, 1, 1, 1, 1, 0],
             [0, 1, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0],
             [0, 1, 0, 0, 1, 0]]    


test_start = [0, 0]  # [x, y] 0,0 initial example
test_goal = [5, 7]   # [x, y] 5,7 initial example



# Create an instance of the PathPlanner class:
test_planner = astar.PathPlanner(world_grid, True)

# Plan a path. Choose 4 or 8 connected
type_connection=4
test_planner.a_star(test_start, test_goal,type_connection)
