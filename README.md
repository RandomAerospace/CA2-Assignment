# CA2 Assignment
 python assignment for Programming fundamentals

Program strcuture:
Main.py(Main file)

subfiles:
start_end.py(Function for showing start screen and Decoding, endcoding files)
display_crypto.py(Function for displaying crypto in a table and sorting them according to user inputted parameters)
add_crypto.py(Function for adding cryptocurrency and it's data manually or automatically)
ammend_crypto.py(ammending existing data)
cryptoportfoilio_statement.py(Shows cryptoportfolio statement in a table)

backend files which have functions that may be referenced by sub files:
live_data.py



#####################################################################

Base requirement functions done by Wai Phyo: Ammend and Add Crypto

New functions by Wai Phyo:

1.General UI improvements in add_crypto.py
   >User's input will be validated for every input. Making it more convenient for the user and to reduce any errors that will be keyed.
2.Live data (found in live_data.py)
   >All cryptocurrencies data will be updated upon launch.(main.py)
   >The user can chose whether they want their portfolio to be updated with the latest market data(Market cap and market price) in add_crypto.py.
   >Additionaly, if no coin has been found by the search function, the user can still manually enter cryptocurrency data.

   >This is "back end" code that has been made so that it can be referenced in multiple funcitions.
   >It uses 2 APIs, YahooFinance and Coinmarketcap(CMC). Yahoo finance searches for a crypto ticker when given a name. CMC takes that ticker and searches the livedata in it's dataset. CMC is used because they have a much wider range of cryptocurrencies avaiable as the barrier to entry for being listed on CMC is much lower than say, Binance, which is an exchange.

Limitations:
While all efforts have been put into ensuring input validation works, the current version of the program can only validate Floats, Integers, Strings but not fractions(3/4, 1/2 etc..).
   

#####################################################################

Base requirement functions done by Terrence: 
