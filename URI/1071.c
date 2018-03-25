#include<stdio.h>
#include<stdlib.h>

int main(){
	int a,b,c,i,sum=0;
	scanf("%d",&a);
	scanf("%d",&b);
	if(a>b){
		c=a;
		a=b;
		b=c;
	}
	for(i=a;i<b;i++){
		if(i%2!=0){
			sum=sum+i;
		}
	}
	printf("%d\n",sum);
	return 0;
}
