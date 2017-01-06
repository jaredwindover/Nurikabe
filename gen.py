from random import shuffle

import nurikabe

width = 20
height = 20

max_island_size = 5

board = [[1 for x in range(height)] for y in range(width)]

cells = [(x,y) for x in range(width) for y in range(height)]

shuffle(cells)

def pretty_print(board):
    for line in nurikabe.pretty_print(board, '██', '  '):
        print(line)
    print()


class NotGonnaWorkException(Exception):
    pass

def thing(board, cells, leave, rows, cols, max_island_size):
    cell = cells.pop()
    x = cell[0]
    y = cell[1]
    undo_list = [(x,y)]
    groups = []
    board[x][y] = 0

    def fail():
        for c in undo_list:
            u_x = c[0]
            u_y = c[1]
            board[u_x][u_y] = 1
        cells.push(cell)
        raise NotGonnaWorkException

    for new_x, new_y in [
            (x, y + 1),
            (x, y - 1),
            (x + 1, y),
            (x - 1, y)
    ]:
        if  (0 <= new_y < rows and
             0 <= new_x < cols and
             board[new_x][new_y] and
            not any([(new_x, new_y) in group for group in groups])):
            groups.append(nurikabe.get_connected_component(board, (new_x, new_y)))
    if len(groups) > 1:
        groups.sort(key=len)
        for group in groups[:-1]:
            for cell in group:
                d_x = cell[0]
                d_y = cell[1]
                if (d_x, d_y) in leave:
                    fail()
                board[d_x][d_y] = 0
                undo_list.append((d_x,d_y))

    if max(nurikabe.island_sizes(board)) > max_island_size:
        fail()
    else:
        if nurikabe.test(board):
            return board
        else:
            try:
                return thing(
                    board,
                    cells,
                    leave,
                    rows,
                    cols,
                    max_island_size)
            except NotGonnaWorkException:
              fail()

board = thing(board, cells, set(), height, width, 5)

#while not nurikabe.test(board):
#    cell = cells.pop()
#    x = cell[0]
#    y = cell[1]
#    board[x][y] = 0
#    if nurikabe.is_disconnected(board):
#        board[x][y] = 1

pretty_print(board)
