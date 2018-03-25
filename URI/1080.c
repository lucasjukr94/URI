#include<stdio.h>
#include<stdlib.h>

int main(){
	int n[100],i,max,pos;
	for(i=0;i<100;i++){
		scanf("%d",&n[i]);
	}
	
	/*
	for(i=0;i<100;i++){
		if(i==53){
			n[i]=421;
		}else{
			n[i]=i;	
		}
		printf("%d ",n[i]);
	}
	printf("\n");
	*/
	
	max=n[0];
	pos=1;
	for(i=0;i<100;i++){
		if(max<n[i+1]){
			max=n[i+1];
			pos=i+2;
		}
	}
	printf("%d\n",max);
	printf("%d\n",pos);
	return 0;
}
