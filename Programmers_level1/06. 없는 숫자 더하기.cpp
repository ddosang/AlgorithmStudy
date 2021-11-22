#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// numbers_len은 배열 numbers의 길이입니다.
int solution(int numbers[], size_t numbers_len) {
    int answer = 0;
    
    int whole_numbers[10] = {0,1,2,3,4,5,6,7,8,9};
    for(int i =0; i < numbers_len; i++) {
        whole_numbers[numbers[i]] = 0;
    }
    
    for(int i = 0; i<10; i++) {
        answer += whole_numbers[i];
    }
    
    return answer;
}
