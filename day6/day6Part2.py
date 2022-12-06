
def main():
  with open("input.txt") as file:
    input_data = file.read()
    print(solve(input_data))
  return 1

def solve(data) -> int:
  data = data[0:-1]
  print(data)
  index = 0
  while len("".join(set(data[index:index+14]))) < 14:
    index +=1
  return index + 14

if __name__ == '__main__':
  main()
