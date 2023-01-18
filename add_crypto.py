#add crypto currency
#start->cryptocheck()->If not loop back to start
#start->crpyotcheck() pass-> move onto input validation

def addcrypto(data):
    
        

    #define new parameters
    new_crypto=input('Enter Cryptocurrency name:\t')
    addon_market_cap=add_market_cap()
    
    new_quantity=input('enter quantity of crypto bought=\t')
    new_buy_in=input('enter buy in price of crypto=\t')
    new_market_price=input('Enter market price crpyto=\t')

    #time to combine these to be written into a file

    add_data=[new_crypto,new_market_cap,new_quantity,new_buy_in,new_market_price]
    print(add_data)
    #data.append(add_data)

    

def add_market_cap():
    
    try:
        new_market_cap=int(input('Enter market cap of crypto'))
    except (TypeError):
        raise AssertionError('Input variables should be integers try again')
    else:
        market_cap=str(new_market_cap)
        state=1
        return market_cap,state

