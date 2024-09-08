#include <stdio.h>
#include <math.h>
 
int main(void){
    int prime_numbers[10000];
    for(int index=0; index<10000; index++){
        prime_numbers[index]=index+1;
    }
    find_prime(prime_numbers, 10000);
 
    int T;
    scanf("%d", &T);
    for(int i=0; i<T; i++){
        int input;
        scanf("%d", &input);
 
        for(int j=input/2; j>=2; j--){
            int num1 = j;
            int num2 = input - j;
 
            if(prime_numbers[num1-1]!=0 && prime_numbers[num2-1]!=0){
                printf("%d %d\n", num1, num2);
                break;
            }
        }
    }
}
 
void find_prime(int * prime_numbers, int size){
    int max_factor = (int) sqrt((double) size);
    
    prime_numbers[0]=0;
    for(int i=2; i<=max_factor; i++){
        for(int j=0; j<size; j++){
            if(prime_numbers[j]!=0){
                if(prime_numbers[j]==i){
                    continue;
                }
                if(prime_numbers[j]%i==0){
                    prime_numbers[j]=0;
                }
            }
        }
    }
}
