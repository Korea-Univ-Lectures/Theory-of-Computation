#include <re2/re2.h>
#include <string>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
	if (argc < 2)
	{
		printf("usage: [%s] [input path]\n", argv[0]);
		return 0;
	}
	int num;
	char strTemp[255];
	int strTemp1;
	int strTemp2;
	std::string strTemp3;
	std::string strTemp4;
	std::string strTemp5;
	std::string strTemp6;


	FILE *fp = NULL;
	fp = fopen(argv[1], "r");
	if (fp == NULL)
	{
		printf("no file found\n");
		return 0;
	}

	fscanf(fp, "%d", &num);
	fgetc(fp);
	
	RE2 re("([1])(\\d{1})(\\s)(years)(\\s)(old)"); // write regular expression here
	while (num--)
	{
		fgets(strTemp, sizeof(strTemp), fp);

		if(RE2::PartialMatch(strTemp, re, &strTemp1, &strTemp2, &strTemp3, &strTemp4, &strTemp5, &strTemp6)) // compare
			printf("match : %d%d%s%s%s%s\n",strTemp1,strTemp2,strTemp3.c_str(),strTemp4.c_str(),strTemp5.c_str(),strTemp6.c_str());
	}

	fclose(fp);
}