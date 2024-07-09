# Libraries #
import numpy as np

# Core #
def main():
    print("--- Roll Die Simulator ---\n")
    
    while True:
        roll = int(input("How many dice you want to roll? [1 or 2 - input 0 to end the simulation] -> "))
        match roll:
            case 0:
                break
            case 1 | 2:
                for i in range(roll):
                    print(np.random.randint(1,6))
            case _: # 'Default'.
                print("Please enter a valid number..")
    print("\n--- Ending ---")

# Execute Program #
if __name__ == '__main__':
    main()