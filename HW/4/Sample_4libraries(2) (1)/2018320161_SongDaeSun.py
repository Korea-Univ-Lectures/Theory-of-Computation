import re

def getCheckSum (number):
	mask = "234567 - 892345"
	mulSum=0;
	for i in range(0,15):
		if i==6:
			continue
		elif i==7:
			continue
		elif i==8:
			continue
		mulSum+=int(number[i])*int(mask[i])

	remainer = mulSum%11
	checkSum = 11 - remainer

	if(checkSum>=10):
		return checkSum%10
	else:
		return checkSum


f = open("input.txt", 'r')
line = f.read().splitlines()

problem1 = int(re.findall('\d+',line[0])[0])
problem2 = int(re.findall('\d+',line[problem1+1])[0])
problem3 = int(re.findall('\d+',line[problem1+problem2+2])[0])

p1_validation = re.compile("^\d{10}$")
p1 = re.compile("20[0-1]\d320\d{3}|19[1-9]\d320\d{3}|190[5-9]320\d{3}")

for i in range(1,problem1+1):
	m1_validation = p1_validation.search(line[i])
	m1=p1.search(line[i])

	if isinstance(m1_validation, re.Match):
		if isinstance(m1, re.Match):
			print("Y")
		else:
			print("N")
	else:
		print("N")

p2_Non_validation = re.compile("[g-zG-Z_]+|\W+")
p2ARP = re.compile("^[f]{12}\w{12}0806")
p2ipv4 = re.compile("^\w{24}0800")

for i in range(problem1+2,problem1+problem2+2):
	m2_validation = p2_Non_validation.search(line[i])
	m2ARP = p2ARP.search(line[i])
	m2ipv4 = p2ipv4.search(line[i])

	if isinstance(m2_validation, re.Match):
		print("N")
	else:
		if isinstance(m2ARP, re.Match):
			print(line[i][12:24])
		elif isinstance(m2ipv4, re.Match):
			print(line[i][0:12])
		else:
			print("N")

p3_format_Validation = re.compile("^\d{6} - \d{7}$")

p3_gender_Validation = re.compile("[2-9][0-9]\d{4} - [1-2]\d{6}|1[8-9]\d{4} - [1-2]\d{6}|0[0-9]\d{4} - [3-4]\d{6}|1[0-7]\d{4} - [3-4]\d{6}")

p3_31months_Validation = re.compile("\d{2}0[1,3,5,7,8][0-2][0-9] - \d{7}|\d{2}0[1,3,5,7,8]3[0-1] - \d{7}|\d{2}1[0,2][0-2][0-9] - \d{7}}|\d{2}1[0,2]3[0-1] - \d{7}")
p3_30months_Validation = re.compile("\d{2}0[4,6,9][0-2][0-9] - \d{7}|\d{2}0[4,6,9]30 - \d{7}|\d{2}11[0-2][0-9] - \d{7}}|\d{2}1130 - \d{7}")
p3_Febmonth_Validation = re.compile("\d{2}02[0-1][0-9] - \d{7}|\d{2}022[0-8] - \d{7}")
p3_leapyear_Validation = re.compile("[0,2,4,6,8][0,4,8]0229 - \d{7}|[1,3,5,7,9][2,6]0229 - \d{7}")

for i in range(problem1+problem2+3,problem1+problem2+problem3+3):
	m3_format_validation = p3_format_Validation.search(line[i])
	if isinstance(m3_format_validation, re.Match):

		m3_gender_validation = p3_gender_Validation.search(line[i])
		if isinstance(m3_gender_validation, re.Match):

			check = getCheckSum(line[i])

			p3_checksum_validation = re.compile("\d{6} - \d{6}"+str(check))
			m3_checksum_validation = p3_checksum_validation.search(line[i])
			if isinstance(m3_checksum_validation, re.Match):
				m3_31month_validation = p3_31months_Validation.search(line[i])
				m3_30month_validation = p3_30months_Validation.search(line[i])
				m3_Febmonth_validation = p3_Febmonth_Validation.search(line[i])
				m3_leapyear_validation = p3_leapyear_Validation.search(line[i])

				if isinstance(m3_31month_validation, re.Match):
					print("Y")
				elif isinstance(m3_30month_validation, re.Match):
					print("Y")
				elif isinstance(m3_Febmonth_validation, re.Match):
					print("Y")
				elif isinstance(m3_leapyear_validation, re.Match):
					print("Y")
				else:
					print("N")
			else:
				print("N")

		else:
			print("N")
	else:
		print("N")

f.close();

input("엔터를 눌러 종료합니다.")

