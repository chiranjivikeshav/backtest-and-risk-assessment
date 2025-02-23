# Actual trade data for BTC-PERPETUAL
(Invoke-WebRequest -Uri "https://www.deribit.com/api/v2/public/get_tradingview_chart_data?instrument_name=BTC-PERPETUAL&resolution=1&start_timestamp=1695000000000&end_timestamp=1705000000000" -Method Get).Content | Out-File "deribit_data.json" 
# Test trade data for BTC-PERPETUAL
(Invoke-WebRequest -Uri "https://test.deribit.com/api/v2/public/get_tradingview_chart_data?instrument_name=BTC-PERPETUAL&resolution=1&start_timestamp=1695000000000&end_timestamp=1705000000000" -Method Get).Content | Out-File "train_deribit_data.json"
