#include<stdio.h>
#include<stdlib.h>
#define PI 3.14159

int main(){
	double val,volume;
	scanf("%lf",&val);
	volume=(4.0/3.0)*PI*val*val*val;
	printf("VOLUME = %.3lf\n",volume);
	return 0;
}
