#include<stdio.h>
#include<stdlib.h>
#include<math.h>

//Uri 2668 - mathematic
int main(){
	long long int a,b,n,k;
	scanf("%lld%lld%lld%lld",&a,&b,&n,&k);
	double x = ((double)a+sqrt((double)b));
	//printf("%lf\n",pow(x,n));
	int m = 0;
	int val = 0;
	switch(((int)x)%10){
		case 0:
			printf("%d\n",0);
			break;
		case 1:
			printf("%d\n",1);
			break;
		case 2:
			m = n%4;
			val = 0;
			switch(m){
				case 0:
					val=6;
					break;
				case 1:
					val=2;
					break;
				case 2:
					val=4;
					break;
				case 3:
					val=8;
					break;
			}
			printf("%d\n",val);
			break;
		case 3:
			m = n%4;
			val = 0;
			switch(m){
				case 0:
					val=1;
					break;
				case 1:
					val=3;
					break;
				case 2:
					val=9;
					break;
				case 3:
					val=7;
					break;
			}
			printf("%d\n",val);
			break;
		case 4:
			m = n%2;
			val = 0;
			switch(m){
				case 0:
					val=6;
					break;
				case 1:
					val=4;
					break;
			}
			printf("%d\n",val);
			break;
		case 5:
			printf("%d\n",5);
			break;
		case 6:
			printf("%d\n",6);
			break;
		case 7:
			m = n%4;
			val = 0;
			switch(m){
				case 0:
					val=1;
					break;
				case 1:
					val=7;
					break;
				case 2:
					val=9;
					break;
				case 3:
					val=3;
					break;
			}
			printf("%d\n",val);
			break;
		case 8:
			m = n%4;
			val = 0;
			switch(m){
				case 0:
					val=6;
					break;
				case 1:
					val=8;
					break;
				case 2:
					val=4;
					break;
				case 3:
					val=2;
					break;
			}
			printf("%d\n",val);
			break;
		case 9:
			m = n%2;
			val = 0;
			switch(m){
				case 0:
					val=1;
					break;
				case 1:
					val=9;
					break;
			}
			printf("%d\n",val);
			break;
	}
	return 0;
}
