
def main():
  with open("input.txt") as file:
    input_data = file.read()
    print(solve(input_data))
  return 1

def solve(data):
  result = 0
  data = data.split("\n")
  data = data[0:-1]
  for pair in data:
    elf1 = pair.split(",")[0]
    elf2 = pair.split(",")[1]
    elf1_set = set()
    elf2_set = set()
    for index in range(int(elf1.split("-")[0]), int(elf1.split("-")[1]) + 1):
      elf1_set.add(index)
    for index in range(int(elf2.split("-")[0]), int(elf2.split("-")[1]) + 1):
      elf2_set.add(index)
    if elf1_set.issuperset(elf2_set):
      result += 1
    if elf2_set.issuperset(elf1_set):
      result +=1
  return result



if __name__ == '__main__':
  main()
