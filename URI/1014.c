#include<stdio.h>
#include<stdlib.h>

int main(){
	int a;
	double b,fuel;
	scanf("%d%lf",&a,&b);
	fuel=a/b;
	printf("%.3lf km/l\n",fuel);
	return 0;
}
