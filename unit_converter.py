# Functions #
def convert_length(value, to_unit):
    if to_unit == 'feet': # Centimetres -> Feet.
        return value * 0.0328084
    elif to_unit == 'cm': # Feet -> Centimetres.
        return value / 0.0328084  # Converting from feet to cm
    else:
        return value # If values are the same/invalid.

def convert_weight(value, to_unit):
    if to_unit == 'lbs': # Kilograms -> Pounds.
        return value * 2.20462
    elif to_unit == 'kg': # Pounds -> Kilograms.
        return value / 2.20462
    else:
        return value # If values are the same/inavlid.

def convert_temperature(value, to_unit):
    if to_unit == 'fahrenheit': # Celsius -> Fahrenheit.
        return (value * 9/5) + 32 
    elif to_unit == 'celsius': # Fahrenheit -> Celsius.
        return (value - 32) * 5/9 
    else:
        return value # If values are the same/invalid.

def conversion_details():
    value = float(input("[SYSTEM] Enter the value you want to convert: "))
    to_unit = input("[SYSTEM] Enter the unit you want to convert to: ").lower()
    return value, to_unit

def main():
    value, to_unit = conversion_details()
    
    if to_unit in ['feet', 'cm', 'm']:
        result = convert_length(value, to_unit)
    elif to_unit in ['lbs', 'kg']:
        result = convert_weight(value, to_unit)
    elif to_unit in ['fahrenheit', 'celsius']:
        result = convert_temperature(value, to_unit)
    else:
        print("[SYSTEM] Input was invalid, try again.")
        return # rerun main.

    print(f"Result is: {result} {to_unit}")

# Execute the program #  
if __name__ == "__main__":
    main()
