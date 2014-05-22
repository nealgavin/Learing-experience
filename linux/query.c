#include <stdio.h>
#include <string.h>

int main()
{
	FILE *fd;
	char line[512],login[64];
	fd = fopen("list.txt","r");
	if(fd == NULL)
	{
		perror("----error--open");
		exit(1);
	}
	while(fgets(line,sizeof(line),fd))
	{
		if(line[0] == '#')
			printf("%s",line);
		else
		{
			if(sscanf(line,"%s",login)>0)
			{
				if(strcmp(login,getlogin()) == 0)
					printf("%s",line);
			}
		}
	}
	return 0;
}

