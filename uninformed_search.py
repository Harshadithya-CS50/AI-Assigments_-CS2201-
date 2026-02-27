import time
from collections import deque
import heapq

# ----------------------------
# Problem Definition /Missionairies and Cannibals
# ----------------------------

TOTAL_M = 3
TOTAL_C = 3
BOAT_CAPACITY = 2

INITIAL_STATE = (3, 3, 1)   # (M_left, C_left, boat_side)
GOAL_STATE = (0, 0, 0)


def is_valid(state):
    M_left, C_left, _ = state
    M_right = TOTAL_M - M_left
    C_right = TOTAL_C - C_left

    if M_left < 0 or C_left < 0 or M_left > TOTAL_M or C_left > TOTAL_C:
        return False

    if M_left > 0 and C_left > M_left:
        return False

    if M_right > 0 and C_right > M_right:
        return False

    return True


def get_successors(state):
    M_left, C_left, boat = state
    successors = []

    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]

    for m, c in moves:
        if boat == 1:  # boat on left
            new_state = (M_left - m, C_left - c, 0)
        else:          # boat on right
            new_state = (M_left + m, C_left + c, 1)

        if is_valid(new_state):
            successors.append(new_state)

    return successors


# ----------------------------
# BFS
# ----------------------------

def bfs():
    start_time = time.time()
    queue = deque([(INITIAL_STATE, [])])
    visited = set()
    nodes_expanded = 0

    while queue:
        state, path = queue.popleft()
        nodes_expanded += 1

        if state == GOAL_STATE:
            return path + [state], nodes_expanded, time.time() - start_time

        visited.add(state)

        for succ in get_successors(state):
            if succ not in visited:
                queue.append((succ, path + [state]))

    return None, nodes_expanded, time.time() - start_time


# ----------------------------
# DFS
# ----------------------------

def dfs():
    start_time = time.time()
    stack = [(INITIAL_STATE, [])]
    visited = set()
    nodes_expanded = 0

    while stack:
        state, path = stack.pop()
        nodes_expanded += 1

        if state == GOAL_STATE:
            return path + [state], nodes_expanded, time.time() - start_time

        if state not in visited:
            visited.add(state)

            for succ in reversed(get_successors(state)):
                stack.append((succ, path + [state]))

    return None, nodes_expanded, time.time() - start_time


# ----------------------------
# Uniform Cost Search (UCS)
# ----------------------------

def ucs():
    start_time = time.time()
    pq = [(0, INITIAL_STATE, [])]
    visited = set()
    nodes_expanded = 0

    while pq:
        cost, state, path = heapq.heappop(pq)
        nodes_expanded += 1

        if state == GOAL_STATE:
            return path + [state], nodes_expanded, time.time() - start_time

        if state not in visited:
            visited.add(state)

            for succ in get_successors(state):
                heapq.heappush(pq, (cost + 1, succ, path + [state]))

    return None, nodes_expanded, time.time() - start_time


# ----------------------------
# IDDFS
# ----------------------------

def dls(state, depth, path, visited, nodes_counter):
    nodes_counter[0] += 1

    if state == GOAL_STATE:
        return path + [state]

    if depth == 0:
        return None

    visited.add(state)

    for succ in get_successors(state):
        if succ not in visited:
            result = dls(succ, depth - 1, path + [state], visited, nodes_counter)
            if result:
                return result

    visited.remove(state)
    return None


def iddfs():
    start_time = time.time()
    depth = 0
    nodes_expanded = 0

    while True:
        visited = set()
        nodes_counter = [0]
        result = dls(INITIAL_STATE, depth, [], visited, nodes_counter)
        nodes_expanded += nodes_counter[0]

        if result:
            return result, nodes_expanded, time.time() - start_time

        depth += 1


# ----------------------------
# Performance Comparison
# ----------------------------

def run_algorithm(name, func):
    path, nodes, exec_time = func()
    print(f"\n{name}")
    print("-" * 30)
    print("Solution Depth:", len(path) - 1)
    print("Nodes Expanded:", nodes)
    print("Execution Time:", round(exec_time, 6), "seconds")


if __name__ == "__main__":
    run_algorithm("BFS", bfs)
    run_algorithm("DFS", dfs)
    run_algorithm("UCS", ucs)
    run_algorithm("IDDFS", iddfs)
