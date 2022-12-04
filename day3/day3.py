
def main():
  with open("input.txt") as file:
    input_data = file.read()
    print(solve(input_data))
  return 1

def solve(data):
  result = 0
  data = data.split("\n")
  data = data[0:-1]
  for rucksack in data:
    rucksack = [*rucksack]
    rucksack_size = len(rucksack)
    compartment_size = rucksack_size//2
    compartment1 = rucksack[0:compartment_size]
    compartment2 = rucksack[compartment_size:]
    item_map = {}
    priority = 0
    for item in compartment1:
      if item not in item_map:
        item_map[item] = 1
    for item in compartment2:
      if item in item_map:
        if item.isupper():
          priority = ord(item) - ord('A') + 27
        else:
          priority += ord(item) - ord('a') + 1
        break
    result += priority
  return result


if __name__ == '__main__':
  main()
