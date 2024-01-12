###
# This app calculates and displays the hypothetical returns on cryptocurrency investments over a specified period
###

import requests

value = int(input('initial value: '))
coin = input('cryptocoin: ')
date = input('date: ')

# get actual price
url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd'
response = requests.get(url).json()

actual_price = response[coin]['usd']

# get old price
url = f'https://api.coingecko.com/api/v3/coins/{coin}/history?date={date}&localization=false'
response = requests.get(url).json()

old_price = response['market_data']['current_price']['usd']

# presenting result
amount = value/old_price
print(f'If I invested ${value} in {coin} in {date}, now I would have ${amount*actual_price}!')

