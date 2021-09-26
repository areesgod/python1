import requests
import json
#Getting data from requests library 
r = requests.get(
    "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&sparkline=false",
    headers = {"accept": "application/json"})
#Sorting list of coins in descending order(Market cap)
def listofcoins(n):
    i = 0
    while i < n:
        packages_json = r.json()
        package_name = packages_json[i]['name']
        package_market = packages_json[i]['market_cap']
        #Printing list of coins
        print(i+1 ,")",package_name,",market cap = ",package_market)
        i += 1
