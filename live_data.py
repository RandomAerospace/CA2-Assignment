#Get coin price and data
# https://gist.github.com/4f77616973/bd7fc6ed95e6abacafa55084867c44c3
# https://gist.github.com/bruhbruhroblox/dd9d981c8c37983f61e423a45085e063
# market cap categories: https://www.statista.com/statistics/1269013/biggest-crypto-per-category-worldwide/#:~:text=High%20cap%3A%20a%20market%20cap,than%20one%20billion%20U.S.%20dollars. 

#High cap: a market cap of 10 billion U.S. dollars or more;
#Mid cap: a market cap between one billion and 10 billion U.S. dollars;
#Low cap: a market cap of less than one billion U.S. dollars.


#Program flow#
#1.Get ticker,which is the unique identifier, for example Bitcoin(BTC) can be differentiated from harrypotterobamasonic10inu(BITCOIN)
#2.Get market data
#3.Feed back market data to main loop

import requests 
import time


#Get ticker, can only be done by webscraping! Yahoo API is no longer working but can use a static site to search names and tickers
def getTicker(crypto):
    yfinance = "https://query2.finance.yahoo.com/v1/finance/search"

    
    #The User-Agent header is used by the server to identify the client software and version, operating system, and device type. 
    # This information can be used to optimize the response or return a different version of the content if necessary.

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'

    '''

    The params dictionary has three key-value pairs:

    "q": company_name - This parameter represents the company name that is being searched for and its value is set to the company_name argument passed to the getTicker function.

    "quotes_count": 1 - This parameter represents the number of quotes to return in the response and its value is set to 1.

    "country": "United States" - This parameter represents the country to search for quotes and its value is set to "United States".

    These are paramters for Yahoo finance API 
    '''

    params = {"q": crypto, "quotes_count": 1, "country": "United States"}

    #HTTP headers are key-value pairs that provide additional information about the request to the server.
    #In this code, the headers dictionary contains a single header User-Agent that provides information about the client that is sending the request
    res = requests.get(url=yfinance, params=params, headers={'User-Agent': user_agent})

    #data type is dictionary
    data = res.json()
    try:

        ticker= data['quotes'][0]['symbol']
    except IndexError:
        print("Crypto currency could not be found")
        return False
    #quotes': [{'exchange': 'CCC', 'shortname': 'Avalanche USD', 'quoteType': 'CRYPTOCURRENCY', 
    #'symbol': 'AVAX-USD', 'index': 'quotes', 'score': 21571.0, 'typeDisp': 'Cryptocurrency', 
    #'exchDisp': 'CCC', 'isYahooFinance': True}, {'exchange': 'CCC', 'shortname': 'Avalanche CAD', 'quoteType': 'CRYPTOCURRENCY',
    #'symbol': 'AVAX-CAD', 'index': 'quotes', 'score': 20137.0,
    return ticker



  
def get_crypto_data(crypto_name):
    api_key = 'f8dd4eb7-ca48-4b96-8c6b-e2490a7a2e18' #wai phyo key
    #api_key='2413d5cd-943f-46bd-85bb-ede6e61be260' #terence key
    url = f'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest?symbol={crypto_name}&CMC_PRO_API_KEY={api_key}'
    response = requests.get(url)
    data= response.json()
    
    
    #note:data returned is in string
    price=data['data'][crypto_name][0]['quote']['USD']['price']
    market_price="{:.2f}".format(price)

    #maybe implement a classfication algo here to identify high and low
    market_cap=data['data'][crypto_name][0]['quote']['USD']['market_cap']

    #market cap classification
    if market_cap>10000000000:
        market_cap_class='High'
    elif market_cap>1000000000 and market_cap<10000000000:
        market_cap_class='Mid'
    elif market_cap<1000000000:
        market_cap='Low'

    return market_price,market_cap_class



#For use to autoupdate prices whenever program is started
def update_live_data(data):
    print('updating database...')
    
    for i in data:
        if i[5]=='1': #reads update state
            company_name=i[0]
            get_ticker=getTicker(company_name)
    
            #Remove the - in the string to get data
            ticker=[]
            for x in get_ticker:
            
                if x!='-':
                    ticker.append(str(x))
                else:
                    break

            ticker=''.join(ticker)
        

            #crypto_data=price,market_cap_class
            crypto_price,market_cap_class = get_crypto_data(ticker)
            i[1]=market_cap_class
            i[4]=str(crypto_price)
            data[data.index(i)]=i
            print('.')
        else:
            continue
    
    return data

#For use in manual operation
def add_live_data(crypto_ticker):
    
    
    
   
   #Remove the - in the string to get data
    ticker=[]
    for i in crypto_ticker:
        
        if i!='-':
            ticker.append(str(i))
        else:
            break

    ticker=''.join(ticker)
    

    market_price,market_cap_class=get_crypto_data(ticker)

    return market_price, market_cap_class


'''
Coin market cap API json dict:

{
'status': {'timestamp': '2023-01-30T07:43:35.609Z', 'error_code': 0, 'error_message': None, 'elapsed': 26, 'credit_count': 1, 'notice': None}, 
'data': 
        {'BTC':
            [
                {'id': 1, 'name': 'Bitcoin', 'symbol': 'BTC', 'slug': 'bitcoin', 'num_market_pairs': 9943, 'date_added': '2013-04-28T00:00:00.000Z', 
                'tags': [
                            {'slug': 'mineable', 'name': 'Mineable', 'category': 'OTHERS'}, {'slug': 'pow', 'name': 'PoW', 'category': 'ALGORITHM'}, 
{'slug': 'sha-256', 'name': 'SHA-256', 'category': 'ALGORITHM'}, {'slug': 'store-of-value', 'name': 'Store Of Value', 'category': 'CATEGORY'},
 {'slug': 'state-channel', 'name': 'State Channel', 'category': 'CATEGORY'}, {'slug': 'coinbase-ventures-portfolio', 'name': 'Coinbase Ventures Portfolio', 
 'category': 'CATEGORY'}, {'slug': 'three-arrows-capital-portfolio', 'name': 'Three Arrows Capital Portfolio', 'category': 'CATEGORY'},
  {'slug': 'polychain-capital-portfolio', 'name': 'Polychain Capital Portfolio', 'category': 'CATEGORY'}, {'slug': 
'binance-labs-portfolio', 'name': 'Binance Labs Portfolio', 'category': 'CATEGORY'},
 {'slug': 'blockchain-capital-portfolio', 'name': 'Blockchain Capital Portfolio', 'category': 'CATEGORY'},
  {'slug': 'boostvc-portfolio', 'name': 'BoostVC Portfolio', 'category': 'CATEGORY'},
   {'slug': 'cms-holdings-portfolio', 'name': 'CMS Holdings Portfolio', 'category': 'CATEGORY'},
    {'slug': 'dcg-portfolio', 'name': 'DCG Portfolio', 'category': 'CATEGORY'}, 
    {'slug': 'dragonfly-capital-portfolio', 'name': 'DragonFly Capital Portfolio', 'category': 'CATEGORY'}, 
    {'slug': 'electric-capital-portfolio', 'name': 'Electric Capital Portfolio', 'category': 'CATEGORY'}, 
    {'slug': 'fabric-ventures-portfolio', 'name': 'Fabric Ventures Portfolio', 'category': 'CATEGORY'}, 
    {'slug': 'framework-ventures-portfolio', 'name': 'Framework Ventures Portfolio', 'category': 'CATEGORY'}, 
    {'slug': 'galaxy-digital-portfolio', 'name': 'Galaxy Digital Portfolio', 'category': 'CATEGORY'}, 
    {'slug': 'huobi-capital-portfolio', 'name': 'Huobi Capital Portfolio', 'category': 'CATEGORY'}, 
    {'slug': 'alameda-research-portfolio', 'name': 'Alameda Research Portfolio', 'category': 'CATEGORY'}, 
    {'slug': 'a16z-portfolio', 'name': 'a16z Portfolio', 'category': 'CATEGORY'}, 
    {'slug': '1confirmation-portfolio', 'name': '1Confirmation Portfolio', 'category': 'CATEGORY'}, 
    {'slug': 'winklevoss-capital-portfolio', 'name': 'Winklevoss Capital Portfolio', 'category': 'CATEGORY'}, 
    {'slug': 'usv-portfolio', 'name': 'USV Portfolio', 'category': 'CATEGORY'}, 
    {'slug': 'placeholder-ventures-portfolio','name': 'Placeholder Ventures Portfolio', 'category': 'CATEGORY'}, 
    {'slug': 'pantera-capital-portfolio', 'name': 'Pantera Capital Portfolio', 'category': 'CATEGORY'}, 
    {'slug': 'multicoin-capital-portfolio', 'name': 'Multicoin Capital Portfolio', 'category': 'CATEGORY'}, 
    {'slug': 'paradigm-portfolio', 'name': 'Paradigm Portfolio', 'category': 'CATEGORY'}
    ]
    ,'max_supply': 21000000, 'circulating_supply': 19276812, 'total_supply': 19276812, 'is_active': 1, 'platform': None, 'cmc_rank': 1, 'is_fiat': 0, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'tvl_ratio': None, 'last_updated': '2023-01-30T07:42:00.000Z', 
    'quote':        {'USD':
                        {'price': 23659.014680229506, 'volume_24h': 25933055076.565052, 'volume_change_24h': 48.3009, 'percent_change_1h': -0.1345927, 'percent_change_24h': 1.94096157, 'percent_change_7d': 4.12809924, 'percent_change_30d': 42.84277837, 'percent_change_60d': 38.21966424, 'percent_change_90d': 14.93850151, 'market_cap': 456070378096.0243, 'market_cap_dominance': 42.5073, 'fully_diluted_market_cap': 496839308284.82, 'tvl': None, 'last_updated': '2023-01-30T07:42:00.000Z'
                        }
                    }
                }
            ]
        }
    }
'''