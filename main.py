#This is the main file#
#Group Name=Hotel

from start_end import *
#imports all functions from neccassary for start up of program
from display_crypto import *
#imports all functions for displaying crypto
from add_crypto import *
#imports all functions for adding crypto
from ammend_crypto import *
#imports all functions for ammending cryptocurrency
from remove_crypto import *
#imports all functions for removing cryptocurrency

'''
csv file will only be saved upon exit of program where the
list will be encoded to a csv file, this simplifies file read and file write
'''

if __name__=="__main__":
    startingscreen()
    data=readfile() #Initialises program by decoding crypto dataset csv file
    
    #In this while loop, the data variable is passed among the different functions
    #All functions that manipulate the data will have to return it.
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
                
                #for this function, you need to return the data list in the function
                data=addcrypto(data)
                #updated the list to have additional cryptocurrency
                
            elif input=='3':
                print('Amend CryptoCurrency')
                #for this function, you need to return the data list in the function
            elif input=='4':
                print('Remove Cryptocurrency')
                #for this function, you need to return the data list in the function
            else:
                raise ValueError()
            
        except ValueError:
            print('oops wrong value')
        except TypeError:
            print("You're supposed to enter an integer")
        
        finally:
            #encode data
            encodefile(data)
            del input