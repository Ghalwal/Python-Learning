
import subprocess
import socket
import os
import iptracer

def Display_Menu():
    header = """"
    __________________________
    |       IP Locater        |
    |       IP Finder         |
    |___________   ___________|
                \  \ 
                ^_ _^
                (o o)\_________
                (_ _)\         )/\/
                  U   ||----W||
                      ||     ||
    ### Tools:
        [1] Locate an IP address
        [2] Get the IP address of a domain
        [3] Exit

    * Type <clear> to clear previous commands
    * Type <q> to abort operation of a tool
    """
    print(header)

def option_1():
    iptracer.locate_ip()
    Display_Menu()

def option_2():
    iptracer.get_ip()
    Display_Menu()
    Home()

def option_3():
    quit()

def Home():
    while True:
        selected_option = input("\nEnter your option\n>> ")
        if selected_option == 'clear':
            subprocess.call('cls' if os.name == 'nt' else 'clear', shell=True)
            Display_Menu()
            continue
        try:
            selected_option = int(selected_option)
            if selected_option not in [1, 2, 3]:
                raise ValueError
        except ValueError:
            print("Please enter a valid number for the option")
            continue

        if selected_option == 1:
            option_1()
        elif selected_option == 2:
            option_2()
        elif selected_option == 3:
            option_3()

def Start_Program():
    Display_Menu()
    Home()

Start_Program()
