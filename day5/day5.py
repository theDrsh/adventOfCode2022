
def main():
  with open("input.txt") as file:
    input_data = file.read()
    print(solve(input_data))
  return 1

def solve(data) -> str:
  result = ""
  data = data[0:-1]
  # Build list of columns, each element of list is a list of the vertical stacks
  stacks = data.split("\n\n")[0]
  moves = data.split("\n\n")[1]
  rows = stacks.split("\n")[0:-1]
  num_columns = int(stacks.split("\n")[-1].strip()[-1])
  grid = []
  for index, temp_row in enumerate(rows):
    temp_row = temp_row.replace("] [", "")
    temp_row = temp_row.replace(" [", "")
    temp_row = temp_row.replace("]", "")
    temp_row = temp_row.replace("[", "")
    temp_row = temp_row.replace("   ", "X")
    temp_row = list(filter(lambda x: x!=' ', temp_row))
    if len(temp_row) < num_columns:
      temp_row += " " * (num_columns - len(temp_row))
    rows[index] = temp_row
  for i in range(num_columns):
    column = []
    for row_item in rows:
      column.append(row_item[i])
    column = list(filter(lambda x: x!=" ", column))
    column = list(filter(lambda x: x!="X", column))
    grid.append(column)
  print(grid)

  # execute moves
  moves = moves.split("\n")
  print(len(moves))
  for move in moves:
    num_to_move = int(move.split("move ")[-1].split(" ")[0])
    move_from = int(move.split("from ")[-1][0])
    move_to = int(move.split("to ")[-1][0])

    # Pick up items
    on_crane = grid[move_from - 1][0:num_to_move]
    on_crane.reverse()
    del grid[move_from - 1][0:num_to_move]
    # Place items
    grid[move_to -1] = on_crane + grid[move_to -1]
  for column in grid:
    result += column[0]
  return result

if __name__ == '__main__':
  main()
