# 1 - enter name, check name
# 2 - pin, validation
# 3 - show balance, show operations(withdraw, deposit, balance)

your_name = input("Please enter your name:")

from clientbase import clients, commands
from all_functions import find_name, get_client, check_pin, check_entered_sum, withdrawal, deposit, show_balance, display_options

while True:
    if not find_name(your_name):
        print("Client does not exist.")
        break
    current_client = {}
    current_client = get_client(your_name, clients, current_client)
    current_client = current_client[0]

    your_pin = input("Please enter your PIN:")

    if not check_pin(your_pin):
        print("You have entered an incorrect PIN 3 times. Card blocked.")
        break
    print("What would you like to do?")
    display_options(commands)
    command = input()

