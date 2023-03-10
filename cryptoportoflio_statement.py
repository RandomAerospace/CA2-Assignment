#Crypto Portoflio statement

def cryptoportoflio_statement(data):
    from tabulate import tabulate #formats and prints the information using tabulate
    import texttable as tt 
    tb = tt.Texttable() #texttable is table for the data
    
    #Total_Invested = Quantity*Buy_In_Price
    #Invested_Portfolio_Size = Percentage_of_Total_Invested/ Sum_of_Total_Invested
    #Total_Current_Value = Quantity x Market_Price
    #Profit_Loss = Total_Current_Value – Total_Invested
    #Current_Portfolio_Size = Percentage_of_Total_Current_Value / Sum_of_Total_Current_Value
    
    headers = ['No.',"Name", "Quantity", "Buy In Price", "Market Price", "Total Invested", 
               "Invested Portfolio Size", "Total Current Value", "Profit/Loss", "Current Portfolio Size"]
    
    sum_of_total_invested = 0
    sum_of_total_current_value = 0
    sum_of_profit_loss = 0
    for i in range(len(data)):
        quantity = float(data[i][2]) # Quantity
        buy_in_price = float(data[i][3]) # Buy In Price
        market_price = float(data[i][4]) # Market Price
        total_invested = quantity*buy_in_price # Total Invested
        sum_of_total_invested += total_invested 
        total_current_value = quantity*market_price # Total Current Value
        sum_of_total_current_value += total_current_value
        

    info = []
    total_invested_sum=0
    total_current_value_sum=0
    profit_loss_sum=0
    count=0
    for i in range(len(data)):
        name = data[i][0] # Name
        quantity = float(data[i][2]) # Quantity
        buy_in_price = float(data[i][3]) # Buy In Price
        market_price = float(data[i][4]) # Market Price
        total_invested = quantity*buy_in_price # Total Invested
        invested_portfolio_size = str(round((total_invested/sum_of_total_invested)*100, 2)) + '%' # Invested Portfolio Size
        total_current_value = quantity*market_price # Total Current Value
        profit_loss = total_current_value-total_invested # Profit / Loss
        current_portfolio_size = str(round((total_current_value / sum_of_total_current_value)*100, 2)) + '%' # Current Portfolio Size

        total_invested_sum+=total_invested
        total_current_value_sum+=total_current_value
        profit_loss_sum+=profit_loss
        count+=1


        info.append([count,name, quantity, buy_in_price, market_price, total_invested, invested_portfolio_size, total_current_value, profit_loss,
                     current_portfolio_size, ])

    info.append(['','SUM',' '," " ,' ',total_invested_sum,'',total_current_value_sum,profit_loss_sum,''])    
    print(tabulate(info, headers=headers, tablefmt="fancy_grid"))
