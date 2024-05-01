# Script Name:                  Uptime Sensor Tool Part 2 of 2
# Author:                       Gilbert Collado
# Date of latest revision:      05/01/2024
# Purpose:                      creat a script that Ask the user for an email address and password to use for sending notifications. Send an email to the administrator if a host status changes (from “up” to “down” or “down” to “up”). Clearly indicate in the message which host status changed, the status before and after, and a timestamp of the event.
# Source1:                      https://docs.python.org/3/library/email.examples.html
# Source2:                      https://github.com/codefellows/seattle-cybersecurity-401d12/blob/main/class-03/challenges/DEMO.md

#!/usr/bin/env python3

import os
import time
import smtplib
from email.mime.text import MIMEText

def ping_host(ip_address):
    response = os.system("ping -c 1 -W 2 " + ip_address + " > /dev/null 2>&1")
    return response == 0

def send_email(sender_email, password, receiver_email, subject, body):
    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = receiver_email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

def main():
    sender_email = input("Enter your email address: ")
    password = input("Enter your email password: ")
    receiver_email = "gilbert.collado.codefellows@gmail.com"  # Change this to your administrator's email address
    destination_ip = "8.8.8.8"  # Change this to your desired destination IP
    
    previous_status = None
    while True:
        current_status = "Active" if ping_host(destination_ip) else "Inactive"
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        if current_status != previous_status:
            if previous_status is not None:  # Avoid sending an email on the first check
                subject = f"Status Change Detected for {destination_ip}"
                body = f"Status for {destination_ip} changed from {previous_status} to {current_status} at {timestamp}."
                send_email(sender_email, password, receiver_email, subject, body)
            print(f"{timestamp} Status changed from {previous_status} to {current_status} for {destination_ip}")
            previous_status = current_status
        else:
            print(f"{timestamp} Network {current_status} to {destination_ip}")

        time.sleep(2)  # Wait for 2 seconds before next ping

if __name__ == "__main__":
    main()


