# banner_grabber.py

import socket

def banner(ip, port):
    try:
        # Create a socket connection to the target
        s = socket.socket()
        s.settimeout(5)  # Set a timeout to handle potential delays

        # Connect to the server
        s.connect((ip, int(port)))

        # Receive and decode the banner
        banner_data = s.recv(1024).decode('utf-8')

        # Display the banner
        if banner_data:
            print(f"Banner from {ip}:{port}:\n{banner_data}")
        else:
            print(f"No banner received from {ip}:{port}")

    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        s.close()

def main():
    try:
        # Get user input for IP and Port
        ip = input("Please enter the IP: ")
        port = input("Please enter the Port: ")

        # Validate the IP and Port inputs
        if not ip or not port.isdigit():
            print("Invalid input. Please enter a valid IP and Port")
            return

        # Call the banner function
        banner(ip, port)

    except KeyboardInterrupt:
        print("\nBanner grabbing interrupted by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
