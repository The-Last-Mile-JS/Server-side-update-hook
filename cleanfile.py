import sys
import re

filename = sys.argv[1] + ".txt"

answer = list()
r = re.compile("diff --git")
with open(filename, "r") as file:
	answer = file.readlines()

newlist = filter(r.match, answer)
idx = [answer.index(n) for n in newlist]
idx += [len(answer)]

i = 0
ans = []
while i < len(idx)-1:
	ans.append(answer[idx[i]:idx[i+1]])
	i += 1

# overlook empty commit
ans = [entry for entry in ans if len(entry) > 3]

# join all the lines for a js file
to_file = []
for jscommit in ans:
	start_idx = 0
	for i in range(len(jscommit)):
		if jscommit[i].startswith("@@"):
			start_idx = i+1
			break

	jsfile_list = jscommit[start_idx:]
	jsfile_list = [e[1:] for e in jsfile_list]
	to_file.append(''.join(jsfile_list))

i = 0
while i < len(to_file):
	jsfile_name = "{}_check_{}.js".format(filename, i)
	js_file = open(jsfile_name, 'w+')
	print js_file
	js_file.write(to_file[i])
	js_file.close()
	i += 1
