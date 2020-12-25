import re
f = open("input1.txt", 'r')
line = f.readlines()
p = re.compile("[1]\\d{1}\\syears\\sold")
for i in line:
	m = p.search(i)

	if isinstance(m, re.Match):
		print("Y")
	else:
		print("N")

f.close();
