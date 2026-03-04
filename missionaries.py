

# Missionaries and Cannibals Problem

# State representation:
# (M_left, C_left, Boat_position)
# Boat_position = 1 means boat is on left side
# Boat_position = 0 means boat is on right side

INITIAL_STATE = (3, 3, 1)
GOAL_STATE = (0, 0, 0)


def is_valid(state):
    m_left, c_left, boat = state

    m_right = 3 - m_left
    c_right = 3 - c_left

    # Missionaries should not be outnumbered on either side
    if m_left > 0 and c_left > m_left:
        return False
    if m_right > 0 and c_right > m_right:
        return False

    if m_left < 0 or c_left < 0 or m_left > 3 or c_left > 3:
        return False

    return True


def get_successors(state):
    m_left, c_left, boat = state
    successors = []

    # Possible moves (M, C)
    moves = [
        (1, 0),
        (2, 0),
        (0, 1),
        (0, 2),
        (1, 1)
    ]

    for m, c in moves:
        if boat == 1:  # Boat on left side
            new_state = (m_left - m, c_left - c, 0)
        else:  # Boat on right side
            new_state = (m_left + m, c_left + c, 1)

        if is_valid(new_state):
            successors.append(new_state)

    return successors


if __name__ == "__main__":
    print("Initial State:", INITIAL_STATE)
    print("Goal State:", GOAL_STATE)
    print("Successors of Initial State:")
    for s in get_successors(INITIAL_STATE):
        print(s)