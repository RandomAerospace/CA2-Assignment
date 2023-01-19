from pyfiglet import Figlet

def startingscreen():
    print(50*'-')
    
    f = Figlet(font='slant')
    print(f.renderText('Crypto checker.exe'))
    print('\tClass 02')
    print('\t1.Kim')
    print('\t2.Chee')
    print(50*'-')
    print('\t Cryptocurrency portfoilio application main menu')
    print(50*'-')

    print('1.Display Crypto currency')
    print('2.Add cryptocurrency')
    print('3.Ammend Crypto currency')
    print('4.Remove Cryptocurrency')
    print('5.Crpyot Portfoilio statement')
    print('E.Exit menu')

def midscreen():

    
    
    print(50*'-')
    print('\t Cryptocurrency portfoilio application main menu')
    print(50*'-')

    print('1.Display Crypto currency')
    print('2.Add cryptocurrency')
    print('3.Ammend Crypto currency')
    print('4.Remove Cryptocurrency')
    print('5.Crpyot Portfoilio statement')
    print('E.Exit menu')




def readfile():
    with open('dataset.csv','r') as file:
    
        data=file.readlines()
        #print(data) # ['Ivy,29,30\n', 'Elisa,5,6\n', 'Spencer,14,15\n', 'Sandy,22,23']

        #ignores headers
        data=data[1:]
        #Processed data which will be used by program
        crypto_dataset=[]

        for i in data:
            str=i.strip() #turns entire list into a string for splitting'
            name_score=str.split(',')
            crypto_dataset.append(name_score)
            

        print(crypto_dataset)
        return crypto_dataset
        #returns the processed dataset

def encodefile(data):
    with open('dataset.csv','w') as file:
        headers=['Name','Market_cap','Quantity','Buy_price','Market_price']
        data.insert(0,headers)
        for i in data:
            file.write(','.join(i) + '\n')

def exitprog():
    #add code to encode data
    print('exiting main menu')
    exit()


