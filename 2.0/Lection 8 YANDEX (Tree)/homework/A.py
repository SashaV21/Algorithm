def init_memory(maxn):
    memory = []
    for i in range(maxn):
        memory.append([0, i + 1, 0])
    return [memory, 0]


def new_node(memstruct):
    memory, first_free = memstruct
    memstruct[1] = memory[first_free][1]
    return first_free


def del_node(mem_struct, index):
    memory, first_free = mem_struct
    memory[index][1] = first_free
    mem_struct[1] = index


def find(memstruct, root, x):
    key = memstruct[0][root][0]
    if x == key:
        return root
    elif x < key:
        left = memstruct[0][root][1]
        if left == -1:
            return -1
        else:
            return find(memstruct, left, x)
    elif x > key:
        right = memstruct[0][root][2]
        if right == -1:
            return -1
        else:
            return find(memstruct, right, x)


def createandfillnode(memstruct, key):
    index = new_node(memstruct)
    memstruct[0][index][0] = key
    memstruct[0][index][1] = -1
    memstruct[0][index][2] = -1
    return index


def add(memstruct, root, x):
    key = memstruct[0][root][0]
    if x < key:
        left = memstruct[0][root][1]
        if left == -1:
            memstruct[0][root][1] = createandfillnode(memstruct, x)
        else:
            add(memstruct, left, x)
    elif x > key:
        right = memstruct[0][root][2]
        if right == -1:
            memstruct[0][root][2] = createandfillnode(memstruct, x)
        else:
            add(memstruct, right, x)


def main():
    n = int(input())
    tree = init_memory(n)
    add_val = list(map(int, input().split()))
    for val in add_val:
        add(tree, val)
    