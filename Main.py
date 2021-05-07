
import tkinter as tk
from tkinter import *
import yfinance as yf

root = tk.Tk()
ammount = 0.0
portfolio = float(0)
money_end = ammount
investement = []
transaction_cost = 0.075

def get_current_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return todays_data["Open"][0]

def buy(quantity, symbol):
    global portfolio, money_end
    price = float(get_current_price(symbol))
    tot_price = price * float(quantity)
    commission = tot_price * transaction_cost
    money_end -= (tot_price + commission)
    portfolio += float(quantity)
    if investement == [] :
        investement.append([symbol, tot_price])
    else:
        investement.append([symbol,investement[-1][1] + tot_price])
    Port["text"] = (f"Ammount = {money_end} \n" \
                   f"Portfolio = {portfolio}  \n" \
                   f"Recent Investement = {investement}\n" \
                   f"Commision Cost = {transaction_cost}   \n")
def sell(quantity, symbol):
    global portfolio, money_end
    price = get_current_price(symbol)
    sell_price = float(quantity) * price
    commission = sell_price * transaction_cost
    money_end += (sell_price - commission)
    portfolio -= float(quantity)
    investement.append([symbol, investement[-1][1] - sell_price])
    Port["text"] = (f"Ammount = {money_end} \n" \
                   f"Portfolio = {portfolio}  \n" \
                   f"Recent Investement = {investement}\n" \
                   f"Commision Cost = {transaction_cost}   \n")

def Save_ammount(x):
    global ammount, money_end, portfolio, investement, transaction_cost
    ammount += float(x)
    money_end = ammount
    print(x)
    Port["text"] = (f"Ammount = {money_end} \n" \
                   f"Portfolio = {portfolio}  \n" \
                   f"Recent Investement = {investement}\n" \
                   f"Commision Cost = {transaction_cost}   \n")





canvas = tk.Canvas(root, height = 700, width= 700, bg="#fbab81")
canvas.pack()
# portfolio section
Portfolio = tk.Frame(root, bg="#ffcdb3", bd = 5)
Portfolio.place(relwidth = 0.75, relheight = 0.10, relx = 0.15, rely= 0.15)
#text
var = StringVar()
Port = tk.Label(Portfolio, textvariable = var, bg="#ffcdb3", font=1)
Port.pack()
var.set("Choose a starting cash ammount")
#form for user
entry = tk.Entry(Portfolio, font=40, bg="#fbab81")
entry.place(relwidth = 0.65, relheight = 0.5, rely = 0.5, )
#button
saver = tk.Button(Portfolio, font = 20, text= "Save ammount", command=lambda : Save_ammount(entry.get()) )
saver.place(rely = 0.5, relx=0.66, relheight = 0.5, relwidth = 0.34)
### TEXT INFO PLACE ####
Info = tk.Frame(root, bg="#fbab81", bd = 5)
Info.place(relwidth = 0.75, relheight = 0.30, relx = 0.15, rely= 0.25)
Port = tk.Label(Info, bg="#fbab81", font=1)
Port.pack()

### Investement section
Investement = tk.Frame(root, bg="white")
Investement.place(relwidth = 0.5, relheight = 0.3, relx = 0.15, rely= 0.55)
#Input Form
Stock_name = tk.Entry(Investement, font=40, bg="#fbab81")
Stock_name.place(relwidth = 0.75, relheight = 0.15, rely = 0.05,  relx= 0.02)
Stock_name.insert(1, "Insert the Symbol of the stock")
Ammount_action = tk.Entry(Investement, font=40, bg="green")
Ammount_action.place(relwidth = 0.75, relheight = 0.15, rely = 0.25, relx= 0.02)
Ammount_action.insert(1, "Input ammount of shares to buy/sell")

#Buy button
Buy_button = tk.Button(Investement, text="Buy", padx =15,
                       pady = 10, fg ="white", bg="#fbab81", command=lambda : buy(Ammount_action.get(), Stock_name.get()))
Sell_button = tk.Button(Investement, text="Sell", padx =15,
                       pady = 10, fg ="white", bg="#fbab81", command=lambda : sell(Ammount_action.get(), Stock_name.get()))
Buy_button.place(rely = 0, relx = 0.78)
Sell_button.place(rely = 0.25, relx = 0.78)

root.mainloop()







