#include<stdio.h>
#include<stdlib.h>

int main(){
	int a,b,c,maior;
	scanf("%d%d%d",&a,&b,&c);
	maior=(a+b+abs(a-b))/2;
	maior=(c+maior+abs(c-maior))/2;
	printf("%d eh o maior\n",maior);
	return 0;
}

int abs(int n){
	if(n<0){
		return n*(-1);
	}
	return n;
}
