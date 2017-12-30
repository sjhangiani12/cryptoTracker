from pypoloniex import LoadPairs

data = LoadPairs()


LTC = data.getPair(market = 'USDT', coin = 'LTC')

LTCvalue = float(LTC.last) * 1.3178

LTCinvestment = 122.99 

LTCnet = LTCvalue - LTCinvestment

print 'Litecoin Net = %s ' %(LTCnet)




BTC = data.getPair(market = 'USDT', coin = 'BTC')

BTCvalue = float(BTC.last) * (0.021749 + 0.06901669)

BTCinvestment = 102.99 + 500.00

BTCnet = BTCvalue - BTCinvestment




print 'Bitcoin Net = %s ' %(BTCnet)

ETH = data.getPair(market = 'USDT', coin = 'ETH')

ETHvalue = float(ETH.last) * 0.25785 

ETHinvestment = 102.99

ETHnet = ETHvalue - ETHinvestment

print 'Ethereum Net = %s ' %(ETHnet)

totalNet = ETHnet + LTCnet + BTCnet

print 'Total Investment Net Return = %s' %(totalNet)