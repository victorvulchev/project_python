def find_name(client_name, client_list):
    result = any(client for client in client_list if client["name"] == client_name)
    return result

def get_client(client_name, client_list, current_client):
    current_client = [client for client in client_list if client["name"] == client_name]
    return current_client

def check_pin(entered_pin, current_client):
    counter = 0
    isCorrect = True
    while entered_pin != current_client["pin"]:
        if counter == 3:
            isCorrect = False
            break
        entered_pin = input("Please enter correct PIN:")
    return isCorrect

def check_entered_sum(numb, current_client):
    isNumb = False
    canOperate = False
    val = current_client["balance"]
    while isNumb != True and canOperate != True:
        try:
            numb_val = int(numb)
            isNumb = True
        except:
            numb = input("Enter your sum in numbers:")
            continue
        numb = int(numb)
        if numb < 0:
            numb = input("Enter a positive sum:")
        elif numb > val:
            numb = input("Not enough funds! Enter a smaller sum:")
        else:
            canOperate = True
    return numb

def withdrawal(numb, current_client):
       val = current_client["balance"]
       newSum = val - check_entered_sum(numb, current_client)
       current_client["balance"] = newSum
       return current_client["balance"]      

def deposit(numb, current_client):
    val = current_client["balance"]
    newSum = val + check_entered_sum(numb, current_client)
    current_client["balance"] = newSum
    return current_client["balance"]

def show_balance(current_client):
    print(f"Your current balancde is {current_client['balance']}")

def display_options(list):
    for i in range(0, len(list)):
        print(i)


        


'''clients = [{"name" : "Pesho", "pin": "1234", "balance": 1000},
          {"name" : "Gosho", "pin": "4321", "balance": 10000},
           {"name" : "Tosho", "pin": "5555", "balance": 6547},
            {"name" : "Misho", "pin": "0000", "balance": 230},
             {"name" : "Tisho", "pin": "5678", "balance": 800},
               ]
the_name = "Pesho"
current_client = {}
numb = 500
print(find_name(the_name, clients))
print(get_client(the_name, clients, current_client))
current_client = get_client(the_name, clients, current_client)
current_client = current_client[0]
#print(check_entered_sum("ttt",current_client[0]))
#print(withdrawal("ttt",current_client))
show_balance(current_client)'''