/*************************************************************************
	> File Name: test.c
	> Author: nealgavin
	> Mail: nealgavin@126.com 
	> Created Time: Fri 23 May 2014 07:55:50 PM CST
 ************************************************************************/

#include<stdio.h>
#include "randapi.h"

#define ITERATIONS 1000000L

int main()
{
    long i;
    long isum;
    float fsum;

    isum = 0L;

    for (i = 0; i<ITERATIONS; ++i)
    {
        isum += getRand(10);
    }

    printf( "getRand() Average %d\n",(int)(isum)/ITERATIONS );

    fsum = 0.0;
    for (i=0;i<ITERATIONS;++i)
    {
        fsum += getSRand();
    }

    printf( "getSRand average %f\n",(fsum/(float)ITERATIONS) );
    return 0;
}
