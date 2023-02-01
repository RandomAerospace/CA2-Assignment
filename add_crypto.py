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

class enterstringplsException():
    """This comes up when a string is not entered"""

class enterdigitplsException():
    """This comes up when a digit is not entered"""


#manually input crypto data, might want to add a path for automatic info filling
def addcrypto(data):
    state_count=0 #program flag 1
    run_state=True #program flag 2
    update_state=0 #program flag 3 in tandem with update feature
    while(run_state==True):
        try:
        
            

            if state_count==0 and run_state==True:
                print('press E to cancel at any point')
                live_data_or_not=input("Do you want your cryptocurrency to be automatically updated? y/n")
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



            if state_count==1 and run_state==True:
                new_crypto=input('Enter Cryptocurrency name:\t')
                
                if new_crypto.upper()=='E':
                    run_state=False
                     #special state count for premature exits
                elif new_crypto.isdigit()==True:
                    print('Please enter in letters')
                    assert enterstringplsException()


                else:
                    #check if crypto currency is there
                    unique_state=cryptocheck(data, new_crypto) #returns boolean state, if unique, will be true
                    
                    if unique_state==False:
                        print("The crypto currency you entered already exists in your data base, maybe you might want to update it's other data")
                        assert uniquestate_error()
                    
                        #Look up ticker
                    if update_state==1:
                        print('Looking for coin in our database...')
                        new_ticker=getTicker(new_crypto)
                        ticker_acceptance=input(f'Woop, we found this ticker {new_ticker} is this what you want? y/n')

                        if ticker_acceptance.upper()=='Y':
                            state_count+=1 #proceed to get market data (state count=2)
                        if ticker_acceptance.upper()=='N':
                            update_state=0
                            state_count+=1 #proceed as usual, have to manually enter
                        elif update_state==0:
                            state_count+=1
                    if update_state==0:
                        state_count+=1
    

                    
            elif state_count==2 and run_state==True and update_state==1:
                print('Getting market data..')
                new_market_price,addon_market_cap=add_live_data(new_ticker)
                print(f'Market Cap of Crypto:{addon_market_cap}')
                state_count+=1

            elif state_count==2  and run_state==True and update_state==0 :
                addon_market_cap=input('Enter market cap of crypto High,Mid,Low=\t')
                if (str(addon_market_cap)).upper()=='E':
                    run_state=False
                elif addon_market_cap.isdigit()==True:
                    print('Please enter High Mid or Low')
                    assert enterstringplsException()
                    #make sure it is also high mid or low
                 
                else:
                    state_count+=1
          

                
            #Input takes in float to go through a value type check.
            #it then coverts back to string for the sake of ease of data processing in other functions and saving data
            elif state_count==3  and run_state==True:
                new_quantity=input('enter quantity of crypto bought=\t')

                if (str(new_quantity)).upper()=='E':
                    run_state=False
                elif new_quantity.isdigit()==True :
                    new_quantity=str(new_quantity)
                    state_count+=1
                else:
                    print("Please enter a digit")
                    assert enterdigitplsException()

            elif state_count==4  and run_state==True:
                new_buy_in=input('enter buy in price of crypto=\t')
                if (str(new_buy_in)).upper()=='E':
                    run_state=False
                elif new_buy_in.isdigit()==True:
                    new_buy_in=str(new_buy_in)
                    state_count+=1
                else:
                    print("Please enter a digit")
                    assert enterdigitplsException()
             


            elif state_count==5 and run_state==True and update_state==1:
               
                print(f'Market Price of Crypto:\t{new_market_price}')
                state_count+=1




            elif state_count==5  and run_state==True:
                new_market_price=input('Enter market price crpyto=\t')
                if (str(new_market_price)).upper()=='E':
                    run_state=False
                elif new_market_price.isdigit()==True:
                    new_market_price=str(new_market_price)
                    state_count+=1    
                else:
                    print("Please enter a digit")
                    assert enterdigitplsException()
                    
        
          
            elif state_count==6: 
                add_data=[new_crypto,addon_market_cap,new_quantity,new_buy_in,new_market_price,update_state]
                #print(add_data)
                data.append(add_data)   
                run_state=False
                return data
                #print(run_state)

            elif state_count==7:
                run_state=False

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
        if i[0]==new_crypto: #element zero is where names are stored
            unique_state=False

    return unique_state

def isfloat(num):
    print('floatcheck')
    if float(num)==True:
        return True
    else:
        return False
    
   

#def autofill(data)
#ask customer to input tiker. Program will find ticker and add to the list info such as name,buy in price and market price at that point
#if applicable, will also put in market cap.(Research what is considered high or low)


    



    

