#include<stdio.h>
#include<stdlib.h>

int main(){
	int n,i,a[1000],b[1000],min,max,k,j,mdc;
	scanf("%d",&n);
	for(i=0;i<n;i++){
		scanf("%d%d",&a[i],&b[i]);
	}
	for(i=0;i<n;i++){
		min=a[i];
		max=b[i];
		if(min>max){
			k=min;
			min=max;
			max=k;
		}
		for(j=min;j>0;j--){
			if(max%j==0 && min%j==0){
				mdc=j;
				break;
			}
		}
		printf("%d\n",mdc);
	}
	return 0;
}
