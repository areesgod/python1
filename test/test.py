from src import listofcoins
import requests
import json
#Inputting number of coins
n = int(input("Enter the number of coins:"))
#Creating request from api and print coins
listofcoins(n)
