// Headers //
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>

// Functions //
int game(char user, char computer) {
    // Results //
    if (user == computer) { // Draw.
        return 0;
    }
    
    if (user == 'r' && computer == 'p') { // Computer wins.
        return -1;
    }
    
    if (user == 'r' && computer == 's') { // User wins.
        return 1;
    }
    
    if (user == 'p' && computer == 's') { // Computer wins.
        return -1;
    }
    
    if (user == 'p' && computer == 'r') { // User wins.
        return 1;
    }
    
    if (user == 's' && computer == 'r') { // Computer wins.
        return -1;
    }
    
    if (user == 's' && computer == 'p') { // User wins. 
        return 1;
    }
}

int main() {
    // Variables //
    srand(time(NULL));
    int number = rand() % 3 + 1; // Computer Choice / 1-3.
    int input;
    char user, computer;
    int u_wins = 0, draws = 0, c_wins = 0;
    
    while (1) {
        // Menu //
        printf("--- Rock, Paper, Scissors Game ---\n");
        printf("0. Exit\n");
        printf("1. Rock\n");
        printf("2. Paper\n");
        printf("3. Scissors\n");
        // User's input //
        printf("[SYSTEM] Give me your input:\n");
        scanf("%d", &input);
        
        if (input == 0) {
            break;
        } else if (input == 1) {
            user = 'r';
        } else if (input == 2) {
            user = 'p';
        } else if (input == 3) {
            user = 's';
        } else {
            printf("[SYSTEM] Input was invalid.");
        }
        
        // Determine Computer's pick //
        if (number == 1) {
            computer = 'r';
        } else if (number == 2) {
            computer = 'p';
        } else {
            computer = 's';
        }
        
        // Determine Result //
        printf("[SYSTEM] You have chosen %c\n", user);
        printf("[SYSTEM] Computer has chosen %c\n", computer);
        if (game(user, computer) == -1) { // Computer wins.
            printf("[SYSTEM] Computer takes this round!\n");
            c_wins++;
        } else if (game(user, computer) == 1) { // User wins.
            printf("[SYSTEM] You win this round!\n");
            u_wins++;
        } else {
            printf("[SYSTEM] It's a draw!\n");
            draws++;
        }
    }
    
    if (u_wins + c_wins + draws > 0) { // At least one game has been made.
        printf("[SYSTEM] Session has concluded with the following stats-> User:%d Draws: %d Computer: %d", u_wins, draws, c_wins);
    }
    
    return 0;
}
