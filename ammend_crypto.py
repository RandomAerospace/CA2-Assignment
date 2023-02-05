#Ammend crypto currency

class enterstringplsException(Exception):
    """This comes up when a string is not entered"""

class enterdigitplsException(Exception):
    """This comes up when a digit is not entered"""

def ammendcrypto_stage_one(data):
    

    #This detects how many crypto currencies there are
    
     
    while (True):
        display_crypto_options() 
        count=processdata(data) 
        user_input=input(f"Enter 0 to {count-1}, press e or E to exit: ")
    
        try:
            
            if user_input.upper()== "E":
                return data
                print("Exiting to menu...")
                exit()
            if int(user_input)<0 or int(user_input)>count-1 : #input validation
                raise ValueError

        except ValueError:
            print(f"Enter 0 to {count-1}")

        else:
            index=int(user_input)
            return data,index
            #goes onto next submenu
            #once submenu is finsihed, we will continue the while loop here

def ammend_crypto_stage_two(data,index):
     #This stage displays crypto info to be ammended
    print(f'\nIndex:\t{index}')
    print(f'1.Name:{data[index][0]}')
    print(f'2.Market Cap:\t{data[index][1]}')
    print(f'3.Quantity bought:\t{data[index][2]}')
    print(f'4.Buy in price:\t{data[index][3]}')
    print(f'5.Price:\t{data[index][4]}')
    print('E.Edit completed Exit\n')
    
        
    run_state=True #program flag 1
    while(run_state==True):
        
        edit_input=input('\nWhat do you want to edit?:\t')

        try:
                
                if check_numerical(edit_input)==False:
                    if str(edit_input).upper() == "E":
                        return data
                        print("Exiting to menu...")
                        run_state=False
                    else:
                        print('Enter a digit from 1 to 5')
                        assert enterdigitplsException()
                        
                
            
                if int(edit_input)<1 or int(edit_input)>5 : #input validation
                    raise ValueError



                elif edit_input=='1':
                    ammend_name=input('Enter New Name of Crypto:\t')
                    
                    if (str(ammend_name)).upper()=='E':
                            run_state=False
                            
                    elif check_numerical(ammend_name)==False :
                        ammend_name=str(ammend_name)
                        data[index][0]=ammend_name
                    else:
                        print("Please enter a string")
                        assert enterstringplsException()
                                    
                elif edit_input=='2':
                        ammend_market_cap_input=input('Enter in numbers, the new market cap of crypto High=1,Mid=2,Low=3 :\t')
                        
                        if (str(ammend_market_cap_input)).upper()=='E':
                            run_state=False

                        elif int(ammend_market_cap_input)<0 or int(ammend_market_cap_input)>3:
                            print('Please enter a number between 1 and 3')
                            assert enterdigitplsException()
                            
                        elif check_numerical(ammend_market_cap_input)==True :

                            if ammend_market_cap_input=='1':
                                ammend_market_cap='High'
                                ammend_market_cap=str(ammend_market_cap)
                                data[index][1]=ammend_market_cap
                                run_state=False
                                
                            elif ammend_market_cap_input=='2':
                                ammend_market_cap='Mid'
                                ammend_market_cap=str(ammend_market_cap)
                                data[index][1]=ammend_market_cap
                                run_state=False
                                
                            elif ammend_market_cap_input=='3':
                                ammend_market_cap='Low'
                                ammend_market_cap=str(ammend_market_cap)
                                data[index][1]=ammend_market_cap
                                run_state=False

                            

                        else:
                            print("Please enter a digit")
                            assert enterdigitplsException()
                            
                elif  edit_input=='3':
                    ammend_quantity_bought=input('Enter new quantity bought:\t')
                    
                    if (str(ammend_quantity_bought)).upper()=='E':
                        run_state=False
                    elif check_numerical(ammend_quantity_bought)==True :
                        ammend_quantity_bought=str(ammend_quantity_bought)
                        data[index][2]=ammend_quantity_bought
                    else:
                        print("Please enter a digit")
                        assert enterdigitplsException()
                            
                elif edit_input=='4':
                    ammend_buy_in_price=input('Enter new buy in price:\t')
                    
                    if (str(ammend_buy_in_price)).upper()=='E':
                        run_state=False
                    elif check_numerical(ammend_buy_in_price)==True :
                        ammend_buy_in_price=str(ammend_buy_in_price)
                        data[index][3]=ammend_buy_in_price
                    else:
                        print("Please enter a digit")
                        assert enterdigitplsException()

                elif edit_input=='5':
                    ammend_market_price=input('Enter new market price')

                    if (str(ammend_market_price)).upper()=='E':
                            run_state=False
                    elif check_numerical(ammend_market_price)==True :
                        ammend_market_price=str(ammend_market_price)
                        data[index][4]= ammend_market_price
                    else:
                        print("Please enter a digit")
                        assert enterdigitplsException()
                

        except ValueError:
            print(f"invalid option try again")

        except enterstringplsException:
            print('Please enter High Mid or Low ') 

        except enterdigitplsException:
            print("Enter a digit please")  

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

def check_numerical(input):
    try:
        # Convert it into integer
        val = int(input)
        return True
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
            return True
        except ValueError:
            return False

