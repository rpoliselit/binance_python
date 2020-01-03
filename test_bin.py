from binance_api import binance
import time
import keys
api = keys.binance_apikey
secret = keys.binance_secret

client = binance(api, secret)
# print(client)

now = int(time.time() * 1000)
month_ago = now - 60*60*24 * 31 * 1000
#public methods
print(client.ping())
# print(client.serverTime())
# print(client.rPrice('LTCBTC'))
# print(client.rAllPrices())
# print(client.rOrderBook('LTCBTC',10,'asks'))
# print(client.rTaker())
# print(client.rMaker())
print(len(client.rKlineData('LTCBTC','1M')))
print(client.rKlineData('LTCBTC','1M',start=month_ago,end=now))
# print(client.bookTicker('LTCBTC','askPrice'))
# print(client.aInfo('balances'))
# print(client.rBalances('TUSD'))
# print(client.rBalances('USDT'))
# print(client.testOrder('LTCBTC','BUY','MARKET',0.1))
# print(client.marketBuy('LTCBTC','BUY','MARKET',0.1))
# print(client.marketBuy('LTCBTC','BUY','MARKET',0.1))
# print(client.newOrder('LTCBTC','BUY','MARKET',10))
# print(client.orderStatus('LTCBTC'))
# print(client.openOrders('LTCBTC'))
# print(client.cancelOrder())

#private methods
