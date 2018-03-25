#include<stdio.h>
#include<stdlib.h>

int main(){
	int n,h,m,s,i,dia[2],hora[2],minuto[2],segundo[2];
	char li[3],xo[3];
		
		printf("Dia ");
		scanf("%d",&n);
		scanf("%d%s%d%s%d\n",&h,&li,&m,&xo,&s);
		dia[0]=n;
		hora[0]=h;
		minuto[0]=m;
		segundo[0]=s;
		
		printf("Dia ");
		scanf("%d",&n);
		scanf("%d%s%d%s%d",&h,&li,&m,&xo,&s);
		dia[1]=n;
		hora[1]=h;
		minuto[1]=m;
		segundo[1]=s;
	
	if(hora[0]<=hora[1] && minuto[0]<=minuto[1] && segundo[0]<=segundo[1]){
		printf("%d dia(s)\n",dia[1]-dia[0]);
	}else{
		if(hora[0]<=hora[1] && minuto[0]<=minuto[1] && segundo[0]<=segundo[1]){
			printf("%d dia(s)\n",dia[1]-dia[0]-1);
		}else{
			if(hora[0]>=hora[1] && minuto[0]<=minuto[1] && segundo[0]<=segundo[1]){
				printf("%d dia(s)\n",dia[1]+30-dia[0]);
			}else{
				printf("%d dia(s)\n",dia[1]+30-dia[0]-1);
			}
		}
	}
	
	if(hora[0]<=hora[1] && minuto[0]<=minuto[1] && segundo[0]<=segundo[1]){
		printf("%d hora(s)\n",hora[1]-hora[0]);
	}else{
		if(hora[0]>=hora[1] && minuto[0]<=minuto[1] && segundo[0]<=segundo[1]){
			printf("%d hora(s)\n",(hora[1]+24)-hora[0]);
		}else{
			if(hora[0]<=hora[1] && minuto[0]>=minuto[1]){
				printf("%d hora(s)\n",hora[1]-hora[0]-1);
			}else{
				printf("%d hora(s)\n",(hora[1]+24)-hora[0]-1);
			}
		}
	}
	
	if(minuto[0]<=minuto[1] && segundo[0]<=segundo[1]){
		printf("%d minuto(s)\n",minuto[1]-minuto[0]);
	}else{
		if(minuto[0]<=minuto[1] && segundo[0]>=segundo[1]){
			printf("%d minuto(s)\n",minuto[1]-minuto[0]-1);
		}else{
			if(minuto[0]>=minuto[1] && segundo[0]<=segundo[1]){
				printf("%d minuto(s)\n",(minuto[1]+60)-minuto[0]);
			}else{
				printf("%d minuto(s)\n",(minuto[1]+60)-minuto[0]-1);
			}
		}
	}

	if(segundo[0]<=segundo[1]){
		printf("%d segundo(s)\n",segundo[1]-segundo[0]);
	}else{
		printf("%d segundo(s)\n",(segundo[1]+60)-segundo[0]);
	}
	
	return 0;
}
