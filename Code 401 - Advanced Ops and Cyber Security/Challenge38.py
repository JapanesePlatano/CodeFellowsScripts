# Script Name:                  XSS Vulnerability Detection with Python
# Author:                       Gilbert Collado
# Date of latest revision:      06/19/2024
# Purpose:                      The script detects SQL Injection vulnerabilities in web forms by submitting SQL payloads and analyzing the response for common SQL error messages.
# Source1:                      https://thepythoncode.com/article/sql-injection-vulnerability-detector-in-python
# Source2:                      https://github.com/codefellows/seattle-cybersecurity-401d12/blob/94b03a684510d5e7a1df119d65c1139751492c26/class-38/challenges/DEMO.md

# Import libraries
import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

# Declare functions

### Function Explanation ###
### This function extracts all HTML forms from a given web page. ###
### It is essential for identifying potential points for user input, which may be vulnerable to SQL Injection attacks. ###
def get_all_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

### Function Explanation ###
### This function extracts details from a form, including its action URL, method, and input fields. ###
### Understanding the structure of the form is necessary to construct appropriate payloads and to submit the form correctly. ###
def get_form_details(form):
    details = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

### Function Explanation ###
### This function submits a form with a given payload to a target URL. ###
### It constructs the form data with the payload and submits it using the appropriate HTTP method (GET or POST). ###
### This step is crucial for testing if the payload triggers any SQL Injection vulnerabilities. ###
def submit_form(form_details, url, value):
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

### Function Explanation ###
### This function scans a given URL for SQL Injection vulnerabilities by submitting SQL payloads to all detected forms. ###
### It checks the response for common SQL error messages to determine if an SQL Injection vulnerability exists. ###
def scan_sql_injection(url):
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    sql_payload = "' OR '1'='1"
    is_vulnerable = False
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, sql_payload).content.decode()
        # Checking for common SQL error messages in the response
        errors = [
            "you have an error in your sql syntax;",
            "warning: mysql",
            "unclosed quotation mark after the character string",
            "quoted string not properly terminated"
        ]
        if any(error in content.lower() for error in errors):
            print(f"[+] SQL Injection Detected on {url}")
            print(f"[*] Form details:")
            pprint(form_details)
            is_vulnerable = True
    return is_vulnerable

# Main

### Main Function Explanation ###
### The main function serves as the entry point for the script execution. ###
### It prompts the user for a URL, scans the URL for SQL Injection vulnerabilities, and prints the results. ###
### This function ensures the script runs in a structured manner, prompting user input and invoking the scan_sql_injection function. ###
if __name__ == "__main__":
    url = input("Enter a URL to test for SQL Injection:") 
    print(scan_sql_injection(url))

### TODO: Test this script against one SQL Injection-positive target and one SQL Injection-negative target
### TODO: Paste the outputs here as comments in this script, clearly indicating which is positive detection and which is negative detection
