# Libraries # 
import sys
import pyshorteners

# Classes/Functions #
class URLShortener:
    def __init__(self):
        self.shortener = pyshorteners.Shortener()

    def short_url(self, url, service='tinyurl'):
        try:
            if service == 'tinyurl':
                return self.shortener.tinyurl.short(url)
            elif service == 'bitly':
                return self.shortener.bitly.short(url)
            elif service == 'isgd':
                return self.shortener.isgd.short(url)
            else:
                raise ValueError("[SYSTEM] Service selected is not compactible!")
        except Exception as e:
            return f"[SYSTEM] Error: {str(e)}"

def menu():
    print("--- URL Shortener Menu: ---")
    print("1. Shorten a URL")
    print("0. Exit")

# Main #
def main():
    menu()
    choice = input("[SYSTEM] Input your option: ")

    if choice == '1':
        url = input("Enter the URL: ")
        service = input("Choose service (tinyurl/bitly/isgd): ").lower()
        s_url = url_shortener.short_url(url, service)
        print(f"[SYSTEM] Shortened URL: {shortened_url}")
    elif choice == '2':
        print("[SYSTEM] Exiting...")
        sys.exit()
    else:
        print("Invalid input. Try again.")

# Execute the program #
if __name__ == '__main__':
    main()
