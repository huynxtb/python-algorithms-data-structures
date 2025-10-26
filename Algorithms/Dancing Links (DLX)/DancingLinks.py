class DLXNode:
    def __init__(self):
        self.left = self.right = self.up = self.down = self
        self.column = None
        self.row_id = None

class DLXColumn(DLXNode):
    def __init__(self, name):
        super().__init__()
        self.size = 0
        self.name = name

class DancingLinks:
    def __init__(self, matrix):
        """
        Initialize the DancingLinks structure for an exact cover problem.

        :param matrix: List of List of int (binary matrix)
        """
        if not matrix or not matrix[0]:
            raise ValueError("Input matrix must be non-empty")

        self.num_rows = len(matrix)
        self.num_cols = len(matrix[0])

        # Create column headers
        self.root = DLXColumn("root")
        self.columns = []

        prev = self.root
        for i in range(self.num_cols):
            col = DLXColumn(i)
            self.columns.append(col)
            # link horizontally
            col.left = prev
            col.right = prev.right
            prev.right.left = col
            prev.right = col
            prev = col

        # Create nodes for matrix
        # For each row, link ones in circular doubly linked list (horizontal)
        self.nodes = []  # keep reference to row nodes for solutions
        for r in range(self.num_rows):
            row_nodes = []
            first_node = None
            last_node = None
            for c in range(self.num_cols):
                if matrix[r][c]:
                    col = self.columns[c]
                    node = DLXNode()
                    node.column = col
                    node.row_id = r
                    # link vertically
                    node.down = col
                    node.up = col.up
                    col.up.down = node
                    col.up = node
                    col.size += 1
                    # link horizontally for this row
                    if first_node is None:
                        first_node = node
                    else:
                        node.left = last_node
                        node.right = last_node.right
                        last_node.right.left = node
                        last_node.right = node
                    last_node = node
                    row_nodes.append(node)
            # close the row circular linked list
            if first_node is not None:
                first_node.left = last_node
                last_node.right = first_node
            self.nodes.append(row_nodes)

        # Initially no solution
        self.solutions = []

    def cover(self, col):
        col.right.left = col.left
        col.left.right = col.right
        i = col.down
        while i != col:
            j = i.right
            while j != i:
                j.down.up = j.up
                j.up.down = j.down
                j.column.size -= 1
                j = j.right
            i = i.down

    def uncover(self, col):
        i = col.up
        while i != col:
            j = i.left
            while j != i:
                j.column.size += 1
                j.down.up = j
                j.up.down = j
                j = j.left
            i = i.up
        col.right.left = col
        col.left.right = col

    def search(self, k=0, solution=None, find_all=False):
        if solution is None:
            solution = []

        if self.root.right == self.root:
            # Found a solution
            self.solutions.append(solution.copy())
            return not find_all  # stop if find_all is False

        # Choose column with minimum size (heuristic)
        c = self.root.right
        min_size = c.size
        col = c
        while c != self.root:
            if c.size < min_size:
                min_size = c.size
                col = c
            c = c.right

        if col.size == 0:
            # No solution possible
            return False

        self.cover(col)
        r = col.down
        while r != col:
            solution.append(r.row_id)
            j = r.right
            while j != r:
                self.cover(j.column)
                j = j.right

            if self.search(k+1, solution, find_all):
                if not find_all:
                    self.uncover(col)
                    return True

            # Backtrack
            solution.pop()
            j = r.left
            while j != r:
                self.uncover(j.column)
                j = j.left
            r = r.down
        self.uncover(col)
        return False

    def solve(self, find_all=False):
        """
        Find exact covers.

        :param find_all: bool - If True, find all solutions, else find one
        :return: List of solutions, where each solution is a list of row indices forming an exact cover
        """
        self.solutions = []
        self.search(find_all=find_all)
        return self.solutions
