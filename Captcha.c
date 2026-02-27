#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

#define CAPTCHA_LENGTH 6

int main() {
    char captcha[CAPTCHA_LENGTH + 1];
    char userInput[CAPTCHA_LENGTH + 1];
    char characters[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    int i;

    // Seed the random number generator
    srand(time(NULL));

    // Generate random CAPTCHA
    for(i = 0; i < CAPTCHA_LENGTH; i++) {
        int index = rand() % (sizeof(characters) - 1);
        captcha[i] = characters[index];
    }

    // Add null terminator to make it a string
    captcha[CAPTCHA_LENGTH] = '\0';

    // Display the CAPTCHA
    printf("===== CAPTCHA Verification =====\n");
    printf("Enter the following CAPTCHA: %s\n", captcha);

    // Get user input
    printf("Input: ");
    scanf("%6s", userInput);

    // Compare user input with generated CAPTCHA
    if(strcmp(captcha, userInput) == 0) {
        printf("CAPTCHA Verified Successfully!\n");
    } else {
        printf("Incorrect CAPTCHA. Try Again.\n");
    }

    return 0;
}
