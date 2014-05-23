/*************************************************************************
	> File Name: randapi.c
	> Author: nealgavin
	> Mail: nealgavin@126.com 
	> Created Time: Fri 23 May 2014 07:49:39 PM CST
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>

/*
 * getSRand() return the value between 0.0 and 1.0
 */

float getSRand()
{
    float randvalue;
    randvalue = ((float)rand()/(float)RAND_MAX);
    return randvalue;
}

/*
 *getRand() return a number between 0 and max-1
 */

 int getRand( int max )
 {
     int randvalue;
     randvalue = (int)((float)max*rand()/(RAND_MAX+1.0));
     return randvalue;
 }
