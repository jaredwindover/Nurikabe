from random import shuffle
from copy import deepcopy

import nurikabe

cols = 10
rows = 10

max_island_size = 10

def gen():
    board = nurikabe.Board(rows, cols)
    cells = list(board.cell_iterator())
    shuffle(cells)
    return doit(board, 0, cells, max_island_size)

def doit(board, i_start, cells, max_island_size):
    for i in range(i_start, len(cells)):
        new_board = run(board, i, cells, max_island_size)
        if new_board:
            return new_board
    return False


def run(board, idx, cells, max_island_size):
    test_board = deepcopy(board)
    cell = cells[idx]
    groups = []
    print('*********************')
    print(test_board)
    if not test_board.get_cell(cell):
        return doit(board, idx + 1, cells, max_island_size)
    test_board.set_cell(cell, 0)
    print('---------------------')
    print(test_board)
    print('---------------------')
    for c in nurikabe.neighbours(cell):
        if (
                test_board.has_cell(c) and
                test_board.get_cell(c) and
                not any([c in group for group in groups])
        ):
            groups.append(test_board.get_connected_component(c))

    early_exit = False

    if len(groups) > 1:
        groups.sort(key=len)
        ignore = set(cells[:idx])
        for group in groups[:-1]:
            if early_exit:
                break
            for d_c in group:
                if d_c in ignore:
                    early_exit = True
                    break
                test_board.set_cell(d_c, 0)

    if early_exit or max(test_board.island_sizes()) > max_island_size:
        return doit(board, idx + 1, cells, max_island_size)

    print(test_board)

    if test_board.is_valid():
        return test_board

    if idx + 1 >= len(cells):
        return False

    return run(test_board, idx + 1, cells, max_island_size)

board = gen()
print(board)


# def thing(board, cells, idx, rows, cols, max_island_size):
#     cell = cells[idx]
#     groups = []
#     undo_list = []
#     board.set_cell(cell, 0)
#
#     def fail():
#         for c in undo_list:
#             board.set_cell(c, 1)
#         return False
#
#     for c in nurikabe.neighbours(cell):
#         if (
#                 board.has_cell(c) and
#                 board.get_cell(c) and
#                 not any([c in group for group in groups])
#         ):
#             groups.append(
#                 board.get_connected_component(c)
#             )
#     if len(groups) > 1:
#         groups.sort(key=len)
#         for group in groups[:-1]:
#             for d_c in group:
#                 if d_c in cells[:idx]:
#                     fail()
#                 board.set_cell(d_c, 0)
#                 undo_list.append(d_c)
#
#     if max(board.island_sizes()) > max_island_size:
#         fail()
#     else:
#         if board.is_valid():
#             return board
#         else:
#             some_thing = thing(
#                 board,
#                 cells,
#                 leave,
#                 rows,
#                 cols,
#                 max_island_size)
#             if some_thing is False:
#                 fail()
#
# board = thing(board, cells, 0, rows, cols, 5)

# while not nurikabe.test(board):
#     cell = cells.pop()
#     x = cell[0]
#     y = cell[1]
#     board[x][y] = 0
#     if nurikabe.is_disconnected(board):
#         board[x][y] = 1
