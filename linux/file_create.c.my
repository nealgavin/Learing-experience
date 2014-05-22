#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
int main()
{
	int f;
	const char *f_path = "test";
	mode_t f_attrib;		///保存文件属性
	struct stat *buf = malloc(sizeof(stat));
	
	f = creat(f_path,f_attrib);
	if(f == -1)
	{
		puts("file create failed!");
		return 1;
	}
	else
	{
		puts("file create success!");
	}
	printf("file : %d\n",f);
	fstat(f,buf);
	if(buf->st_mode & S_IRUSR)
		puts("file has the right for read!");
	if(buf->st_mode & S_IRGRP)
		puts("group has the right for read!");
	close(f);
	chmod(f_path,0771);
	stat(f_path,buf);
	if(buf->st_mode & S_IWUSR)
		puts("can write for user!");
	if(buf->st_mode & S_IWOTH)
		puts("can write for others");
	else puts("can't write for others");
	free(buf);
	return 0;
}
