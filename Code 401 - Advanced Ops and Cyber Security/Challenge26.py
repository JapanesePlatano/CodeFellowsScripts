# Script Name:                  Event Logging Tool Part 1 of 3
# Author:                       Gilbert Collado
# Date of latest revision:      06/03/2024
# Purpose:                      This Python script is a modification of my uptime sensor tool created for OpsChallenge03.Logging in this script provides real-time and historical tracking of network status checks and email notifications, facilitating debugging, operational monitoring, and error handling.
# Source1:                      https://docs.python.org/3/howto/logging.html#logging-basic-tutorial
# Source2:                      https://github.com/codefellows/seattle-cybersecurity-401d12/blob/main/class-26/challenges/DEMO.md

#!/usr/bin/env python3

import os
import time
import smtplib
from email.mime.text import MIMEText
import logging

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create handlers
file_handler = logging.FileHandler('network_monitor.log')
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Create formatters and add them to handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def ping_host(ip_address):
    logger.debug(f"Pinging {ip_address}")
    response = os.system("ping -c 1 -W 2 " + ip_address + " > /dev/null 2>&1")
    if response == 0:
        logger.info(f"{ip_address} is reachable.")
    else:
        logger.warning(f"{ip_address} is not reachable.")
    return response == 0

def send_email(sender_email, password, receiver_email, subject, body):
    logger.debug(f"Attempting to send email to {receiver_email}")
    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = receiver_email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        logger.info("Email sent successfully.")
    except Exception as e:
        logger.error("Failed to send email", exc_info=True)

def main():
    sender_email = input("Enter your email address: ")
    password = input("Enter your email password: ")
    receiver_email = "gilbert.collado.codefellows@gmail.com"
    destination_ip = "8.8.8.8"
    
    previous_status = None
    while True:
        current_status = "Active" if ping_host(destination_ip) else "Inactive"
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        if current_status != previous_status:
            if previous_status is not None:
                subject = f"Status Change Detected for {destination_ip}"
                body = f"Status for {destination_ip} changed from {previous_status} to {current_status} at {timestamp}."
                send_email(sender_email, password, receiver_email, subject, body)
                logger.info(f"Status change email sent: {previous_status} -> {current_status}")
            print(f"{timestamp} Status changed from {previous_status} to {current_status} for {destination_ip}")
            logger.info(f"Status changed from {previous_status} to {current_status} for {destination_ip}")
            previous_status = current_status
        else:
            print(f"{timestamp} Network {current_status} to {destination_ip}")
            logger.debug(f"Network {current_status} to {destination_ip}")

        time.sleep(2)

if __name__ == "__main__":
    main()
