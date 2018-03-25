#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){
	char vert[20],gen[20],com[20];
	int vertebrado(char),ver,vir,vor,vur;
	scanf("%s",&vert);
	scanf("%s",&gen);
	scanf("%s",&com);
	
	int i,cont=0,cont1=0,cont2=0,cont3=0;
	char val[20]="vertebrado",vel[20]="ave",vil[20]="carnivoro",vol[20]="onivoro";
	char pim[20]="inseto",pom[20]="hematofago";
	for(i=0;i<strlen(vert);i++){
		if(vert[i]==val[i]){
			cont++;
			if(gen[i]==vel[i]){
				cont1++;
			}
			if(com[i]==vil[i]){
				cont2++;
			}else{
				if(com[i]==vol[i]){
					cont3++;
				}
			}
		}else{
			if(gen[i]==pim[i]){
				cont1++;
			} 
			if(com[i]==pom[i]){
				cont2++;
			}
		}
	}
	
	ver=cont;
	vir=cont1;
	vor=cont2;
	vur=cont3;
	
	if(ver==10){
		if(vir==3){
			if(vor==9){
				printf("aguia\n");
			}else{
				printf("pomba\n");
			}
		}else{
			if(vur==7){
				printf("homem\n");
			}else{
				printf("vaca\n");
			}
		}
	}else{
		if(vir==6){
			if(vor==10){
				printf("pulga\n");
			}else{
				printf("lagarta\n");
			}
		}else{
			if(vor==10){
				printf("sanguessuga\n");
			}else{
				printf("minhoca\n");
			}
		}
	}
	return 0;
}

