import yfinance as yf
import pandas as pd

# List of company symbols with proper formatting
symbols = [
    "MSFT", "AAPL", "AMZN", "NVDA", "GOOGL", 
    "META", "GOOG", "BRK-B", "TSLA", "UNH"
]

# Download monthly adjusted close prices for the last 100 months
start_date = "2015-01-01"  # Adjust based on the required timeline
end_date = "2024-12-01"

# Download data for all stocks
stock_data = yf.download(symbols, start=start_date, end=end_date, interval="1mo")['Adj Close']

# Download market data (e.g., S&P 500)
market_symbol = "^GSPC"  # S&P 500 index
market_data = yf.download(market_symbol, start=start_date, end=end_date, interval="1mo")['Adj Close']

# Merge and clean the data
merged_data = stock_data.copy()
merged_data['Market'] = market_data
merged_data.dropna(inplace=True)  # Drop rows with missing values

# Save the data to an Excel file
output_path = r"C:\Users\brian\Downloads\stock_data21.xlsx"
with pd.ExcelWriter(output_path) as writer:
    merged_data.to_excel(writer, sheet_name='Stock Data')

# Display a summary
print(f"Data downloaded successfully and saved to {output_path}. Here's a preview:")
print(merged_data.head())
