#Subprogram to display crypto

def displaycrypto(data):
    from tabulate import tabulate  
    #import texttable package as texttable enables a cell-like structure in which each data is stored and is similar to CSV files.
    import texttable as tt 
    tb = tt.Texttable() 
    for i in data:
        i.remove(i[5])
    print(data)
    headers = ["Name", "Market Cap", "Quantity", "Buy Price", "Market Price"]
    info = data[0:] #start reading from the left side  
    print(tabulate(info, headers=headers, tablefmt="fancy_grid", showindex = "always"))
    
    
    #other tableformats can be jira, textile, html
    #showindex = "always" is to add index
    import csv 
    
    def sort_crypto_data(data, key):
        return sorted(data, key=lambda x: x[key])
    
    with open("dataset.csv", "r") as file:
        reader = csv.DictReader(file) 
        data = [row for row in reader] 
    #reads the data into a list of dictionaries, each dictionary represents a row in the csv
     
    sort_options = int(input("Choose options to sort: "))
    
    def display_sort_options():
        display_sort_options()
        print("1. Name")
        print("2. Market Cap")
        print("3. Quantity")
        print("4. Buy Price")
        print("5. Market Price")
        print("6. Exit to Menu")
    
    while(True):
        if sort_options == 1:
            sorted_data = sort_crypto_data(data, "Name") #sort by Name
            print("Sorted data by Name!")
            for item in sorted_data:
                print(f"{item['Name']}")
            # print(f"{item['symbol']}: {item['Name']}")

        elif sort_options == 2:
            sorted_data = sort_crypto_data(data, "Market Cap") #sort by Market Cap
            print("Sorted data by Market Cap!")
            for item in sorted_data:
                print(f"{item['Market Cap']}")

        elif sort_options == 3:
            sorted_data = sort_crypto_data(data, "Quantity") #sort by Quantity
            print("Sorted data by Quantity!")
            for item in sorted_data:
                print(f"{item['Quantity']}")

        elif sort_options == 4:
            sorted_data = sort_crypto_data(data, "Buy Price") #sort by Buy Price
            print("Sorted data by Buy Price!")
            for item in sorted_data:
                print(f"{item['Buy Price']}")
        
        elif sort_options == 5:
            sorted_data = sort_crypto_data(data, "Market Price") #sort by Market Price
            print("Sorted data by Market Price!")
            for item in sorted_data:
                print(f"{item['Market Price']}")
        
        elif sort_options == "e" or sort_options == "E":
            print("Exiting to menu...")
            break
            
        index = int(sort_options)
        if index<0 or index>5:
                raise ValueError