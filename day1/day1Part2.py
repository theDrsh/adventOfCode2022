
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
      elves.append(sum(calories))
      calories = []
    else:
      calories.append(int(food))
  top3 = [0, 0, 0]
  for elf in elves:
    if elf > top3[0]:
      top3[2] = top3[1]
      top3[1] = top3[0]
      top3[0] = elf
      print("top spot taken")
      print(top3)
    elif elf > top3[1]:
      top3[2] = top3[1]
      top3[1] = elf
      print("second spot taken")
      print(top3)
    elif elf > top3[2]:
      top3[2] = elf
      print("final spot taken")
      print(top3)
  return sum(top3)



if __name__ == '__main__':
  main()
