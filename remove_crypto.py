 #remove cryptocurrency

def display_crypto_options():

    print("-"*100)
    print("")
    print("")
    print("-"*40)


def processdata(data):
    
    count=-1
    for i in data:
        count+=1
        print(f'{count}-\t{i[0]}') #format the output
    
    return count



def removecrypto(data):

    
    display_crypto_options()
    #put a function here to process AND SHOW THE DATA
     
    while (True):
        try:
            count=processdata(data)  
            user_input=input(f"Enter 0 to {count}, press e or E to exit: ")
            

            if user_input == "e" or user_input == "E":
                print("Exiting to menu...")
                break
            index = int(user_input)
            if index<0 or index>count:
                raise ValueError

            
            
        except ValueError:
            print(f"Enter 0 to {count}")
        else:
             
            del data[index]#This deletes the entire element, will not leave it blank!
            break
        
