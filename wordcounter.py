# Libraries #
import re # regular expressions.

# Functions #
def count_names(names):
    count = names.count('"') # must be an even number, else there is an error.
    
    if (count % 2 == 0):
        return count // 2
    else:
        print("Number of quotes are odd, check again.")

def extract_names(input_names):
    # Find all names enclosed in double quotes, including spaces #
    names = re.findall(r'"([^"]+)"', input_names)
    return names

def find_common_names(in_names1, in_names2):
    names1 = extract_names(in_names1)
    names2 = extract_names(in_names2)
    
    # Find Common Names #
    common_names = set(names1) & set(names2)
    return common_names 

def main():
    input_names1 = str(input("[SYSTEM] Give your names/strings: "))
    input_names2 = str(input("[SYSTEM] Give your names/strings (2): "))
    
    total_names = count_names(input_names1)
    print("[SYSTEM] Total number of names:", total_names)
    
    common_names = find_common_names(input_names1, input_names2)
    print("[SYSTEM] Common names are: ", common_names)

if __name__ == "__main__":
    main()