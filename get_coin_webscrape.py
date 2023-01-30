#Get coin price and data
# https://gist.github.com/4f77616973/bd7fc6ed95e6abacafa55084867c44c3
# https://gist.github.com/bruhbruhroblox/dd9d981c8c37983f61e423a45085e063


import yfinance as yf
import requests 
import time


#Get ticker, can only be done by webscraping!
def getTicker(company_name):
    yfinance = "https://query2.finance.yahoo.com/v1/finance/search"
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    params = {"q": company_name, "quotes_count": 1, "country": "United States"}

    res = requests.get(url=yfinance, params=params, headers={'User-Agent': user_agent})
    data = res.json()
    
    company_code = data['quotes'][0]['symbol']
    print(company_code)
    return company_code

def getPrice(ticker):
    coin=yf.Ticker(ticker)
    print(coin.info)

'''    
def get_crypto_data(crypto_name):
    api_key = 'your_api_key'
    url = f'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info?symbol={crypto_name}&CMC_PRO_API_KEY={api_key}'
    response = requests.get(url)
    return response.json()


crypto_name = input('Enter cryptocurrency name: ')
crypto_data = get_crypto_data(crypto_name)
print(crypto_data)
'''

if __name__=="__main__":
    company_name='Bitcoin'
    ticker=getTicker(company_name)
    getPrice(ticker)