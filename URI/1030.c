#include<stdio.h>
#include<stdlib.h>

void deleta(int *vect,int c,int inicio){
	
}

int main(){
	int n,m,k,i,j,p=0,vec[10000];
	scanf("%d%*c",&n);
	for(i=0;i<n;i++){
		scanf("%d%d%*c",&m,&k);
		for(j=0;j<m;j++){
			vec[j]=j+1;
		}
		deleta(vec,k,0);
		printf("Case %d: %d\n",i+1,vec[0]);
	}
	
	return 0;
}
