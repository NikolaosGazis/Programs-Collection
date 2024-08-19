// Imports //
import java.io.*;
import java.util.Scanner;

public class BMICalc
{
    // Calculate the BMI //
    public static double get_bmi(double height, double weight) {
        height = height / 100; // To metres.
        double bmi = weight / Math.pow(height, 2);
        return bmi;
    }
    
    // Main //
    public static void main(String[] args) {
        // Initiate Scanner //
        Scanner scanner = new Scanner(System.in);
        
        // Get user's weight and height (Metric units) //
        System.out.print("[SYSTEM] Enter your height in centimetres:");
        double height = scanner.nextDouble();
        System.out.print("[SYSTEM] Enter your weight in kilograms:");
        double weight = scanner.nextDouble();
        
        double bmi = get_bmi(height, weight);
        
        // Display results //
        System.out.printf("[SYSTEM] Your BMI is: %.2f\n", bmi);
        if (bmi < 18.5) {
            System.out.print("[SYSTEM] You are... underweight!");
        } else if (bmi >= 18.5 && bmi <= 25) {
            System.out.print("[SYSTEM] You are... normal!");
        } else if (bmi > 25 && bmi < 30) {
            System.out.print("[SYSTEM] You are... overweight!");
        } else {
            System.out.print("[SYSTEM] You are... obese!");
        }
        
        scanner.close();
    }
}
