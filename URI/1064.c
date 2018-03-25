#include<stdio.h>
#include<stdlib.h>

int main(){
	int i=0,cont=0;
	double med,n[6],sum=0;
	while(i<6){
		scanf("%lf",&n[i]);
		i++;
	}
	for(i=0;i<6;i++){
		if(n[i]>=0){
			cont++;
			sum=sum+n[i];
		}
	}
	med=sum/cont;
	printf("%d valores positivos\n",cont);
	printf("%.1lf\n",med);
	return 0;
}
