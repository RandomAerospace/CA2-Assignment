''''
Unique Features:
1.Asks if user wants to live tracking of data
2..Checks Crypto according to the database
3..Allows user to cancel the data entry process halfway
4.updates the data variable in the main loop.
'''

#input validation weakness: floating point numbers cannot be checked 

from live_data import *

class uniquestate_error(Exception):
    """This comes up when the cryptocurrency name is NOT unique"""

class enterstringplsException(Exception):
    """This comes up when a string is not entered"""

class enterdigitplsException(Exception):
    """This comes up when a digit is not entered"""


#manually input crypto data, might want to add a path for automatic info filling
def addcrypto(data):
    state_count=0 #program flag 1
    run_state=True #program flag 2
    update_state=0 #program flag 3 in tandem with update feature
    print('press E to cancel at any point')
    while(run_state==True):
        try:
        
            if state_count==0 and run_state==True:
                
                live_data_or_not=input("Do you want your cryptocurrency to be automatically updated? y/n\t")
                if live_data_or_not.upper()=='E':
                    run_state=False
                     #special state count for premature exits
                #will help program detect if the data will be updated on start up or not 1=yes 0=no
                elif live_data_or_not.upper()=='Y':
                    update_state=1 
                    state_count+=1
                elif live_data_or_not.upper()=='N':
                    update_state=0
                    state_count+=1
                
                else:
                    print('Please enter Y or N')
                    assert enterstringplsException()


            elif state_count==1 and run_state==True:
                new_crypto=input('Enter Cryptocurrency name:\t')
                
                if new_crypto.upper()=='E':
                    run_state=False
                     #special state count for premature exits
                elif check_numerical(new_crypto)==True:
                    print('Please enter in letters')
                    assert enterstringplsException()


                else:
                    #check if crypto currency is there
                    new_crypto=new_crypto.upper() #fool proof way of ensuring everything is in upper case so that it is easier to check for uniqueness
                    unique_state=cryptocheck(data, new_crypto) #returns boolean state, if unique, will be true
                    
                    if unique_state==False:
                        print("The crypto currency you entered already exists in your data base, maybe you might want to update it's other data")
                        assert uniquestate_error()
                        state_count=0
                    else:
                        #manual entry
                        if update_state==0:
                            state_count+=1


                            #Look up ticker
                        if update_state==1:
                            print('Looking for coin in our database...')
                            new_ticker=getTicker(new_crypto)
                            if new_ticker==False:
                                state_count=0
                            else:
                                ticker_acceptance=input(f'Woop, we found this ticker {new_ticker} is this what you want? y/n\t')

                                if ticker_acceptance.upper()=='Y':
                                    state_count+=1 #proceed to get market data (state count=2)
                                if ticker_acceptance.upper()=='N':
                                    update_state=0
                                else:
                                    print('Please enter Y or N')
                                    assert enterstringplsException()
                                 
            elif state_count==2 and run_state==True and update_state==1:
                print('Getting market data..')
                new_market_price,addon_market_cap=add_live_data(new_ticker)
                print(f'Market Cap of Crypto:{addon_market_cap}')
                print(f'Market Price of Crypto:\t{new_market_price}')
                state_count+=1

            elif state_count==2  and run_state==True and update_state==0 :
                addon_market_cap_input=int(input('Enter in numbers, the market cap of crypto High=1,Mid=2,Low=3 :\t'))
                if (str(addon_market_cap_input)).upper()=='E':
                    run_state=False
                elif addon_market_cap_input<0 or addon_market_cap_input>3:
                    print('Please enter a number between 1 and 3')
                    assert enterdigitplsException()

                elif check_numerical(addon_market_cap_input)==False:
                    print('Please enter High Mid or Low')
                    assert enterstringplsException()
                    #make sure it is also high mid or low
                else:
                    if addon_market_cap_input==1:
                        addon_market_cap='High'
                        state_count+=1
                    elif addon_market_cap_input==2:
                        addon_market_cap='Mid'
                        state_count+=1
                    elif addon_market_cap_input==3:
                        addon_market_cap='Low'
                        state_count+=1
                    
          
    
            #Input takes in as string, input validation goes through Cancel key "E" ->checknumerical() to check if it's a int or float, returns
            #false if it is string
            #it then coverts back to string for the sake of ease of data processing in other functions and saving data
            elif state_count==3  and run_state==True:
                new_quantity=input('enter quantity of crypto bought=\t')

                if (str(new_quantity)).upper()=='E':
                    run_state=False
                elif check_numerical(new_quantity)==True :
                    new_quantity=str(new_quantity)
                    state_count+=1
                else:
                    print("Please enter a digit")
                    assert enterdigitplsException()

            elif state_count==4  and run_state==True:
                new_buy_in=input('enter buy in price of crypto=\t')
                if (str(new_buy_in)).upper()=='E':
                    run_state=False
                elif check_numerical(new_buy_in)==True:
                    new_buy_in=str(new_buy_in)
                    state_count+=1
                else:
                    print("Please enter a digit")
                    assert enterdigitplsException()
             
            elif state_count==5 and update_state==1:
                state_count+=1

            elif state_count==5 and run_state==True and update_state==0:
                new_market_price=input('Enter market price crpyto=\t')
                if (str(new_market_price)).upper()=='E':
                    run_state=False
                elif check_numerical(new_market_price)==True:
                    new_market_price=str(new_market_price)
                    state_count+=1    
                else:
                    print("Please enter a digit")
                    assert enterdigitplsException()
                    
        
            #print summary of data
            elif state_count==6: 
                print('\nNew data summary')
                print(f'Cryptocurrency name:{new_crypto}')
                print(f'Market capitalisation:{addon_market_cap}')
                print(f'Quantity bought:{new_quantity}')
                print(f'Buy in price:{new_buy_in}')
                print(f'Market price:\t{new_market_price}')
                if update_state==1:
                    update_bool=True
                    print(f'Automatic updates?\t:{update_bool}')
                else:
                    update_bool=False
                    print(f'Automatic updates?:\t{update_bool}')
                state_count+=1

            elif state_count==7:
                user_restart_input=input('Y: save changes N:Restart from beginning\t')
               
                if user_restart_input.upper()=='N':
                    state_count=0
                elif user_restart_input.upper()=='Y':
                    state_count+=1
                    
                else:
                    print('Please enter Y or N')
                    assert enterstringplsException()


                
            elif state_count==8:
                update_state=str(update_state)
                add_data=[new_crypto,addon_market_cap,new_quantity,new_buy_in,new_market_price,update_state]
                
                data.append(add_data)   
            
                
                return data
                run_state=False
                #print(run_state)

        except ValueError:
            print('please put in an integer please')
        
        except uniquestate_error:
            print("The crypto currency you entered already exists in your data base, maybe you might want to update it's other data")
        
        except enterstringplsException:
            print('Please enter High Mid or Low ') 

        except enterdigitplsException:
            print("Enter a digit please")   


def cryptocheck(data,new_crypto): 
    
    unique_state=True #boolean
    
    
    for i in data:
        if (i[0]).upper()==new_crypto: #element zero is where names are stored
            
            unique_state=False
            

    return unique_state

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