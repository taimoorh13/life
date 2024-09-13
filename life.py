from bitarray import bitarray

class Life:
    """A Python implementation of Game of Life.

    It is a part of Big Geodata Processing Course in Quartile 1, Year 2.

    Rules:
    - Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    - Any live cell with two or three live neighbours lives on to the next generation.
    - Any live cell with more than three live neighbours dies, as if by overpopulation.
    - Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    """

    def __init__(self, filename: str):
        """Creates a Game of Life object.

        Args:
          filename: Input filename.

        Raises:
          Exception: If input data is invalid.
        """
        self.filename = filename
        self.grid = []
        with open(filename) as f:
            self.w, self.h  = map(int, f.readline().split(maxsplit = 1))
            
            for y in range(self.h + 2):
                self.grid.append([0] * (self.w + 2))
                
            for ind, line in enumerate(f):
                try:
                    y, x = map(int, line.split(maxsplit = 1))
    
                    if y < 0 or x < 0:
                        raise ValueError
                
                except ValueError:
                    raise Exception(f"Invalid cell on line {ind + 2}")        
                
                self.grid[y+1][x+1] = 1      
                
    
    def tick(self, num_generations: int=1):
        """Applies the rules of Game of Life for specified number of generations.

        Args:
          n: Number of generations.
        """
        for i in range(num_generations):
            for y, row in enumerate(self.grid[1:-1]):
                y2 = y+2
                curr = [0] * (self.w + 2)            
                for x, cell in enumerate(row[1:-1]):                
                    count = self.grid[y][x] + self.grid[y][x+1] + self.grid[y][x+2] + row[x] + row[x+2] + self.grid[y2][x] + self.grid[y2][x+1] + self.grid[y2][x+2]
                    curr[x+1] = 1 if count == 3 or (count == 2 and cell) else 0
                if y > 0:
                    self.grid[y] = prev
                prev = curr
            self.grid[y+1] = curr
