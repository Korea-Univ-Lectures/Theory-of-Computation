#include <regex>
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
	std::smatch m;
	int errorcode;
	int rc;
	int num;
	char strTemp[255];
	std::string strTemp1;

	FILE *fp = NULL;
	if (fopen_s(&fp, argv[1], "r") != 0)
	{
		printf("no file found\n");
		return 0;
	}

	fscanf_s(fp, "%d", &num);
	fgetc(fp);

	std::regex re("[1]\\d{1}\\syears\\sold"); // write regular expression here
	while (num--)
	{
		fgets(strTemp, sizeof(strTemp), fp);
		strTemp1 = strTemp;

		std::regex_search(strTemp1, m, re); // compare

		for (auto& sm : m)
		{
			printf("%s",sm);
		}

	}

	fclose(fp);
	system("pause");
}