#include <stdio.h>

int main() {
    float r, t;
    
    if (scanf("%f %f", &r, &t) == 2) {
        float phi = 22.0 / 7.0;
        
        float volume = phi * r * r * t;
        float luas = 2 * phi * r * (r + t);
        float keliling = 2 * phi * r;
        
        printf("Volume = %.2f\n", volume);
        printf("Luas = %.2f\n", luas);
        printf("Keliling = %.2f\n", keliling);
    }
    
    return 0;
}