#This is the main file#
#Group Name=Hotel

#Internal libraries
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
from cryptoportoflio_statement import * 
#imports all functions for crypto portoflio statement
from live_data import *

'''
csv file will only be saved upon exit of program where the
list will be encoded to a csv file, this simplifies file read and file write
'''

class inputerror(Exception):
    """Raise for when the menu option is put in wrongly"""
    #this is done to define the exception for it to be asserted in the main program


if __name__=="__main__":
    data=readfile() #Initialises program by decoding crypto dataset csv file
    
    #update_live_data(data)
    startingscreen()
    
    #add in autoupdate function here
    main_run_state=0 #for the sake of this main loop, this makes sure that the mid program does NOT appear at the end.


    #In this while loop, the data variable is passed among the different functions
    #All functions that manipulate the data will have to return it.
    while(True):
        try:
            input=input('select an option:\t')
           

            if input=='E' or input=='e':
                main_run_state=1
                encodefile(data) #writes and saves all changes
                exitprog()
                
            elif input=='1':
                print('Display Cryptocurrency')
                data_for_display=data.copy()
                displaycrypto_raw(data_for_display)
                
                
                data_sorted=display_sort_options(data_for_display)
                if data_sorted==0:
                    continue
                else:
                    displaycrypto(data_sorted)
                
                #goes to finally step to clear shallow copies
                
                
            elif input=='2':
                print('Add Cryptocurrency')
                addcrypto(data)
                encodefile(data)

            elif input=='3':
                print('Amend Cryptocurrency')
                data,index=ammendcrypto_stage_one(data)
                if data==False and index==False:
                    continue
                else:
                    ammend_crypto_stage_two(data, index)
                    encodefile(data)
                #for this function, you need to return the data list in the function
            elif input=='4':
                print('Remove Cryptocurrency')
                removecrypto(data)
                encodefile(data)
                #for this function, you need to return the data list in the function
            elif input=='5':
                print('Crypto Portoflio statement')
                cryptoportoflio_statement(data)
                #for this function, you need to return the data list in the function
            else:
                raise inputerror
            
        
        except inputerror:
             print('Please input the appropriate menu option')
        
        
        
        finally:
            if main_run_state==0:
                midscreen()
            del input
            #can't find a way to make a deep copy without external libraries, only way for now.
            data=readfile()
    
    

