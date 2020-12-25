import re
f = open("input.txt", 'r')
line = f.readlines()
p = re.compile("[1]\\d{1}\\syears\\sold")
for i in line:
	m = p.search(i)
	print(m)

f.close();