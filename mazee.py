class MazeSolver:
    def __init__(self, maze_file):
        self.maze = self.load_maze(maze_file)
        self.start_position = None
        self.end_position = None
        self.visited = set()

    def load_maze(self, maze_file):
        with open(maze_file, 'r') as file:
            dimensions = file.readline().strip().split(',')
            length = int(dimensions[0])
            width = int(dimensions[1])
            maze = []
            for line in file:
                maze.append(list(line.strip()))
        return maze

    def solve_maze(self):
        self.start_position, self.end_position = self.find_start_end_positions()
        path = self.dfs(self.start_position)
        if path:
            self.print_solution(path)
        else:
            print("No solution found.")

    def find_start_end_positions(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                if self.maze[i][j] == 'S':
                    start_position = (i, j)
                elif self.maze[i][j] == 'G':
                    end_position = (i, j)
        return start_position, end_position

    def dfs(self, position):
        if position == self.end_position:
            return [position]

        self.visited.add(position)

        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        for move in moves:
            new_position = (position[0] + move[0], position[1] + move[1])
            if self.is_valid_move(new_position):
                path = self.dfs(new_position)
                if path:
                    return [position] + path

        return []

    def is_valid_move(self, position):
        i, j = position
        if (
            0 <= i < len(self.maze) and
            0 <= j < len(self.maze[0]) and
            self.maze[i][j] != '%' and
            position not in self.visited
        ):
            return True
        return False

    def print_solution(self, path):
        moves = []
        for i in range(1, len(path)):
            diff = (path[i][0] - path[i-1][0], path[i][1] - path[i-1][1])
            if diff == (0, 1):
                moves.append("right")
            elif diff == (1, 0):
                moves.append("down")
            elif diff == (0, -1):
                moves.append("left")
            elif diff == (-1, 0):
                moves.append("up")
        print("-".join(moves))


# Usage example
maze_solver = MazeSolver('map_maze.txt')
maze_solver.solve_maze()
