import streamlit as st
st.title('😍My First Streamlit App 😍')

st.header('이게 되네~!>~>!~>!~>!>~!>>!~>>~~>~~>~>~>~>~>~>~>😍😍😍😍')

import yfinance as yf


# 원하는 주식 종목 (예: 애플 AAPL)
ticker_symbol = 'AAPL'
ticker = yf.Ticker(ticker_symbol)

# 주식 데이터 (최근 1년 데이터, 일별)
data = ticker.history(period="1y")
print(data)
