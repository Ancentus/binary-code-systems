#include <stdio.h>
#include <string.h>

// // Function to convert binary to gray
// unsigned int binaryToGray(unsigned int num)
// {
//     // Right shift by 1 bit
//     unsigned int gray = num >> 1;
    
//     // XOR with original number
//     gray = gray ^ num;

//     return gray;
// }

// Function to convert binary to gray
void binaryToGray(char *binary)
{
    int len = strlen(binary);
    int i;

    // Gray code starts with the most significant bit (MSB) same as binary
    // Initialize the gray code with the MSB of binary code
    char gray[len+1];
    gray[0] = binary[0];

    // Iterate through the remaining bits and perform XOR operation
    // to generate gray code
    for (i = 1; i < len; i++) {
        gray[i] = (binary[i-1] != binary[i]) ? '1' : '0';
    }

    // Null-terminate the gray code string
    gray[len] = '\0';

    printf("Gray code: %s\n", gray);
}

int main()
{
    char binary[100];
    printf("Enter binary number: ");
    scanf("%s", binary);

    binaryToGray(binary);

    return 0;
}
