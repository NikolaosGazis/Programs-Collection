// Headers //
#include<stdio.h>
#include<math.h>

// Functions //
int decToBinary() {
    // Do something.
}

int binToDecimal() {
    // Do something.
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
            case 1:
                // Decimal to Binary.
                break;
            case 2:
                // Binary to Decimal.
                break;
            default:
                printf("[SYSTEM] Input was invalid.");
                break;
        }
    }
    
    return 0;
}
