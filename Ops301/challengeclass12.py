# Script Name:                  Ops Challenge - Python Requests Library
# Author:                       Gilbert Collado
# Date of latest revision:      04/09/2024
# Purpose:                      Create a script that uses library requests
# Source1:                      https://github.com/codefellows/seattle-ops-301d12/tree/main/class-12/challenges
# Source2:                      https://gemini.google.com/app/fa1cfb31e4a45b3e

import requests

# Translate HTTP status codes into plain terms
def translate_status_code(code):
    status_codes = {
        200: 'OK', 201: 'Created', 204: 'No Content',
        301: 'Moved Permanently', 302: 'Found', 304: 'Not Modified',
        400: 'Bad Request', 401: 'Unauthorized', 403: 'Forbidden', 404: 'Not Found',
        405: 'Method Not Allowed', 500: 'Internal Server Error', 502: 'Bad Gateway',
        503: 'Service Unavailable'
    }
    return status_codes.get(code, 'Unknown Status Code')

# Handle the main logic
def main():
    # Prompt user for destination URL
    destination_url = input("Enter the destination URL: ")

    # Prompt user to select HTTP Method
    method = input("Enter the HTTP Method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ").upper()
    
    # Validate HTTP Method
    if method not in ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'PATCH', 'OPTIONS']:
        print("Invalid HTTP Method!")
        return
    
    # Print the entire request about to be sent
    print(f"Sending {method} request to: {destination_url}")

    # Ask for confirmation before proceeding
    if input("Do you want to proceed? (yes/no): ").lower() != 'yes':
        print("Request aborted.")
        return
    
    # Perform the request using requests library
    response = requests.request(method, destination_url)
    
    # Print response status code and translate it into plain terms
    print("\nResponse:")
    print("Status Code:", response.status_code, translate_status_code(response.status_code))
    
    # Print response headers
    print("\nResponse Headers:")
    for key, value in response.headers.items():
        print(key + ":", value)

# Execute main function if the script is run directly
if __name__ == "__main__":
    main()


