#This is the main file

from Function_1 import *
#imports all functions from Function_1

if __name__=="__main__":
    startingscreen()
    data=readfile() #Initialises program by reading crypto dataset   
    while(True):
        try:
            input=input('select an option:\t')

            if input=='E' or input=='e':
                exitprog()
            elif input=='1':
                print('Display Cryptocurrency')
                displaycrypto(data)
            elif input=='2':
                print('Add Crytpcurrency')
            elif input=='3':
                print('Amend CryptoCurrency')
            elif input=='4':
                print('Remove Cryptocurrency')
            else:
                raise ValueError()
            
        except ValueError:
            print('oops wrong value')
        finally:
            del input