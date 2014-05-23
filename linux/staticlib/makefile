test:test.o randapi.o initapi.o
	gcc -o test test.o randapi.o initapi.o
test.o:test.c
	gcc -c -o test.o test.c
randapi.o: randapi.c randapi.h
	gcc -c -o randapi.o randapi.c
initapi.o:initapi.c
	gcc -c -o initapi.o initapi.c
clean:
	rm *.o test
