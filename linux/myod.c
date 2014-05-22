#include <stdio.h>
#include <errno.h>
#include <fcntl.h>

int main(int argc,char ** argv)
{
	int fd,i,k,j,len;
	unsigned char buf[512];
	
	for(i=1;i<argc;++i)
	{
		fd = open(argv[i],O_RDONLY);
		if(fd == -1)
		{
			fprintf(stderr,"Open file fail \"%s\":%s (ERROR %d)\n",argv[i],strerror(errno),errno);
		}
		while((len = read(fd,buf,sizeof(buf)))>0)
		{
			for(j=0;j<len;++j)
			printf("%02x ",buf[j]);
		}
		if(len<0)
			perror("read data");
		close(fd);
	}
	return 0;
}
