#include<stdio.h>
#include<stdlib.h>

int main(){
	double n,vec[20]={100.00,50.00,20.00,10.00,5.00,2.00,1.00,0.50,0.25,0.10,0.05,0.01};
	int i,vec1[20];
	scanf("%lf",&n);
	for(i=0;i<12;i++){
		if(n>=vec[i]){
			vec1[i]=n/vec[i];
		}else{
			vec1[i]=0;
		}
		n=n-(vec1[i]*vec[i]);
	}
	for(i=0;i<12;i++){
		if(i==6){
			printf("MOEDAS:\n");
			printf("%d moeda (s) de R$ %.2lf\n",vec1[i],vec[i]);
		}else{
			if(i==0){
				printf("NOTAS:\n");
				printf("%d nota (s) de R$ %.2lf\n",vec1[i],vec[i]);
			}else{
				if(i<6){
					printf("%d nota (s) de R$ %.2lf\n",vec1[i],vec[i]);
				}else{
					printf("%d moeda (s) de R$ %.2lf\n",vec1[i],vec[i]);
				}
			}
		}
	}
	return 0;
}
