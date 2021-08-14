import streamlit as st
import yfinance as yf
import pandas as pd
import cufflinks as cf
import datetime

# App title
st.markdown('''
# Stock Price App
Stock price data for query companies are shown here.
''')
st.write('---')

# Sidebar
st.sidebar.subheader('Inputs')
start_date = st.sidebar.date_input("Start date", datetime.date(2019, 1, 1))
end_date = st.sidebar.date_input("End date", datetime.date(2021, 1, 31))

# Retrieving tickers data
ticker_list = pd.read_csv('https://raw.githubusercontent.com/rahulrachh/stock-web-app/master/data/stock_symbols.csv')
# tickerSymbol_user = st.sidebar.text_input('Give Input of Stock Symbol')
tickerSymbol = st.sidebar.selectbox('Stock ticker', ticker_list) # Select ticker symbol
tickerData = yf.Ticker(tickerSymbol) # Get ticker data
tickerDf = tickerData.history(period='1d', start=start_date, end=end_date) #get the historical prices for this ticker

tickerInfo = tickerData.info

# Ticker information
string_logo = '<img src=%s>' % tickerInfo['logo_url']
st.markdown(string_logo, unsafe_allow_html=True)

string_name = tickerInfo['longName']
st.header(f'**{string_name}**')

string_summary = tickerInfo['longBusinessSummary']
st.info(string_summary)

# Ticker data
st.header('**Ticker data**')
st.write(tickerDf)

# Bollinger bands
st.header('**Bollinger Bands**')
qf=cf.QuantFig(tickerDf,title='First Quant Figure',legend='top',name='GS')
qf.add_bollinger_bands()
fig = qf.iplot(asFigure=True)
st.plotly_chart(fig)

####
#st.write('---')
#st.write(tickerData.info)