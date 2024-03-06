# Libraries # 
import pyshorteners

# Functions #
def urlshortener(url):
    s = pyshorteners.Shortener()
    print(s.tinyurl.short(url))

# Main #
def main():
    # Input the URL to be shortend #
    url = input("Enter the URL you want to be shortened: ")
    
    urlshortener(url)

# Execute the program #
if __name__ == '__main__':
    main()
