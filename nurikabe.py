def test(board):
    cols = len(board)
    rows = len(board[0])
    first = None
    count = sum(map(sum, board))
    try:
        first_x = [i for i, c in enumerate(board) if 1 in c][0]
        first_y = [i for i, v in enumerate(board[first_x]) if v == 1][0]
    except IndexError:
        return True
    for x in range(cols - 1):
        for y in range(rows - 1):
            if (board[x][y] and
                board[x][y + 1] and
                board[x + 1][y] and
                board[x + 1][y + 1]):
                return False

    envelope = {(first_x, first_y)}
    visited = []
    while len(envelope) > 0:
        next_cell = envelope.pop()
        visited.append(next_cell)
        count -= 1
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
                board[new_x][new_y]):
                envelope.add((new_x, new_y))
    return count == 0
