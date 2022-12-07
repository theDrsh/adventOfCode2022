
def main():
  with open("input.txt") as file:
    input_data = file.read()
    print(solve(input_data))
  return 1

def solve(data) -> int:
  result = 0
  directory_sizes = {}
  file_system = {"directory_path": ["/"]}
  file_system_pointer = file_system
  data = data[0:-1]
  commands = list(filter(lambda x: "$" in x, data.split("\n")))
  buffer = []
  terminal_output = []
  # Group terminal output into list, after for loop grab whatever's left
  for line in data.split("\n"):
    if "$" in line:
      if len(buffer) > 0:
        terminal_output.append(buffer)
        buffer = []
    else:
      buffer.append(line)
  if len(buffer) > 0:
    terminal_output.append(buffer)

  # iterate through commands to build file_system
  terminal_index = 0
  for command in commands:
    parsed_command = command.split("$ ")[-1].split(" ")[0]

    # cd command: move into if exists
    if parsed_command == "cd":
      target_directory = command.split("$ ")[-1].split(" ")[-1]
      if target_directory in file_system_pointer.keys():
        file_system_pointer = file_system_pointer[target_directory]
      elif target_directory == "..":
        yellow_brick_road = file_system_pointer["directory_path"][0:-1]
        file_system_pointer = file_system
        for breadcrumb in yellow_brick_road[1:]:
          file_system_pointer = file_system_pointer[breadcrumb]
      elif target_directory == "/":
        file_system_pointer = file_system
      else:
        print("file:{} not found in {}".format(target_directory, file_system_pointer))

    # ls command
    elif parsed_command == "ls":
      for item in terminal_output[terminal_index]:
        file_name = item.split(" ")[-1]
        file_size  =  item.split(" ")[0]
        if "dir" in item:
          directory_name = item.split(" ")[-1]
          directory_path = file_system_pointer["directory_path"]+ [directory_name]
          file_system_pointer[directory_name] = {"directory_path": directory_path}
        else:
          file_system_pointer[file_name] = file_size
      terminal_index += 1
  sizes = []
  get_sizes(file_system, sizes)
  sizes = list(filter(lambda x: x < 100000, sizes))
  return sum(sizes)

def calculate_directory_size(directory):
  file_sizes = 0
  for key in directory.keys():
    if isinstance(directory[key], str):
      file_sizes += int(directory[key])
    elif isinstance(directory[key], dict):
      file_sizes += calculate_directory_size(directory[key])
  return file_sizes

def get_sizes(directory, sizes):
  for subdirectory in directory:
    if isinstance(directory[subdirectory], dict):
      sizes.append(calculate_directory_size(directory[subdirectory]))
      get_sizes(directory[subdirectory], sizes)
  # something's wrong here, just dedup because I've spent too long trying to figure this out
  sizes = list(dict.fromkeys(sizes))

if __name__ == '__main__':
  main()
