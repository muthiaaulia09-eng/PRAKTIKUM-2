#include <math.h>
#include <stdio.h>

int main() {
    float a, b;
    
    if (scanf("%f %f", &a, &b) == 2) {
        float alas = sqrt((b * b) - (a * a));
        float tinggi = a;
        float keliling = alas + tinggi + b;
        float luas = 0.5 * alas * tinggi;
        
        printf("Alas = %d cm\n", (int)alas);
        printf("Tinggi = %d cm\n", (int)tinggi);
        printf("Keliling = %d cm\n", (int)keliling);
        printf("Luas = %d cm^2\n", (int)luas);
    }
    
    return 0;
}