# Script Name:                  Cookie Capture Capades?
# Author:                       Gilbert Collado
# Date of latest revision:      06/18/2024
# Purpose:                      This Python script fetches cookies from a target website, sets a custom cookie in a session, sends it to a different site to receive a response, saves the response to an HTML file, and opens it in Firefox while displaying an ASCII art of a cookie monster.
# Source1:                      https://www.dev2qa.com/how-to-get-set-http-headers-cookies-and-manage-sessions-use-python-requests-module/
# Source2:                      https://github.com/codefellows/seattle-cybersecurity-401d12/blob/main/class-37/challenges/DEMO.md
#!/usr/bin/env python3

import requests
import webbrowser

def bringforthcookiemonster():
    print('''
              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.
        ''')

targetsite = "http://www.whatarecookies.com/cookietest.asp" 
response = requests.get(targetsite)
cookie = response.cookies

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)

# Create a session
session = requests.Session()

# Set a cookie for the session
session.cookies.set('my_cookie', 'cookie_value')

# Send the cookie back to the site and receive an HTTP response
response = session.get('https://httpbin.org/cookies')

# Generate a .html file to capture the contents of the HTTP response
with open('response.html', 'w') as file:
    file.write(response.text)

# Open the .html file with Firefox
try:
    webbrowser.get('firefox').open('response.html')
except webbrowser.Error:
    print("Could not open Firefox. Please ensure Firefox is installed and accessible.")
