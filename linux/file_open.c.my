#include <fcntl.h> //open()
#include <sys/types.h>//mode_t
#include <sys/stat.h>//open()
#include <unistd.h>//close
#include <stdio.h>
int main()
{
	int f;
	const char *f_path = "test4";
	mode_t f_attrib;
	f_attrib = S_IRUSR | S_IWUSR | S_IRGRP | S_IWGRP | S_IROTH;
	f = open(f_path,O_RDONLY);
	if (f == -1)
	{
		f = open(f_path,O_RDWR | O_CREAT ,f_attrib);
		if(f != -1)
			puts("创建一个新文件");
		else 
			{
				puts("无法创建");
				return 1;
			}
	}
	else puts("文件打开成功！");
	close(f);
	return 0;
}
