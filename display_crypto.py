#Subprogram to display crypto
def displaycrypto(data):
    from tabulate import tabulate
    import texttable as tt
    tb = tt.Texttable()
    headers = ["Name", "Market_Cap", "Quantity", "Buy_Price", "Market_Price"]
    info = data[0:]
    print(tabulate(info, headers=headers, tablefmt="fancy_grid", showindex = "always"))
