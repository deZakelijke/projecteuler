#include <iostream>
#include <math.h>
#include <stdio.h>
using namespace std;

int main(){

    unsigned long long int counter = 0;
    long long mod_number = 10000000000;
    long long  number;

    for (int i = 1; i <= 1000; i++){
        number = 1;
        for (int j = 1; j <=i; j++){
            number *= i;
            number = number % mod_number;
        }
        counter += number;
        counter = counter % mod_number;
    }
    printf("%llu\n", counter);

    return 0;
}
