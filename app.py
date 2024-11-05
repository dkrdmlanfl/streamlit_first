import streamlit as st
st.title('😍My First Streamlit App 😍')

st.header('이게 되네~!>~>!~>!~>!>~!>>!~>>~~>~~>~>~>~>~>~>~>😍😍😍😍')

import yfinance as yf
import os
try:
    import yfinance as yf
except ModuleNotFoundError:
    os.system("pip install yfinance")
    import yfinance as yf

# yfinance를 이용한 데이터 처리 코드 작성
ticker = yf.Ticker("AAPL")
data = ticker.history(period="1y")
st.write(data)