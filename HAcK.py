import webbrowser
import time
import sys

def slow_print(text, delay=0.2):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print() 

url = 'https://githubman6996.github.io/05konz-blooket-site/'

while True:
    user = input("Enter the passkey to hack Blooket: ")

    if "coco" in user.lower():
        slow_print("Access granted! open the bookmark bar and when you get there drag one of the buttons to the bookmark bar and click the bookmark when in dashboard, you will be gone to the website in 10 seconds", delay=0.1)
        time.sleep(8)
        webbrowser.open_new_tab(url)
        break
    else:
        slow_print("Incorrect passkey.", delay=0.1)


