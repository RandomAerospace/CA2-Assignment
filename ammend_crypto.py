#Ammend crypto currency

def ammendcrypto_stage_one(data):
    display_crypto_options()

    #This detects how many crypto currencies there are
    count=processdata(data) 
    
    while (True):
          
        user_input=input(f"Enter 0 to {count}, press e or E to exit: ")
    
        try:
            
            if user_input.upper()== "E":
                return data
                print("Exiting to menu...")
                exit()
            if int(user_input)<0 or int(user_input)>count : #input validation
                raise ValueError

        except ValueError:
            print(f"Enter 0 to {count}")

        else:
            index=int(user_input)
            ammend_crypto_stage_two(data, index) #goes onto next submenu

def ammend_crypto_stage_two(data,index):
     #This stage displays crypto info to be ammended

    run_state=True #program flag 1
    while(run_state==True):
        print(f'Index:\t{index}')
        print(f'1.Name:{data[index][0]}')
        print(f'2.Market Cap:\t{data[index][1]}')
        print(f'3.Quantity bought:\t{data[index][2]}')
        print(f'4.Buy in price:\t{data[index][3]}')
        print(f'5. Price:\t{data[index][4]}')
        print('E.Edit completed Exit\n')
        edit_input=input('What do you want to edit?:\t')
        
        try:
                
                if edit_input.upper() == "E":
                    return data
                    print("Exiting to menu...")
                    run_state=False
                if int(edit_input)<0 or int(edit_input)>5 : #input validation
                    raise ValueError

        except ValueError:
            print(f"invalid option try again")

        else:
            if edit_input=='1':
                ammend_name=input('Enter New Name of Crypto:\t')
                if (str(ammend_name)).upper()=='E':
                    run_state=False
               
                else:
                    ammend_name=str(ammend_name)
                    data[index][0]=ammend_name
                        
            elif edit_input=='2':
                    ammend_market_cap=input('Enter new market cap of Crypto:\t')
                    if (str(ammend_market_cap)).upper()=='E':
                        run_state=False
                        
               
                    else:
                        ammend_market_cap=str(ammend_market_cap)
                        data[index][1]=ammend_market_cap
                        
            elif  edit_input=='3':
                ammend_quantity_bought=float(input('Enter new quantity bought:\t'))
                if (str(ammend_quantity_bought)).upper()=='E':
                    run_state=False
               
                else:
                    ammend_quantity_bought=str(ammend_quantity_bought)
                    data[index][2]=ammend_quantity_bought
                        
            elif edit_input=='4':
                ammend_buy_in_price=float(input('Enter new buy in price:\t'))
                if (str(ammend_buy_in_price)).upper()=='E':
                    run_state=False
               
                else:
                    ammend_buy_in_price=str(ammend_buy_in_price)
                    data[index][3]=ammend_buy_in_price

            elif edit_input=='5':
                ammend_market_price=float(input('Enter new market price'))
                if (str(ammend_market_price)).upper()=='E':
                    run_state=False
               
                else:
                    ammend_market_price=str(ammend_market_price)
                    data[index][4]= ammend_market_price

def display_crypto_options():

    print("-"*100)
    print("")
    print("No - cryptocurrency")
    print("-"*40)

def processdata(data):

    count=0
    for i in data:
        print(f'{count} - \t{i[0]}')
        count+=1
    return count



