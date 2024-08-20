# Functions #
def is_palindrome(word):
    word = word.replace(" ", "").lower() # Exclude spaces.
    return word == word[::-1]

def main():
    word = input("[SYSTEM] Enter your word: ")
    if is_palindrome(word): # True.
        print("[SYSTEM] Word is palindrome!")
    else:
        print("[SYSTEM] Word is not palindrome.")

# Execute the program #
if __name__ == "__main__":
    main()
