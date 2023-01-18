#remove cryptocurrency

def display_crypto_options():

    print("-"*100)
    print("")
    print("No - cryptocurrency")
    print("-"*40)
    
    #for i in range(len()):
    #    #keep track of the index of the current element in the list and user must select one of the options
    #    print(i, "-", [i]) 
    ''''''
    #user_input = input("Enter 0 to {} for your selection or E to exit: ".format(len()-1))
    #return user_input

def processdata(data):
    print(data)
    count=0
    for i in data:
        print(f'{count} - \t{i[0]}')
        count+=1
    return count


def removecrypto(data):

    
    display_crypto_options()
    #put a function here to process AND SHOW THE DATA
     
    while True:
        try:
            count=processdata(data)  
            user_input=input(f'Enter 0 to {count}, press e or E to exit: ')
            if user_input == "e" or user_input == "E":
                print("Exiting to menu...")
                exit()
            index = int(user_input)
            if index<0 or index>count:
                raise ValueError
            del data[index][0:] #data[variable][0:]
        except ValueError:
            print(f"Enter 0 to {count}")

    ''''''
    #user_input = input("Enter 0 to {} for your selection or E to exit: ".)

    #if user_input.lower() == 'e' or user_input.lower() == 'E':
    #    print("Exiting...")
    #else:
    #    try:
    #        user_input = int(user_input)
    #        if user_input >= 0 and user_input < len(crypto_list):
    #            # check for valid number
    #            selected_crypto = crypto_list[user_input]
    #            # assigns the selected crypto_currency to the variable 'selected_crypto', using the user_input as the index of the crypto_list
    #            print("You selected:", selected_crypto)
    #            crypto_list = [crypto for i, crypto in enumerate(crypto_list) if i != user_input]
    #            # create a new list with the elements you want to keep
    #            # the specified input cryptocurrency will be removed
    #            print("updated crypto_list:", crypto_list)
    #        else:
    #            print("Invalid input. Please enter a number between 0 and {} or E to exit.".format(len(crypto_list)-1)) 
    #            # input and invalid and will minus 1 from that list
    #            # .format() method is used to insert the value of len(crypto_list)-1 into the string at the location of {}
    #    except ValueError:
     #       print("Invalid input. Please enter a number between 0 and {} or E to exit.".format(len(crypto_list)-1)) 
            #used when value input is not a number 
    ''''''
