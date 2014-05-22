#include <stdio.h>
//#include <fcnlt.h>

int main(int argc,int ** grgv)
{
	int p;
	p = fork();
	if(p>0)
	{
		printf("father %d\n",p);
	}
	else if(p == 0)
	{
		printf("fa :%d son:%d\n",getppid(),getpid());
	}
	return 0;
}
