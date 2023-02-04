#Subprogram to display crypto








def display_sort_options(data):
    
    #process market cap data from High, Mid, Low to 1,2,3 to make sorting easier.
    data=data_process_market_cap(data)
    
    
    #after that, sorting is better done with dictionaries which have keys. 
    #Can use list sorting through keys with a user made method
    data=list_to_dict(data)
    
   
    print("1. Market Cap")
    print("2. Quantity")
    print("3. Buy Price")
    print("4. Market Price")
    print("5.press E to Exit to Menu")
    
    run_state=True

    while(run_state==True):
        sort_options = int(input("Choose options to sort: "))
        index = int(sort_options)
        try:
            if sort_options == 1: #market cap
                sort_order=int(input('Increasing order:1  Decreasing order:2 \t'))
                if sort_order==1:
                
                    data.sort(key=get_market_cap)
                
                elif sort_order==2:

                    data.sort(key=get_market_cap,reverse=True)
                
                data_sorted=dict_to_list(data)
                data_output=data_process_market_cap_output(data_sorted)
                    
                return data_output
                    

            elif sort_options == 2: #quantity bought, this needs addiitonal processing for numbers
                sort_order=int(input('Increasing order:1  Decreasing order:2 \t'))
                if sort_order==1:
                
                    data.sort(key=get_quantity)
                
                elif sort_order==2:
                    
                    data.sort(key=get_quantity,reverse=True)
                
                data_sorted=dict_to_list(data)
                data_output=data_process_market_cap_output(data_sorted)
                    
                return data_output

            elif sort_options == 3: #buy price
                sort_order=int(input('Increasing order:1  Decreasing order:2 \t'))
                if sort_order==1:
                
                    data.sort(key=get_buy_in_price)
                
                elif sort_order==2:
                    
                    data.sort(key=get_buy_in_price,reverse=True)
                
                data_sorted=dict_to_list(data)
                data_output=data_process_market_cap_output(data_sorted)
                    
                return data_output
            
            elif sort_options == 4:
                sort_order=int(input('Increasing order:1  Decreasing order:2 \t'))
                if sort_order==1:
                
                    data.sort(key=get_market_price)
                
                elif sort_order==2:
                    
                    data.sort(key=et_market_price,reverse=True)
                
                data_sorted=dict_to_list(data)
                data_output=data_process_market_cap_output(data_sorted)
                    
                return data_output
            
            elif sort_options == "e" or sort_options == "E":
                print("Exiting to menu...")
                break
    
            elif index<0 or index>5:
                raise ValueError
        except:
            print('')


def data_process_market_cap(data):
    for i in data:
        if i[1]=='High':
            i[1]=1
        if i[1]=='Mid':
            i[1]=2
        if i[1]=='Low':
            i[1]==3
    return data

def data_process_market_cap_output(data):
    for i in data:
        if i[1]==1:
            i[1]='High'
        if i[1]==2:
            i[1]='Mid'
        if i[1]==3:
            i[1]=='Low'

    return data


def list_to_dict(data):

    keys=['NAME','MCAP','Q','BUYP','MPRICE']
    crypto_dictonary_list=[]
    
    for x in data:
        for y in x:
            print(y)
        
            if check_numerical(y)==True:
                x[x.index(y)]=float(y)
            
        crypto_dictionary_sub= dict(zip(keys, x))
        crypto_dictonary_list.append(crypto_dictionary_sub)
        print(crypto_dictonary_list)

    return crypto_dictonary_list

def dict_to_list(data):
    main_list=[]
    for i in data:
        sub_list=list(i.values())
        main_list.append(sub_list)
    
    return main_list
        


def get_market_cap(element):
    return element['MCAP']

def get_market_price(element):
    return element['MPRICE']

def get_buy_in_price(element):
    return element['BUYP']

def get_quantity(element):
    return element['Q']


#FIRST TO BE CALLED DUE TO RAW DATA (UNPROCESSED LIST)
def displaycrypto_raw(data):
    from tabulate import tabulate  
    #import texttable package as texttable enables a cell-like structure in which each data is stored and is similar to CSV files.
    import texttable as tt 
    tb = tt.Texttable() 
   
    for i in data:
        i.remove(i[5])
   
    headers = ["Name", "Market Cap", "Quantity", "Buy Price", "Market Price"]
    info = data[0:] #start reading from the left side  
    print(tabulate(info, headers=headers, tablefmt="fancy_grid", showindex = "always"))
    
    
    #other tableformats can be jira, textile, html
    #showindex = "always" is to add index

#TO SHOW ORDERED,PROCESSED LIST
def displaycrypto(data):
    from tabulate import tabulate  
    #import texttable package as texttable enables a cell-like structure in which each data is stored and is similar to CSV files.
    import texttable as tt 
    tb = tt.Texttable() 

   
    headers = ["Name", "Market Cap", "Quantity", "Buy Price", "Market Price"]
    info = data[0:] #start reading from the left side  
    print(tabulate(info, headers=headers, tablefmt="fancy_grid", showindex = "always"))
    
    
    #other tableformats can be jira, textile, html
    #showindex = "always" is to add index


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










      