#This is the main file
#List [name,market_cap,quantity,buy_price,market_price]


from Function_1 import startingscreen
from Function_1 import readfile
from Function_1 import exitprog

if __name__=="__main__":
    startingscreen()
    readfile() #Initialises program by reading crypto dataset   
    while(True):
        startingscreen()
        readfile() #Initialises program by reading crypto dataset


        input=input('select an option:\t')

        if input=='E' or input=='e':
            exitprog()
