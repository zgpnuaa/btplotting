import ccxt

exchange = ccxt.binance(config={
    'apiKey': 'CRdqW2S3T5n6WCGor6mirN1J8scS5TJIeqyMF1h5g8oKc9gb6B01hpeL4FLrOc9K',
    'secret': 'QoRbjRtl4Emr0jzpUfRPGNGbhhMfs1h92Q0LKpXDeWWXkW1v5nkUMH7pZnRWmlnJ',
    'enableRateLimit': True,
    'timeout':100000,
    'requests_trust_env':True,
    'options': {
#             'defaultType': 'spot'
            'adjustForTimeDifference':True,
        }
})  # 使用Binance交易所，你也可以选择其他交易所
exchange.load_markets()