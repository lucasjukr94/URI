#include<stdio.h>
#include<stdlib.h>

int main(){
	double n,reaj;
	int inc=15;
	scanf("%lf",&n);
	if(n>400 && n<=800){
		inc=12;
	}else{
		if(n>800 && n<=1200){
			inc=10;
		}else{
			if(n>1200 && n<=2000){
				inc=7;
			}else{
				if(n>2000){
					inc=4;
				}
			}
		}
	}
	reaj=(n*(inc/100.0))+n;
	printf("Novo salario: %.2lf\n",reaj);
	printf("Reajuste ganho: %.2lf\n",reaj-n);
	printf("Em percentual: %d %%\n",inc);
	return 0;
}
