// 1번 문제
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* reverse(char str[]) {
    char * copy = (char *)malloc(sizeof(char) * strlen(str));
    
    int len = strlen(str);
    int local_len = 0;
    for (int i = 0; i < len; i++) {
        int start = i - local_len;
        if (str[i] == ' ') {
            int copyStart = len - 2 - start - local_len + 1; // 나머지는 이 규칙이 먹히는데,
            copy[copyStart - 1] = ' ';
            
            for (int j = start; j < i; j++) {
                copy[copyStart++] = str[j];
            }
            local_len = 0;
            continue;
        }
        
        else if (i == len - 1) {
            int copyStart = 0; // 맨 마지막 것이 띄어쓰기가 아니면 위의 규칙이 안먹히고, 위의 if 문에 잡히지도 않음.
            for (int j = start; j < i; j++) {
                copy[copyStart++] = str[j];
            }
            local_len = 0;
            continue;
        }
        
        local_len++;
    }
    
    copy[len - 1] = 0;
    
    printf("\n");
    return copy;
}


int main() {
    char str[30];
    char * rev;
    
    printf("문장을 입력하세요: " );
    fgets(str, sizeof(str), stdin);

    rev = reverse(str);
    printf("%s\n", rev);
    
    return 0;
}

// 2 번 문제

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* reverse(char str[]) {
    char * copy = (char *)malloc(sizeof(char) * strlen(str));
    
    int len = strlen(str);
    int local_len = 0;
    for (int i = 0; i < len; i++) {
        int start = i - local_len;
        if (str[i] == ' ') {
            int copyStart = len - 2 - start - local_len + 1; // 나머지는 이 규칙이 먹히는데,
            copy[copyStart - 1] = ' ';
            
            for (int j = start; j < i; j++) {
                copy[copyStart++] = str[j];
            }
            local_len = 0;
            continue;
        }
        
        else if (i == len - 1) {
            int copyStart = 0; // 맨 마지막 것이 띄어쓰기가 아니면 위의 규칙이 안먹히고, 위의 if 문에 잡히지도 않음.
            for (int j = start; j < i; j++) {
                copy[copyStart++] = str[j];
            }
            local_len = 0;
            continue;
        }
        
        local_len++;
    }
    
    copy[len - 1] = 0;
    
    printf("\n");
    return copy;
}


int main() {
    int* arr = (int*)malloc(sizeof(int) * 5);
    int size = 5;
    int i = 0;
    int num = 0;
    
    do {
        printf("정수를 입력하시오 : ");
        scanf("%d", &num);
        
        if (i == size - 1) {
            size += 3;
            arr = (int*)realloc(arr, sizeof(int) * size);
        }
        
        arr[i] = num;
        i++;
    } while(num != -1);
    
    
    for(int j = 0; j < i - 1; j++) {
        printf("%d  ", arr[j]);
    }
    
    return 0;
}
