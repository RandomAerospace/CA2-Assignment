#This is the main file

from Function_1 import *
#imports all functions from Function_1

if __name__=="__main__":
    startingscreen()
    readfile() #Initialises program by reading crypto dataset   
    while(True):
        startingscreen()
        readfile() #Initialises program by reading crypto dataset


        input=input('select an option:\t')

        if input=='E' or input=='e':
            exitprog()
