

''''
Unique Features:
1.Checks Crypto according to the database
2.Allows user to cancel the data entry process halfway
3.updates the data variable in the main loop.

'''

class uniquestate_error(Exception):
    """This comes up when the cryptocurrency name is NOT unique"""

def addcrypto(data):
    
    state_count=0
    run_state=True
    while(run_state==True):
        try:
            #define new parameters
            if state_count==0 and run_state==True:
                new_crypto=input('Enter Cryptocurrency name or press E to cancel at any point=\t')
                if new_crypto.upper()=='E':
                    run_state=False
                     #special state count for premature exits
                else:
                    unique_state=cryptocheck(data, new_crypto) #returns boolean state, if unique, will be true
                    if unique_state==False:
                        print("The crypto currency you entered already exists in your data base, maybe you might want to update it's other data")
                        assert uniquestate_error()
                    else:
                        state_count+=1
                    #check if crypto currency is there
                
            elif state_count==1  and run_state==True :
                addon_market_cap=input('Enter market cap of crypto High,Mid,Low=\t')
                if addon_market_cap.upper()=='E':
                    run_state=False
                 
                else:
                    state_count+=1
                
            #Input takes in float to go through a value type check.
            #it then coverts back to string for the sake of ease of data processing in other functions and saving data
            elif state_count==2  and run_state==True:
                new_quantity=float(input('enter quantity of crypto bought=\t'))
                if (str(new_quantity)).upper()=='E':
                    run_state=False
               
                else:
                    new_quantity=str(new_quantity)
                    state_count+=1

            elif state_count==3  and run_state==True:
                new_buy_in=float(input('enter buy in price of crypto=\t'))
                if (str(new_buy_in)).upper()=='E':
                    run_state=False
                
                else:
                    new_buy_in=str(new_buy_in)
                    state_count+=1

            elif state_count==4  and run_state==True:
                new_market_price=float(input('Enter market price crpyto=\t'))
                if (str(new_market_price)).upper()=='E':
                    run_state=False
                    
                else:
                    new_market_price=str(new_market_price)
                    state_count+=1
                #print(state_count)
          
            elif state_count==5: 
                add_data=[new_crypto,addon_market_cap,new_quantity,new_buy_in,new_market_price]
                #print(add_data)
                data.append(add_data)   
                run_state=False
                return data
                #print(run_state)

            elif state_count==6:
                run_state=False

        except ValueError:
            print('please put in an integer please')
        
        except uniquestate_error:
            print("The crypto currency you entered already exists in your data base, maybe you might want to update it's other data")
    
    return 0  

def cryptocheck(data,new_crypto):
    
    unique_state=True #boolean
    for i in data:
        if i[0]==new_crypto: #element zero is where names are stored
            unique_state=False
    
    return unique_state



    



    

