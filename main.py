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

class inputerror(Exception):
    """Raise for when the menu option is put in wrongly"""
    #this is done to define the exception for it to be asserted in the main program







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
                addcrypto(data)
                
                
           
       
            elif input=='3':
                print('Amend CryptoCurrency')
                #for this function, you need to return the data list in the function
            elif input=='4':
                print('Remove Cryptocurrency')
                removecrypto(data)
                #for this function, you need to return the data list in the function
            else:
                raise inputerror
            
        
        except inputerror:
             print('Please input the appropriate menu option')
        except ValueError:
            print('Please enter an integer')
        
        
        finally:
            startingscreen()
            del input
    #saves file IF AND ONLY IF PROGRAM EXITS LOOp
    encodefile(data)

