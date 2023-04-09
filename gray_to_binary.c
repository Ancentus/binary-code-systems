#include <stdio.h>
#include <string.h>

// Function to convert gray to binary
void grayToBinary(char *gray)
{
    int len = strlen(gray);
    int i;

    // Binary code starts with the most significant bit (MSB) same as gray
    // Initialize the binary code with the MSB of gray code
    char binary[len + 1];
    binary[0] = gray[0];

    // Iterate through the remaining bits and perform XOR operation
    // to generate binary code
    for (i = 1; i < len; i++) {
        binary[i] = (gray[i] != binary[i - 1]) ? '1' : '0';
    }

    // Null-terminate the binary code string
    binary[len] = '\0';

    printf("Binary code: %s\n", binary);
}

int main()
{
    char gray[100];
    printf("Enter Gray code: ");
    scanf("%s", gray);

    grayToBinary(gray);

    return 0;
}
