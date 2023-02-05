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
    print("press E to Exit to Menu")
    
    run_state=True

    while(run_state==True):
        sort_options = input("Choose options to sort: ")
        
        
        try:

            
                
            if sort_options.upper()=='E':
                return 0
                run_state=False   
        
            if int(sort_options)<0 or int(sort_options)>4:
                raise ValueError()

            elif sort_options == '1': #market cap
                sort_order=int(input('Increasing order:1  Decreasing order:2 \t'))
                if sort_order<1 or sort_order>2:
                    raise ValueError()
                

                elif sort_order=='1':
                    #key=method which is a function that is defined below
                    #print(data)
                    #Returns a list of dictionaries
                    #[{'NAME': 'Bitcoin', 'MCAP': 1.0, 'Q': 15.0, 'BUYP': 38000.0, 'MPRICE': 23378.66},
                    #{'NAME': 'Ethereum', 'MCAP': 1.0, 'Q': 90.0, 'BUYP': 4200.0, 'MPRICE': 1662.19}, 
                    #{'NAME': 'Solana', 'MCAP': 2.0, 'Q': 60.0, 'BUYP': 260.0, 'MPRICE': 24.57},
                    #{'NAME': 'Decentraland', 'MCAP': 2.0, 'Q': 30000.0, 'BUYP': 1.5, 'MPRICE': 0.78}, 
                    #{'NAME': 'The Sandbox', 'MCAP': 2.0, 'Q': 25000.0, 'BUYP': 2.0, 'MPRICE': 0.76}, 
                    #{'NAME': 'Dogecoin', 'MCAP': 1.0, 'Q': 55000.0, 'BUYP': 0.4, 'MPRICE': 0.01}]
                    
                    #key=method which is a function that is defined below which sorts a dictionaries with respect to their keys.
                    data.sort(key=get_market_cap)
                
                elif sort_order=='2':

                    data.sort(key=get_market_cap,reverse=True)
                
                #turn back dictionary back to a list
                data_sorted=dict_to_list(data)

                #turn 1,2,3 back to high mid low for data presentation.
                data_output=data_process_market_cap_output(data_sorted)
                        
                return data_output
                break
                        

            elif sort_options == '2': #quantity bought, this needs addiitonal processing for numbers
                sort_order=int(input('Increasing order:1  Decreasing order:2 \t'))
                if sort_order<1 or sort_order>2:
                    raise ValueError()

                elif sort_order==1:
                    
                    data.sort(key=get_quantity)
                    
                elif sort_order==2:
                        
                    data.sort(key=get_quantity,reverse=True)
                    
                data_sorted=dict_to_list(data)
                data_output=data_process_market_cap_output(data_sorted)
                        
                return data_output
                break

            elif sort_options == '3': #buy price
                sort_order=int(input('Increasing order:1  Decreasing order:2 \t'))
                if sort_order<1 or sort_order>2:
                    raise ValueError()
                

                elif sort_order==1:
                    
                        data.sort(key=get_buy_in_price)
                    
                elif sort_order==2:
                        
                    data.sort(key=get_buy_in_price,reverse=True)
                    
                data_sorted=dict_to_list(data)
                data_output=data_process_market_cap_output(data_sorted)
                        
                return data_output
                break
                
            elif sort_options =='4':
                sort_order=int(input('Increasing order:1  Decreasing order:2 \t'))
                if sort_order<1 or sort_order>2:
                    raise ValueError()
                
               

                elif sort_order==1:
                    
                    data.sort(key=get_market_price)
                    
                elif sort_order==2:
                        
                    data.sort(key=get_market_price,reverse=True)
                    
                data_sorted=dict_to_list(data)
                data_output=data_process_market_cap_output(data_sorted)
                        
                return data_output
                break
        
        except ValueError:
            print('please enter an appropriate option')
        
   
#change to integers for the sake of sorting
def data_process_market_cap(data):
    for i in data:
        if i[1]=='High':
            i[1]=1
        if i[1]=='Mid':
            i[1]=2
        if i[1]=='Low':
            i[1]==3
    return data

#change back to original for presentation of data
def data_process_market_cap_output(data):
    for i in data:
        if i[1]==1:
            i[1]='High'
        if i[1]==2:
            i[1]='Mid'
        if i[1]==3:
            i[1]=='Low'

    return data

#this functions turns the list into a dictionary for sorting.
#additionally, this function turns strings into floats for the sake of sorting
def list_to_dict(data):

    keys=['NAME','MCAP','Q','BUYP','MPRICE']
    crypto_dictonary_list=[]
    
    for x in data:
        for y in x:
            
            
            if check_numerical(y)==True:
                #integer AND float, y will be turned into a floating point number
                #There is no need to revert back to string as this function does not return a value or save to a file.
                x[x.index(y)]=float(y)
            
        crypto_dictionary_sub= dict(zip(keys, x))
        crypto_dictonary_list.append(crypto_dictionary_sub)
        

    return crypto_dictonary_list

def dict_to_list(data):
    main_list=[]
    for i in data:
        sub_list=list(i.values())
        main_list.append(sub_list)
    
    return main_list
        

#sorting methods for sort(key=)
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
    count=1
    for i in data:
        i.remove(i[5])
        i.insert(0,count)
        count+=1
   
    
    headers = ['No',"Name", "Market Cap", "Quantity", "Buy Price", "Market Price"]
    info = data[:] #start reading from the left side  
    print(tabulate(info, headers=headers, tablefmt="fancy_grid",numalign="right"))
    for i in data:
        i.remove(i[0])
  
    
    #other tableformats can be jira, textile, html
    #showindex = "always" is to add index

#TO SHOW ORDERED,PROCESSED LIST
def displaycrypto(data):
    from tabulate import tabulate  
    #import texttable package as texttable enables a cell-like structure in which each data is stored and is similar to CSV files.
    import texttable as tt 
    tb = tt.Texttable() 
    count=1
    for i in data:
        i.insert(0,count)
        count+=1
        
   
    headers = ['No.',"Name", "Market Cap", "Quantity", "Buy Price", "Market Price"]
    info = data[:] #start reading from the left side  
    print(tabulate(info, headers=headers, tablefmt="fancy_grid",numalign="right"))
    for i in data:
        i.remove(i[0])
       
    
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










      