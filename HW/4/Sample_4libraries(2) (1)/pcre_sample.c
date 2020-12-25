#define PCRE2_CODE_UNIT_WIDTH 8

#include "pcre2.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
	if (argc < 2)
	{
		printf("usage: [%s] [input path]\n", argv[0]);
		return 0;
	}
	pcre2_code *re = NULL;
	pcre2_match_data *match_data = NULL;
	PCRE2_SIZE erroffset, *ovector;
	int errorcode;
	int rc;
	int num;
	char strTemp[255];

	FILE *fp = NULL;
	if (fopen_s(&fp, argv[1], "r") != 0)
	{
		printf("no file found\n");
		return 0;
	}

	fscanf_s(fp, "%d", &num);
	fgetc(fp);

	PCRE2_SPTR pattern = (PCRE2_SPTR)"[1]\\d{1}\\syears\\sold"; // write regular expression here
	while (num--)
	{
		fgets(strTemp, sizeof(strTemp), fp);
		PCRE2_SPTR input = (PCRE2_SPTR)strTemp;

		re = pcre2_compile(pattern, -1, 0, &errorcode, &erroffset, NULL);

		if (re == NULL)
		{
			PCRE2_UCHAR8 buffer[120];
			(void)pcre2_get_error_message(errorcode, buffer, 120);
			/* Handle error */
			return 0;
		}

		match_data = pcre2_match_data_create(20, NULL);
		rc = pcre2_match(re, input, -1, 0, 0, match_data, NULL);

		if (rc <= 0)
			printf("No match\n");
		else
		{
			ovector = pcre2_get_ovector_pointer_8(match_data);
			printf("Match succeeded at offset %d\n", (int)ovector[0]);
			int index = (int)ovector[0];
			int n = 0;
		}
	}

	fclose(fp);

	pcre2_match_data_free(match_data);
	pcre2_code_free(re);
}