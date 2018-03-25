#include<stdio.h>
#include<stdlib.h>

int main(){
	int mof,vala,valb,a,b,binario(int),mofiz(int,int),decimal(int),pot(int,int);
	scanf("%d%d",&a,&b);
	vala=binario(a);
	printf("%d\n",vala);
	valb=binario(b);
	printf("%d\n",valb);
	mof=mofiz(vala,valb);
	printf("%d\n",mof);
	return 0;
}

int binario(int n){
	int bin,ben,i,binar=0,cont=0,m=n;
	while(n>0){
		ben=n%2;
		n=(n-ben)/2;
		cont++;
	}
	for(i=cont;i==0;i--){
		bin=m%2;
		binar=binar+bin*pot(10,i);
		m=(m-bin)/2;
	}
	return bin;
}

int pot(int n,int cont){
	if(cont==0){
		return 1;
	}else{
		if(cont==1){
			return n;
		}else{
			return n*n;	
		}
	}
}

int mofiz(int a,int b){
	int soma,val,i,var;
	for(i=0;i<32;i++){
		soma=((a%pot(10,i))/pot(10,i))+((b%pot(10,i))/pot(10,i));
		if(soma==2){
			val+=0;
		}else{
			val=val+soma*pot(10,i);
		}
	}
	var=decimal(val);
	printf("%d",var);
	return var;
}

int decimal(int n){
	int i,dec=0,val;
	for(i=0;i<32;i++){
		val=(n/pot(10,i));
		dec=dec+val*pot(2,i);
	}
	return dec;
}
