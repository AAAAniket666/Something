import heapq
from copy import deepcopy

def print_board(state):
    for i in range(3):
        for j in range(3):
            if state[i*3 + j] == -1:
                print("_", end=" ")
            else:
                print(state[i*3 + j], end=" ")
        print()
    print()

def get_manhattan_distance(start, goal):
    distance = 0
    for i in range(9):
        if start[i] != -1 and start[i] != goal[i]:
            goal_pos = goal.index(start[i])
            x1, y1 = i // 3, i % 3
            x2, y2 = goal_pos // 3, goal_pos % 3
            distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

def get_possible_moves(state):
    empty_pos = state.index(-1)
    row, col = empty_pos // 3, empty_pos % 3
    possible_states = []
    
    if col > 0:
        new_state = state.copy()
        new_state[empty_pos], new_state[empty_pos - 1] = new_state[empty_pos - 1], new_state[empty_pos]
        possible_states.append(new_state)
    
    if col < 2:
        new_state = state.copy()
        new_state[empty_pos], new_state[empty_pos + 1] = new_state[empty_pos + 1], new_state[empty_pos]
        possible_states.append(new_state)
    
    if row > 0:
        new_state = state.copy()
        new_state[empty_pos], new_state[empty_pos - 3] = new_state[empty_pos - 3], new_state[empty_pos]
        possible_states.append(new_state)
    
    if row < 2:
        new_state = state.copy()
        new_state[empty_pos], new_state[empty_pos + 3] = new_state[empty_pos + 3], new_state[empty_pos]
        possible_states.append(new_state)
    
    return possible_states

def a_star_solve(start, goal):
    start_tuple = tuple(start)
    goal_tuple = tuple(goal)
    
    open_set = [(get_manhattan_distance(start, goal), 0, start_tuple, [])]
    heapq.heapify(open_set)
    
    closed_set = set()
    
    states_explored = 0
    
    while open_set:
        f_score, move_count, current_state, path = heapq.heappop(open_set)
        states_explored += 1
        
        current_state_list = list(current_state)
        
        if current_state == goal_tuple:
            print(f"Solved in {move_count} moves!")
            print(f"States explored: {states_explored}")
            for i, state in enumerate(path + [current_state_list]):
                print(f"Move {i}:")
                print_board(state)
            return True
        
        if current_state in closed_set:
            continue
        
        closed_set.add(current_state)
        
        next_states = get_possible_moves(current_state_list)
        
        for next_state in next_states:
            next_state_tuple = tuple(next_state)
            
            if next_state_tuple in closed_set:
                continue
            
            g_score = move_count + 1
            h_score = get_manhattan_distance(next_state, goal)
            f_score = g_score + h_score
            
            new_path = path + [current_state_list]
            heapq.heappush(open_set, (f_score, g_score, next_state_tuple, new_path))
    
    print("No solution found!")
    return False

def main():
    start = []
    goal = []
    
    print("Enter the start state (Enter -1 for empty):")
    for i in range(9):
        start.append(int(input()))
    
    print("Enter the goal state (Enter -1 for empty):")
    for i in range(9):
        goal.append(int(input()))
    
    print("\nStart state:")
    print_board(start)
    print("Goal state:")
    print_board(goal)
    
    a_star_solve(start, goal)

if __name__ == '__main__':
    main()