import streamlit as st
import requests

# Get list of cryptocurrencies from CoinGecko API
url = 'https://api.coingecko.com/api/v3/coins/list?per_page=100'
response = requests.get(url).json()
cryptocurrencies = response['data']

# Define input fields for user selection
initial_value = st.number_input('Initial Investment Value', min_value=1)
target_coin = st.selectbox('Select Cryptocurrency', cryptocurrencies)
target_date = st.date_input('Investment Date')

# Calculate actual price and hypothetical returns
coin_symbol = target_coin['symbol']

# Get actual price
url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin_symbol}&vs_currencies=usd'
response = requests.get(url).json()
actual_price = response[coin_symbol]['usd']

# Get historical price on target date
url = f'https://api.coingecko.com/api/v3/coins/{coin_symbol}/history?date={target_date}&localization=false'
response = requests.get(url).json()

old_price = response['market_data']['current_price']['usd']

amount = initial_value / old_price
hypothetical_return = amount * actual_price

# Display results
if st.button('Calculate Returns'):
    st.subheader(f'Hypothetical Returns for Investing ${initial_value} in {target_coin} on {target_date}')
    st.text(f'Current Price: ${actual_price}')
    st.text(f'Investment Value: ${initial_value}')
    st.text(f'Hypothetical Return: ${hypothetical_return}')
