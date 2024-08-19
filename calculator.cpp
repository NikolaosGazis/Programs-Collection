// Headers //
#include<iostream>
using namespace std;

// Function Initialization //
void menu();
double add(double a, double b);
double subtract(double a, double b);
double multiply(double a, double b);
double divide(double a, double b);

// Main //
int main()
{
    // Variables //
    int choice;
    double num1, num2, result;
    
    while (true) {
        menu();
        cout << "[SYSTEM] Choose the number of your operation:" << endl;
        cin >> choice;
        
        // Exit //
        if (choice == 0) {
            cout << "[SYSTEM] Exiting..." << endl;
            break;
        }
        
        // Invalid input //
        if (choice < 1 || choice > 5) {
            cout << "[SYSTEM] Input was invalid, please try again." << endl;
            continue;
        }
        
        // Numbers input //
        cout << "[SYSTEM] Number 1: ";
        cin >> num1;
        cout << "[SYSTEM] number 2: ";
        cin >> num2;
        
        // Execute Operation //
        switch (choice) {
            case 1: // Addition.
                result = add(num1, num2);
                cout << "Result: " << result << endl;
                break;
            case 2: // Subtraction.
                result = subtract(num1, num2);
                cout << "Result: " << result << endl;
                break;
            case 3: // Multplication.
                result = multiply(num1, num2);
                cout << "Result: " << result << endl;
                break;
            case 4: // Division.
                if (num2 == 0) {
                    cout << "[SYSTEM] Cannot divide with 0." << endl;
                } else {
                    result = divide(num1, num2);
                    cout << "Result: " << result << endl;
                }
                break;
        }
    }
    
    return 0;
}

// Function Implementation //
void menu() {
    cout << "0. Exit" << endl;
    cout << "1. Addition" << endl;
    cout << "2. Subtraction" << endl;
    cout << "3. Multplication" << endl;
    cout << "4. Division" << endl;
}

double add(double a, double b) {
    return a + b;
}

double subtract(double a, double b) {
    return a - b;
}

double multiply(double a, double b) {
    return a * b;
}

double divide(double a, double b) {
    return a / b;
}
