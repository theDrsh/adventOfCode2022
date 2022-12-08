
def main():
  with open("input.txt") as file:
    input_data = file.read()
    solution = solve(input_data)
    print(solution)
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

  scenic_grid = []
  for y in range(height):
    row_of_scenic_scores = []
    for x in range(width):
      tree_height = grid[y][x]
      row = grid[y]
      col = []
      # build column
      for test_row in grid:
        col += [test_row[x]]

      east_neighbors = row[:x]
      west_neighbors = row[x+1:]
      north_neighbors = col[:y]
      south_neighbors = col[y+1:]
      east_neighbors.reverse()
      north_neighbors.reverse()
      num_trees_east = 0
      for index in range(len(east_neighbors)):
        num_trees_east += 1
        if east_neighbors[index] >= tree_height:
          break
      num_trees_west = 0
      for index in range(len(west_neighbors)):
        num_trees_west += 1
        if west_neighbors[index] >= tree_height:
          break
      num_trees_north = 0
      for index in range(len(north_neighbors)):
        num_trees_north += 1
        if north_neighbors[index] >= tree_height:
          break
      num_trees_south = 0
      for index in range(len(south_neighbors)):
        num_trees_south += 1
        if south_neighbors[index] >= tree_height:
          break
      scenic_score = num_trees_north * num_trees_west * num_trees_south * num_trees_east
      row_of_scenic_scores.append(scenic_score)
    scenic_grid.append(row_of_scenic_scores)
  max_scenic = 0
  for row in scenic_grid:
    if max_scenic < max(row):
      max_scenic = max(row)
  return max_scenic

if __name__ == '__main__':
  main()
