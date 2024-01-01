your_name = input("Please enter your name:")

import mysql.connector
from db_essentials import db_config, connect_to_database, disconnec_from_database
connection, cursor = connect_to_database(db_config)
from clientbase import clients, commands
from all_functions import find_name, get_client, check_pin, check_entered_sum, withdrawal, deposit, show_balance, display_options, operations


while True:
    if not find_name(your_name, clients):
        print("Client does not exist.")
        break
    current_client = {}
    current_client = get_client(your_name, clients, current_client)
    current_client = current_client[0]

    your_pin = input("Please enter your PIN:")

    if not check_pin(your_pin, current_client):
        print("You have entered an incorrect PIN 3 times. Card blocked.")
        break
    print("What would you like to do?")
    display_options(commands)
    command = input()
    
    while not operations(command):
        command = input("Please choose from one of the options by typing in the respective number:")
        if operations(command):
            break
    command = int(command)
    if command == 1:
        command = input("Enter the ammount you wish to withdaw:")
        command = check_entered_sum(command, current_client)
        print(withdrawal(command,current_client))
        break
    elif command == 2:
        command = input("Enter the ammount you wish to deposit:")
        command = check_entered_sum(command, current_client)
        print(deposit(command,current_client))
        break
    elif command == 3:
        show_balance(current_client)
        break
    else:
        print("Have a nice day!")
        break
disconnec_from_database(connection, cursor)