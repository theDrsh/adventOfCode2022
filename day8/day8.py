
def main():
  with open("input.txt") as file:
    input_data = file.read()
    print(solve(input_data))
  return 1

def solve(data) -> int:
  data = data.split('\n')
  data = data[0:-1]
  grid = []
  for tree_row in data:
    grid_row = [*tree_row]
    for index, item in enumerate(grid_row):
      grid_row[index] = int(item)
    grid.append(grid_row)

  width = len(grid[0])
  height = len(grid)

  # outer trees always visible
  visible_trees = (len(grid[0]) * 2) + (len(grid) - 2) * 2
  for y in range(1, height-1):
    for x in range(1, width-1):
      row = grid[y]
      col = []
      # build column
      for test_row in grid:
        col += [test_row[x]]

      east_neighbors = row[:x]
      west_neighbors = row[x+1:]
      north_neighbors = col[:y]
      south_neighbors = col[y+1:]
      east_max = max(east_neighbors)
      west_max = max(west_neighbors)
      north_max = max(north_neighbors)
      south_max = max(south_neighbors)
      tree_height = grid[y][x]
      if tree_height > east_max or tree_height > west_max or tree_height > north_max or tree_height > south_max:
        visible_trees +=1
  return visible_trees

if __name__ == '__main__':
  main()
