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
    
