import re #re 임포트

def getCheckSum (number): #checkSum을 계산하여 return하는 함수이다.
	mask = "234567 - 892345" #ppt에 나온 마스크는 다음과 같다.
	mulSum=0;
	for i in range(0,15):#숫자 12개만 비교하면 된다.
		if i==6:#공백은 무시합니다
			continue
		elif i==7: #-는 무시합니다
			continue
		elif i==8: #공백은 무시합니다
			continue
		mulSum+=int(number[i])*int(mask[i]) #주민등록번호의 숫자와 마스크의 숫자를 곱하여 더합니다.

	remainer = mulSum%11 #ppt에 제시된 대로 11의 나머지를 구합니다
	checkSum = 11 - remainer #ppt에 제시된 대로 checkSum을 구합니다.

	if(checkSum>=10): #만약이 checkSum이 10이상이면 10의 나머지를 return합니다.
		return checkSum%10
	else:
		return checkSum

f = open("input.txt", 'r') #input을 받아서 line별로 나눕니다.
line = f.read().splitlines()

problem1 = int(re.findall('\d+',line[0])[0]) #problem1의 문제 수를 받습니다.
problem2 = int(re.findall('\d+',line[problem1+1])[0]) #problem2의 문제 수를 받습니다.
problem3 = int(re.findall('\d+',line[problem1+problem2+2])[0]) #problem3의 문제 수를 받습니다.

p1_validation = re.compile("^\d{10}$") #10개의 숫자가 있는지를 판단합니다.

#년도은 1905~2019로 제한합니다.
p1 = re.compile("20[0-1]\d320\d{3}|19[1-9]\d320\d{3}|190[5-9]320\d{3}")

for i in range(1,problem1+1):

	m1_validation = p1_validation.search(line[i])
	if isinstance(m1_validation, re.Match): #만일 주어진 input이 10개의 숫자이면,

		m1 = p1.search(line[i])
		if isinstance(m1, re.Match): #그 숫자가 유효한 컴퓨터학과 학생의 학번인지를 확인합니다
			print("Y")
		else:
			print("N")
	else:
		print("N")

# 주어진 문자열이 0,1,2,3,4,5,6,7,8,9,a(A),b(B),c(C),d(D),e(E),f(F)으로 구성된 HEX인지를 확인한다
p2_Non_validation = re.compile("[g-zG-Z_]+|\W+")

#If first 6bytes are "ff ff ff ff ff ff” and last 2bytes are “08 06”, It is the ARP Broadcast packet.
p2ARP = re.compile("^[f]{12}\w{12}0806")

# If last 2bytes are "08 00”, It is the Ipv4 packet.
p2ipv4 = re.compile("^\w{24}0800")

for i in range(problem1+2,problem1+problem2+2):

	#만일 유효한 HEX의 input이 아니면
	m2_validation = p2_Non_validation.search(line[i])
	if isinstance(m2_validation, re.Match):
		print("N") #N를 출력한다.

	# 만일 유효한 HEX의 input이면,
	else:
		m2ARP = p2ARP.search(line[i])
		m2ipv4 = p2ipv4.search(line[i])

		# 만일 ARP Broadcast Packet이면 source MAC address를 출력한다.
		if isinstance(m2ARP, re.Match):
			print(line[i][12:24])

		# 만일 IPv4 Packet이면 destination MAC address를 출력한다.
		elif isinstance(m2ipv4, re.Match):
			print(line[i][0:12])

		# 만일 둘다 아니면 N을 출력
		else:
			print("N")

# (6-digits) + (single space) + ‘-’ + (single space) + (7-digits)의 형식인지 확인한다.
p3_format_Validation = re.compile("^\d{6} - \d{7}$")

#1920 ~ 1999  20xxxx – 1xxxxxx , 99xxxx – 2xxxxxx, … (starts with 1, 2)
#2000 ~ 2019  00xxxx – 3xxxxxx, 19xxxx – 4xxxxxx, … (starts with 3, 4)
# ppt에 나온 대로 gender validation을 설정한다.
p3_gender_Validation = re.compile("[2-9][0-9]\d{4} - [1-2]\d{6}|[0-1][0-9]\d{4} - [3-4]\d{6}")

# 31일이 말일인 달 1,3,5,7,8을 valid하게 처리합니다.
p3_31months_Validation = re.compile("\d{2}0[1,3,5,7,8][0-2][0-9] - \d{7}|\d{2}0[1,3,5,7,8]3[0-1] - \d{7}|\d{2}1[0,2][0-2][0-9] - \d{7}}|\d{2}1[0,2]3[0-1] - \d{7}")

# 30일이 말일인 달 4, 6, 9, 11을 valid하게 처리합니다.
p3_30months_Validation = re.compile("\d{2}0[4,6,9][0-2][0-9] - \d{7}|\d{2}0[4,6,9]30 - \d{7}|\d{2}11[0-2][0-9] - \d{7}}|\d{2}1130 - \d{7}")

# 일반적으로 28일이 말일인 2월을 vaild하게 처리합니다.
p3_Febmonth_Validation = re.compile("\d{2}02[0-1][0-9] - \d{7}|\d{2}022[0-8] - \d{7}")

# 만일 2월에 29일인 경우, 윤년인지의 여부를 따져서 윤년이면 valid하게 처리합니다.
# 윤년의 기준은 ppt에 제시된 MODIFIED algorithm을 사용합니다. ->if (year is divisible by 4) then (it is a leap year)
# 수학적 법칙에 따라 맨 마지막 두자리가 4의 배수이면, 전체가 4의 배수가 됩니다.
# 수학적 법칙에 따라 십의 자리수가 짝수이면, 일의 자릿수가 0, 4, 8이어야 하고
# 십의 자릿수가 홀수이면 일의 자릿수가 2, 6이어야 합니다.
p3_leapyear_Validation = re.compile("[0,2,4,6,8][0,4,8]0229 - \d{7}|[1,3,5,7,9][2,6]0229 - \d{7}")

for i in range(problem1+problem2+3,problem1+problem2+problem3+3):

	#만일 주어진 input이 valid한 형식의 HEX이면
	m3_format_validation = p3_format_Validation.search(line[i])
	if isinstance(m3_format_validation, re.Match):

		#만일 주어진 gender가 형식에 맞으면,
		m3_gender_validation = p3_gender_Validation.search(line[i])
		if isinstance(m3_gender_validation, re.Match):

			check = getCheckSum(line[i]) #주어진 input의 checkSum을 계산하고
			p3_checksum_validation = re.compile("\d{6} - \d{6}"+str(check))
			m3_checksum_validation = p3_checksum_validation.search(line[i])

			#print(check)

			# 만일 checkSum이 vaild하면
			if isinstance(m3_checksum_validation, re.Match):
				m3_31month_validation = p3_31months_Validation.search(line[i])
				m3_30month_validation = p3_30months_Validation.search(line[i])
				m3_Febmonth_validation = p3_Febmonth_Validation.search(line[i])
				m3_leapyear_validation = p3_leapyear_Validation.search(line[i])

				# 말일이 31일인 달들에 포함되는지를 보고
				if isinstance(m3_31month_validation, re.Match):
					print("Y") # 포함되면 Y를 출력

				# 아니면, 말일이 30일인 달들에 포함되는지를 보고
				elif isinstance(m3_30month_validation, re.Match):
					print("Y") # 포함되면 Y를 출력

				# 아니면, 말일이 28일인 2월달에 포함되는지를 보고
				elif isinstance(m3_Febmonth_validation, re.Match):
					print("Y") # 포함되면 Y를 출력

				# 아니면, 윤년인지의 여부를 보고
				elif isinstance(m3_leapyear_validation, re.Match):
					print("Y") # 윤년이면 Y를 출력

				# 그것조차 아니면 N을 출력
				else:
					print("N")
			else:
				print("N")

		else:
			print("N")
	else:
		print("N")

# 입력을 아무거나 받으면 프로그램 종료
input("엔터키를 눌러 종료합니다.")

f.close();

