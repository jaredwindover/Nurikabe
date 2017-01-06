def pretty_print(board, block_symbol, space_symbol):
    return [''.join([block_symbol if c else space_symbol for c in line]) for line in board]

def parse(str_board, block_symbol, space_symbol):
    return [
        [0 if c == space_symbol else 1
         for c in [line[i:i+len(space_symbol)] for i in range(0, len(line), 2)]]
        for line in str_board]

def island_sizes(board):
    cols = len(board)
    rows = len(board[0])
    visited = set()
    results = {}
    for x in range(cols):
        for y in range(rows):
            if ((x,y) not in visited and
                not board[x][y]):
                ccomp = get_connected_component(board, (x,y))
                for c in ccomp:
                    visited.add(c)
                size = len(ccomp)
                if size in results:
                    results[size] += 1
                else:
                    results[size] = 1
    return results


def get_connected_component(board, cell):
    cols = len(board)
    rows = len(board[0])
    envelope = {cell}
    visited = set()
    i_x = cell[0]
    i_y = cell[1]
    state = board[i_x][i_y]
    while len(envelope) > 0:
        next_cell = envelope.pop()
        visited.add(next_cell)
        x = next_cell[0]
        y = next_cell[1]
        for new_x, new_y in [
                (x, y + 1),
                (x, y - 1),
                (x + 1, y),
                (x - 1, y)
        ]:
            if ((new_x, new_y) not in visited and
                0 <= new_y < rows and
                0 <= new_x < cols and
                board[new_x][new_y] == state):
                envelope.add((new_x, new_y))
    return visited


def is_disconnected(board):
    cols = len(board)
    rows = len(board[0])
    count = sum(map(sum, board))
    try:
        first_x = [i for i, c in enumerate(board) if 1 in c][0]
        first_y = [i for i, v in enumerate(board[first_x]) if v == 1][0]
    except IndexError:
        return False
    return len(get_connected_component(board,(first_x,first_y))) != count


def test(board):
    cols = len(board)
    rows = len(board[0])
    first = None
    for x in range(cols - 1):
        for y in range(rows - 1):
            if (board[x][y] and
                board[x][y + 1] and
                board[x + 1][y] and
                board[x + 1][y + 1]):
                return False

    return not is_disconnected(board)
