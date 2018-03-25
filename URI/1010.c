#include<stdio.h>
#include<stdlib.h>

int main(){
	int A,B,D,E;
	double C,F,PRICEA,PRICEB,PRICETOT;
	scanf("%d%d%lf",&A,&B,&C);
	scanf("%d%d%lf",&D,&E,&F);
	PRICEA=B*C;
	PRICEB=E*F;
	PRICETOT=PRICEA+PRICEB;
	printf("VALOR A PAGAR: R$ %.2lf\n",PRICETOT);
	return 0;
}
