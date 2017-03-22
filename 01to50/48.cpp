#include <iostream>
#include <math.h>
#include <stdio.h>
using namespace std;

int main(){

    unsigned long long int counter = 0;
    long long mod_number = 1000000000;
    int number;

    for (int i = 1; i <= 1000; i++){
        number = pow(i, i);
        printf("Number : %d\n", number);
        counter += number % mod_number;
        printf("counter: %llu\n", counter);
    }

    return 0;
}
