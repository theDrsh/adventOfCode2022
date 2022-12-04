
def main():
  with open("input.txt") as file:
    input_data = file.read()
    print(solve(input_data))
  return 1

oppo = {"A": 1, "B": 2, "C": 3}
you = {"X": 1, "Y": 2, "Z": 3}
loses = {"A": 3, "B": 1, "C": 2}
beats = {"A": 2, "B": 3, "C": 1}
draw =  {"A": 1, "B": 2, "C": 3}
oppo_translated = {"A": "rock", "B": "paper", "C": "scissors"}
you_translated = ["zero_index_lul","rock", "paper", "scissors"]
outcome_translated = {"X": "lose", "Y": "draw", "Z": "win"}
def solve(data):
  result = 0
  data = data.split("\n")
  data = data[0:-1]
  for round in data:
    moves = round.split(" ")
    oppo_move = moves[0]
    outcome = moves[1]
    if outcome == "X":
      your_move = loses[oppo_move]
      round_result = 0
    elif outcome == "Y":
      your_move = draw[oppo_move]
      round_result = 3
    else:
      your_move = beats[oppo_move]
      round_result = 6
    round_total = your_move + round_result
    result += round_total
    print("oppo:{} you:{} outcome:{} result:{} your_move={} outcome={}".format(oppo_translated[oppo_move], you_translated[your_move], outcome_translated[outcome], round_total, your_move, round_result))
  return result


if __name__ == '__main__':
  main()
