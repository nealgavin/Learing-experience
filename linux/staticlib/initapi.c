/*************************************************************************
	> File Name: initapi.c
	> Author: nealgavin
	> Mail: nealgavin@126.com 
	> Created Time: Fri 23 May 2014 07:47:12 PM CST
 ************************************************************************/

#include<stdio.h>
#include<time.h>

void initRand()
{
    time_t seed;
    seed = time(NULL);
    srand( seed );
    return;
}
