import sys
filename = sys.argv[1] + ".txt"

answer = list()

with open(filename, "r") as file:
	answer = file.readlines()

print(answer)