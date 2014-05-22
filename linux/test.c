#include <stdio.h>
#include <fcntl.h>
int main()
{
	int pid = fork();
	if(pid == 0)
	{
		execlp("/bin/cat","wc","-1","test",0);
	}
	wait(0);
	return 0;
}
