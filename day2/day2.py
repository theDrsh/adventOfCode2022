
def main():
  with open("input.txt") as file:
    input_data = file.read()
    print(solve(input_data))
  return 1

oppo = {"A": 1, "B": 2, "C": 3}
you = {"X": 1, "Y": 2, "Z": 3}
beats = {"X": "W", "Y": "L", "Z": "D"}
draw = {"X": "A", "Y": "B", "Z": "C"}
oppo_translated = {"A": "rock", "B": "paper", "C": "scissors"}
you_translated = {"X": "rock", "Y": "paper", "Z": "scissors"}
def solve(data):
  result = 0
  data = data.split("\n")
  data = data[0:-1]
  for round in data:
    moves = round.split(" ")
    oppo_move = moves[0]
    your_move = moves[1]
    if oppo_move == draw[your_move]:
      outcome = 3
    elif oppo_move == beats[your_move]:
      outcome = 6
    else:
      outcome = 0
    round_total = you[your_move] + outcome
    print("oppo:{} you:{} won:{} total:{}".format(oppo_translated[oppo_move], you_translated[your_move], outcome, round_total))
    result += round_total
  return result


if __name__ == '__main__':
  main()
