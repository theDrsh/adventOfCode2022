
def main():
  with open("input.txt") as file:
    input_data = file.read()
    print(solve(input_data))
  return 1

def solve(data):
  result = 0
  data = data.split("\n")
  data = data[0:-1]
  num_groups = len(data)//3
  for group in range(num_groups):
    group_start_index = (group * 3)
    group_end_index = group_start_index + 3
    group_rucksacks = data[group_start_index:group_end_index]
    priority = 0
    for item in group_rucksacks[0]:
      if item in group_rucksacks[1] and item in group_rucksacks[2]:
        print(item)
        if item.isupper():
          priority = ord(item) - ord('A') + 27
        else:
          priority = ord(item) - ord('a') + 1
        break
    result += priority





  return result


if __name__ == '__main__':
  main()
