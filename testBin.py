from binanceAPI import binance
import keys

api = keys.binance_apikey
secret = keys.binance_secret

client = binance(api, secret)
# print(client)

#public methods
print(client.ping())
# print(client.serverTime())
# print(client.eInfo())
# print(client.rPrice('LTCBTC'))
# print(client.rAllPrices())
print(client.rOrderBook('LTCBTC',10,'asks'))
# print(client.bookTicker('LTCBTC','askPrice'))
# print(client.aInfo('balances'))
print(client.rBalances('DASH','asset'))
print(client.testOrder('LTCBTC','BUY','MARKET',0.1))
# print(client.marketBuy('LTCBTC','BUY','MARKET',0.1))
# print(client.marketBuy('LTCBTC','BUY','MARKET',0.1))
# print(client.newOrder('LTCBTC','BUY','MARKET',10))
# print(client.orderStatus('LTCBTC'))
# print(client.openOrders('LTCBTC'))
# print(client.cancelOrder())

#private methods
