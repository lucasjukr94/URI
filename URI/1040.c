#include<stdio.h>
#include<stdlib.h>

int main(){
	double a,b,c,d,media,e,mf;
	scanf("%lf%lf%lf%lf",&a,&b,&c,&d);
	media=(a*2+b*3+c*4+d)/10.0;
	printf("Media: %.1lf\n",media);
	if(media<5){
		printf("Aluno reprovado.\n");
	}else{
		if(media<7){
			printf("Aluno em exame.\n");
			scanf("%lf",&e);
			printf("Nota do exame: %.1lf\n",e);
			mf=(e+media)/2.0;
			if(mf<5){
				printf("Aluno reprovado.\n");
				printf("Media final: %.1lf\n",mf);
			}else{
				printf("Aluno aprovado.\n");
				printf("Media final: %.1lf\n",mf);
			}
		}else{
			printf("Aluno aprovado.\n");
		}
	}
	return 0;
}
