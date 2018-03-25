#include<stdio.h>
#include<stdlib.h>

int main(){
	int n,amount[100],i,coelhos=0,ratos=0,sapos=0,cobaias=0;
	char type[100];
	double coep=0,ratp=0,sapp=0,co,ra,sap,cob;
	scanf("%d",&n);
	for(i=0;i<n;i++){
		scanf("%d %c",&amount[i],&type[i]);
	}
	
	for(i=0;i<n;i++){
		cobaias=cobaias+amount[i];
		if(type[i]==67){
			coelhos=coelhos+amount[i];
		}else{
			if(type[i]==82){
				ratos=ratos+amount[i];
			}else{
				sapos=sapos+amount[i];
			}
		}
	}
	co=coelhos;
	ra=ratos;
	sap=sapos;
	cob=cobaias;
	coep=(co/cob)*100;
	ratp=(ra/cob)*100;
	sapp=(sap/cob)*100;
	
	printf("Total: %d cobaias\n",cobaias);
	printf("Total de coelhos: %d\n",coelhos);
	printf("Total de ratos: %d\n",ratos);
	printf("Total de sapos: %d\n",sapos);
	
	printf("Percentual de coelhoes: %.2lf %%\n",coep);
	printf("Percentual de ratos: %.2lf %%\n",ratp);
	printf("Percentual de sapos: %.2lf %%\n",sapp);
	return 0;
}
