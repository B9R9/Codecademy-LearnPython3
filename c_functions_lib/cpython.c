#include <stdio.h>


int return_int(int a, int b){
	return a + b;
}

void print(void){
	printf("Hello World!\n");
}

int test_char(int x){
	return x + 1;
}

void print_str(char *str, size_t len){
	int index = 0;
	while (index < len){
		printf("%c", str[index]);
		index++;
	}
}

void print_test(char *str){
	int index = 0;
	while (str[index] != '\0')
	{
		printf("%d ", index);
		printf("%c", str[index]);
		index++;
	}
}
