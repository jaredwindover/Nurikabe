def left(cell):
    x = cell[0]
    y = cell[1]
    return (x - 1, y)

def right(cell):
    x = cell[0]
    y = cell[1]
    return (x + 1, y)

def up(cell):
    x = cell[0]
    y = cell[1]
    return (x, y - 1)

def down(cell):
    x = cell[0]
    y = cell[1]
    return (x, y + 1)

def neighbours(cell):
    return [up(cell),
            down(cell),
            right(cell),
            left(cell)]

class Board():
    def from_str(str_board, block_symbol, space_symbol):
        n = len(space_symbol)
        return Board([
            [0 if c == space_symbol else 1
             for c in [line[i:i + n] for i in range(0, len(line), n)]]
            for line in str_board])

    def __init__(self, *argv):
        if len(argv) == 1:
            cells = argv[0]
            self._init_board(cells)
        elif len(argv) == 2:
            rows = argv[0]
            cols = argv[1]
            self._init_rows_cols(rows, cols)

    def __str__(self):
        return '\n'.join(self.pretty_print('██', '  '))

    def _init_board(self, cells):
        self.cells = cells
        self.cols = len(cells)
        self.rows = len(cells[0])

    def _init_rows_cols(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.cells = [[1 for x in range(cols)] for y in range(rows)]

    def has_cell(self, c):
        return (0 <= c[1] < self.rows and
                0 <= c[0] < self.cols)

    def set_cell(self, c, v):
        self.cells[c[0]][c[1]] = v

    def get_cell(self, c):
        return self.cells[c[0]][c[1]]

    def cell_iterator(self):
        for y in range(self.rows):
            for x in range(self.cols):
                yield (x, y)

    def _is_2x2_block(self, cell):
        return (self.get_cell(cell) and
                self.get_cell(down(cell)) and
                self.get_cell(right(cell)) and
                self.get_cell(down(right(cell))))

    def has_2x2_block(self):
        return any([self._is_2x2_block((x, y))
                    for x in range(self.rows - 1)
                    for y in range(self.cols - 1)])

    def pretty_print(self, block_symbol, space_symbol):
        return [''.join([block_symbol if c else space_symbol for c in line])
                for line in self.cells]

    def island_sizes(self):
        visited = set()
        results = {}
        for c in self.cell_iterator():
            if (
                    c not in visited and
                    not self.get_cell(c)):
                ccomp = self.get_connected_component(c)
                for cc in ccomp:
                    visited.add(cc)
                size = len(ccomp)
                if size in results:
                    results[size] += 1
                else:
                    results[size] = 1
        return results

    def get_connected_component(self, cell):
        envelope = {cell}
        visited = set()
        state = self.get_cell(cell)
        while len(envelope) > 0:
            c = envelope.pop()
            visited.add(c)
            for new_c in neighbours(c):
                if (
                        new_c not in visited and
                        self.has_cell(new_c) and
                        self.get_cell(new_c) == state):
                    envelope.add(new_c)
        return visited

    def is_disconnected(self):
        count = sum(map(sum, self.cells))
        try:
            first = [c for c in self.cell_iterator() if self.get_cell(c)][0]
        except IndexError:
            return False
        return len(self.get_connected_component(first)) != count

    def is_valid(self):
        return not self.has_2x2_block() and not self.is_disconnected()
