# Libraries # 
import pyshorteners

# Input the URL to be shortend #
url = input('Enter the URL: ')

# Functions #
def urlshortener(url):
    s =  pyshorteners.Shortener()
    print(s.tinyurl.short(url))

# Main #
def main():
    urlshortener(url)

if __name__ == '__main__':
    main()
