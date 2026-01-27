"""def calculate_h(state, goal):
    count=0
    for i in range (len(state)):
        for j in range (len(state[0])):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count+=1
    return count
    
    
def find_blank(state):
    for i in range (len(state)):
        for j in range(len(state[0])):
            if state[i][j] == 0:
                return i,j
                
def copy_state(state):
    new_state=[]
    for row in state:
        new_row=[]
        for val in row:
            new_row.append(val)
        new_state.append(new_row)
    return new_state
    
def child(state,goal,g,parent_index):
    children=[]
    x,y = find_blank(state)
    moves = [(-1,0), (1,0), (0,-1), (0,1)]
    
    for dx,dy in moves:
        nx,ny = x+dx, y+dy
        
        if 0<=nx < len(state) and 0 <= ny < len(state[0]):
            new_state = copy_state(state)
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            
            h= calculate_h(new_state, goal)
            f=g+1+h
            
            children.append({
                "state": new_state,
                "g": g + 1,
                "h": h,
                "f": f,
                "parent": parent_index
            })
            
    return children
    
    
def a_star(start, goal):
    open_list = []
    closed_list = []

    open_list.append({
        "state": start,
        "g": 0,
        "h": calculate_h(start, goal),
        "f": calculate_h(start, goal),
        "parent": -1
    })

    while open_list:
        current = min(open_list, key=lambda x: x["f"])
        open_list.remove(current)
        closed_list.append(current)

        if current["state"] == goal:
            print("Goal reached!")
            return closed_list

        children = child(
            current["state"],
            goal,
            current["g"],
            len(closed_list) - 1
        )

        for c in children:
            if c["state"] not in [x["state"] for x in closed_list]:
                open_list.append(c)

    return None"""
    
    
def calculate_h(state, goal):
    count = 0
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count


def find_blank(state):
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == 0:
                return i, j


def copy_state(state):
    new_state = []
    for row in state:
        new_state.append(row[:])
    return new_state


def child(state, goal, g, parent_index):
    children = []
    x, y = find_blank(state)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if 0 <= nx < len(state) and 0 <= ny < len(state[0]):
            new_state = copy_state(state)
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]

            h = calculate_h(new_state, goal)
            f = g + 1 + h

            children.append({
                "state": new_state,
                "g": g + 1,
                "h": h,
                "f": f,
                "parent": parent_index
            })

    return children


def a_star(start, goal):
    open_list = []
    closed_list = []

    h0 = calculate_h(start, goal)
    open_list.append({
        "state": start,
        "g": 0,
        "h": h0,
        "f": h0,
        "parent": -1
    })

    while open_list:
        current = min(open_list, key=lambda x: x["f"])
        open_list.remove(current)
        closed_list.append(current)

        if current["state"] == goal:
            print("Goal reached!")
            print_path(closed_list, len(closed_list)-1)
            return

        children = child(
            current["state"],
            goal,
            current["g"],
            len(closed_list) - 1
        )

        for c in children:
            if c["state"] not in [x["state"] for x in closed_list]:
                open_list.append(c)

    return None
    
    
def print_path(closed_list, goal_index):
    path = []
    index = goal_index

    while index != -1:
        path.append(closed_list[index]["state"])
        index = closed_list[index]["parent"]

    path.reverse()

    print("\nSolution Path:\n")
    step = 0
    for state in path:
        print(f"Step {step}:")
        for row in state:
            print(row)
        print()
        step += 1



start = [
    [7, 4, 1],
    [0, 3, 2],
    [5, 6, 8]
]

goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

result = a_star(start, goal)

print(result)

 


