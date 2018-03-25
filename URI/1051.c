#include<stdio.h>
#include<stdlib.h>

int main(){
	double n,val,val1,val2=0,var,val3,val4=0,val5;
	int m;
	scanf("%lf",&n);
	m=n;
	if(m<=2000){
		printf("Isento");
	}else{
		if(m>=3000){
			val=(m-2000)-(m%3000);
			if(m<=4500){
				val2=m%3000;
			}else{
				val2=(m-3000)-(m%4500);
				val4=m-4500;
			}
		}else{
			val=m-2000;
		}
		val1=val*0.08;
		val3=val2*0.18;
		val5=val4*0.28;
		var=val1+val3+val5;
		printf("R$ %.2lf\n",var+0.000001);
	}
	return 0;
}
