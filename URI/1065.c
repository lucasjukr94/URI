#include<stdio.h>
#include<stdlib.h>

int main(){
	int n[5],i=0,cont=0;
	while(i<5){
		scanf("%d",&n[i]);
		i++;
	}
	for(i=0;i<5;i++){
		if(n[i]%2==0){
			cont++;
		}
	}
	printf("%d valores pares\n",cont);
	return 0;
}
