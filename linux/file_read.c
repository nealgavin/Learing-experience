#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <stdio.h>
#define LENGTH 2000
int main()
{
	char c[LENGTH];
	int f,i,j = 0;
	f = open("/usr/include/gnu-versions.h",
			O_RDONLY,
			LENGTH);
	if (f != -1)
	{
		i = read(f,c,LENGTH);
		if(i > 0)
		{
			for(;i>0;--i)
				putchar(c[j++]);
		}
		else 
			perror("读取");
	}
	else
		perror("打开文件");
		return 0;
}
