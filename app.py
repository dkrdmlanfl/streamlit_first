import streamlit as st
st.title('😍My First Streamlit App 😍')

st.header('이게 되네~!>~>!~>!~>!>~!>>!~>>~~>~~>~>~>~>~>~>~>😍😍😍😍')

import yfinance as yf

ticker = yf.Ticker('AAPL')

data = ticker.history(period="1y")
print(data)
