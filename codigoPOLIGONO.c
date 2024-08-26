/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>
#include <math.h>

void defVetor(int n, int vx[], int vy[]) {
//	int i;
//  for(i=0; i<n; i++) {
//  vx[i] = rand()%10;
//  vy[i] = rand()%10;
//	}
    vx[0] = 10; vy[0] = 5;
    vx[1] = 9; vy[1] = 8;
    vx[2] = 6; vy[2] = 9;
    vx[3] = 3; vy[3] = 12;
    vx[4] = 2; vy[4] = 7;
    vx[5] = 5; vy[5] = 6;
    vx[6] = 7; vy[6] = 4;

}

void mostraVetor(int n, int vx[], int vy[]){
	int i;
	printf("\n");
	for(i=0; i<n; i++){
		printf("(%d, %d)", vx[i], vy[i]);
	}
}

void converteVetorPolig(int n, int vx[], int vy[], int vvx[], int vvy[]) {
	int i = 0;
	while(i<n) {
		vvx[i] = vx[(i+1)%n] - vx[i];
		vvy[i] = vy[(i+1)%n] - vy[i];
		i++;
	}
}
int convexo (int i, int j, int a[], int b []){
    int w;
    w = a[i]*b[j] - a[j]*b[i];
    return w;
}

void analiseConvex(int n,int vvx[],int vvy[]){
    int i = 0;
    int w;
    while (i<n){
        w = convexo(i, (i+1)%n, vvx, vvy);
        if(w<0){
        printf("\n Vertice %d e concavo\n", i);
        printf("TESTE %d\n",vvx[i]);    
        printf("TESTE %d",vvy[i]); 
        }
        else{
        printf("\n Vertice %d eh convexo\n", i);
        }
        i++;
    }
}

void vetortransl(int n, int vcx[], int vcy[]){
	int i;
	float yc = 0.0f;
	float xc= 0.0f;
	for (i=0; i<n; i++){
		yc =+ vcy[i];
		xc =+ vcx[i];
		printf("\nvalor do centro y %.2f \n", yc);
		printf("\n valor do centro x %.2f \n",xc);

	}	
	yc/=n;
	xc/=n;
	printf("\n valor do centro %.2f,%.2f", xc,yc);
}


//(vvx)[i] -= (vvx)[i+1]
//(vvy)[i] -= (vvy)[i+1]

void main(void) {
	int n;
	int vx[99], vy[99], vvx[99], vvy[99];
	printf("\n Digite o valor de n: ");
	scanf("%d", &n);
	defVetor(n, vx, vy);
	printf("\n Vertices do poligono \n");
	mostraVetor(n, vx, vy);
	converteVetorPolig(n, vx, vy, vvx, vvy);
	printf("\n Arestas do poligono \n");
	mostraVetor(n, vvx, vvy);
	analiseConvex(n, vvx, vvy);
	vetortransl(n, vvx, vvy);
}
