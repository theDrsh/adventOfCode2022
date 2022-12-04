
def main():
  with open("input.txt") as file:
    input_data = file.read()
    print(solve(input_data))
  return 1

def solve(data):
  data = data.split("\n")
  elves = [0]
  calories = []
  for food in data:
    if food == "":
      print(calories)
      elves.append(sum(calories))
      calories = []
    else:
      calories.append(int(food))
  return max(elves)


if __name__ == '__main__':
  main()
