#add crypto currency
#start->cryptocheck()->If not loop back to start
#start->crpyotcheck() pass-> move onto input validation

class uniquestate_error(Exception):
    """This comes up when the cryptocurrency name is NOT unique"""

def addcrypto(data):
    
    state_count=0
    run_state=True
    while(run_state==True):
        try:
            #define new parameters
            if state_count==0 and run_state==True:
                new_crypto=input('Enter Cryptocurrency name:\t')
                unique_state=cryptocheck(data, new_crypto) #returns boolean state, if unique, will be true
                if unique_state==False:
                    print("The crypto currency you entered already exists in your data base, maybe you might want to update it's other data")
                    assert uniquestate_error()
                else:
                    state_count+=1
                #check if crypto currency is there
                
            elif state_count==1  and run_state==True :
                addon_market_cap=int(input('Enter market cap of crypto'))
                
                state_count+=1
                

            elif state_count==2  and run_state==True:
                new_quantity=int(input('enter quantity of crypto bought=\t'))
                state_count+=1

            elif state_count==3  and run_state==True:
                new_buy_in=int(input('enter buy in price of crypto=\t'))
                state_count+=1

            elif state_count==4  and run_state==True:
                new_market_price=int(input('Enter market price crpyto=\t'))
                state_count+=1
                #print(state_count)
            elif state_count==5: 
                 
                run_state=False
                #print(run_state)
            
            
            #time to combine these to be written into a file
       
            
        except ValueError:
            print('please put in an integer please')
        
        except uniquestate_error:
            print("The crypto currency you entered already exists in your data base, maybe you might want to update it's other data")
       


    add_data=[new_crypto,addon_market_cap,new_quantity,new_buy_in,new_market_price]
    #print(add_data)
    data.append(add_data)   
    return data   

def cryptocheck(data,new_crypto):
    
    unique_state=True #boolean
    for i in data:
        if i[0]==new_crypto: #element zero is where names are stored
            unique_state=False
    
    return unique_state



    



    

