#Subprogram to display crypto

from tabulate import tabulate
import texttable as tt
tb = tt.Texttable()


def displaycrypto(data):


    headers = data[0]
    info = data[0:]
    print(tabulate(info, headers=["Name", "Market_Cap", "Quantity", "Buy_Price", "Market_Price"], tablefmt="fancy_grid", showindex = "always"))
