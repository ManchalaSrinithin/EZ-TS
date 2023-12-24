// check the ith bit is set or not
//(set means ith bit from right is 1 or not)
/*
1011 ------ 11
0100 ------ 1<<2
0 ---------0

1011 ---------11
0010 --------1<<1
2 ---------2

1111 ---------15
1000 --------1<<3
8 ------------8
*/


main()
{
	int a=15,i=4;
	if(a&(1<<(i-1)))
	{
		printf("yes");
	}
	else
	{
		printf("no");
	}
}
