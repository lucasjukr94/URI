#include<stdio.h>
#include<stdlib.h>

int main(){
	int n,i=0;
	scanf("%d",&n);
	while(i<6){
		if(n%2==0){
			n=n+1;
			printf("%d\n",n);
		}else{
			n=n+2;
			printf("%d\n",n);
		}
		i++;
	}
	return 0;
}
