#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){
	int n,j,i;
	char vec[100][100],var[100][100];
	scanf("%d",&n);
	for(i=0;i<=n;i++){
		//scanf("%s",vec[i]); não funciona se usar espaço ou ponto
		gets(vec[i]);
		//strcat(var[i],vec[i]);
	}
	
	//move 3 pra direita no ASCII
	for(i=0;i<=n;i++){
		for(j=0;vec[i][j]!='\0';j++){
			if((vec[i][j]>='a'&&vec[i][j]<='z')||(vec[i][j]>='A'&&vec[i][j]<='Z'))
			vec[i][j]=vec[i][j]+3;
		}
	}
	
	//move 1 pra esquerda no ASCII
	for(i=0;i<=n;i++){
		for(j=0;j<=strlen(vec[i])/2;j++){
			vec[i][j]=vec[i][j]-1;
		}
	}
	/*
	//reverso
	for(i=0;i<=n;i++){
		for(j=strlen(vec[i]);j>=0;j--){
			var[i][strlen(vec[i])-j]=vec[i][j];
		}
	}
	*/
	for(i=0;i<=n;i++){
		//for(j=0;vec[i][j]!='\0';j++){
		for(j=0;j<strlen(vec[i]);j++){
			printf("%c",vec[i][j]);
		}
		printf("\n");
	}
	return 0;
}
