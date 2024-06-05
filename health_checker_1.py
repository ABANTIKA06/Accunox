import urllib.request
import time

def check_application_health(url):
    try:
        response = urllib.request.urlopen(url)
        if response.getcode() == 200:
            return "UP"
        else:
            return "DOWN"
    except urllib.error.URLError as e:
        return "DOWN"

def main():
    url = "https://www.google.com"  # Replace with your application's URL
    while True:
        status = check_application_health(url)
        print(f"Application Status: {status}")
        time.sleep(1)

if __name__ == "__main__":
    main()