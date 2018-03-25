#include<stdio.h>
#include<stdlib.h>

int main(){
	int i=0,cont=0;
	double n[6];
	while(i<6){
		scanf("%lf",&n[i]);
		i++;
	}
	for(i=0;i<6;i++){
		if(n[i]>=0){
			cont++;
		}
	}
	printf("%d valores positivos\n",cont);
	return 0;
}
