# -*- coding: utf-8 -*-
"""
Created on Tue March  26 08:345:47 2025

@author: IAN CARTER KULANI

"""

from colorama import Fore
import pyfiglet
import os
font=pyfiglet.figlet_format("Echo Client")
print(Fore.GREEN+font)

import socket

def print_error_and_exit(message):
    print(message)
    exit(1)

def main():
    # Prompt user for server details
    server_ip = input("Enter the server IP address:")
    server_port = int(input("Enter the server port number:"))
    
    # Prompt for the message to send
    message = input("Enter the message to send to the server:")

    # Create a socket
    try:
        sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print_error_and_exit(f"Error creating socket: {e}")

    # Set up the server address
    server_addr = (server_ip, server_port)

    # Connect to the server
    try:
        sockfd.connect(server_addr)
    except socket.error as e:
        print_error_and_exit(f"Connection to the server failed: {e}")

    print(f"Connected to the server at {server_ip}:{server_port}")

    # Send the message to the server
    try:
        sockfd.sendall(message.encode())
    except socket.error as e:
        print_error_and_exit(f"Error sending data to server: {e}")
    
    print(f"Message sent to server: {message}")

    # Receive the echoed message from the server
    try:
        data = sockfd.recv(1024)
        if not data:
            print("Server closed the connection.")
        else:
            print(f"Received echoed message from server: {data.decode()}")
    except socket.error as e:
        print_error_and_exit(f"Error receiving data from server: {e}")

    # Close the socket
    sockfd.close()
    print("Connection closed.")

if __name__ == "__main__":
    main()
