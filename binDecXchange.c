// Headers //
#include<stdio.h>
#include<stdlib.h>
#include<math.h>

// Functions //
void decToBinary(long long number) {
    int binary[64], i = 0; // 64-bit number;

    if (number == 0) { // Input is 0.
        printf("[SYSTEM] Equivalent: 0\n");
    }

    while (number > 0) {
        binary[i] = number % 2; // Store the remainder.
        number = number / 2;
        i++;
    }

    // Print the number in reverse.
    printf("[SYSTEM] Binary: ");
    for (int j = i - 1; j >= 0; j--)
        printf("%d", binary[j]);
    printf("\n");
}

long long binToDecimal(long long number) {
    long long decNumber = 0;
    int remainder, base = 1;

    while (number > 0) {
        remainder = number % 10; // Last digit.
        decNumber += remainder * base;
        number = number / 10; // Next digit.
        base = base * 2;
    }

    return decNumber;
}

// Main //
int main()
{
    // Variables //
    long long number;
    int choice;

    while (1) {
        // Input Choice //
        printf("[SYSTEM] Do you want to convert: (1) Decimal to Binary or (2) Binary to Decimal? (0 for exit)");
        scanf("%d", &choice);

        switch(choice) {
            case 0:
                printf("[SYSTEM] Exiting...");
                exit(0);
            case 1: // Decimal to Binary.
                printf("[SYSTEM] Give your decimal number: ");
                scanf("%lld", &number);
                decToBinary(number);
                break;
            case 2: // Binary to Decimal.
                printf("[SYSTEM] Give your binary number: ");
                scanf("%lld", &number);
                printf("[SYSTEM] Decimal: %lld\n", binToDecimal(number));
                break;
            default:
                printf("[SYSTEM] Input was invalid.");
                break;
        }
    }
    
    return 0;
}
