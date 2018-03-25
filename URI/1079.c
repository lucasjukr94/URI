#include<stdio.h>
#include<stdlib.h>

int main(){
	int n,i,j;
	double mat[1000][3];
	scanf("%d",&n);
	for(i=0;i<n;i++){
		scanf("%lf%lf%lf",&mat[i][0],&mat[i][1],&mat[i][2]);
	}
	for(i=0;i<n;i++){
		printf("%.1lf\n",(mat[i][0]*2+mat[i][1]*3+mat[i][2]*5)/10.0);
	}
	return 0;
}
