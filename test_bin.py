from binance_api import binance
import keys
api = keys.binance_apikey
secret = keys.binance_secret

client = binance(api, secret)
# print(client)

#public methods
print(client.ping())
# print(client.serverTime())
symbols = client.eInfo()['symbols']
for k in symbols:
    if k['symbol'] == 'TUSDUSDT':
        for j in k['filters']:
            if j['filterType'] == 'LOT_SIZE':
                minQty = float(j['minQty'])
                maxQty = float(j['maxQty'])
                stepSize = float(j['stepSize'])
q = 126.65
print(f'{q} / {stepSize} == {q / stepSize}')
print(f'{q} // {stepSize} == {q // stepSize}')
print(f'{q} % {stepSize} == {(q - minQty) % stepSize}')
print(q - q % stepSize)
# print(client.rPrice('LTCBTC'))
# print(client.rAllPrices())
print(client.rOrderBook('LTCBTC',10,'asks'))
print(client.rTaker())
print(client.rMaker())
# print(client.bookTicker('LTCBTC','askPrice'))
# print(client.aInfo('balances'))
print(client.rBalances('TUSD'))
print(client.rBalances('USDT'))
print(client.testOrder('LTCBTC','BUY','MARKET',0.1))
# print(client.marketBuy('LTCBTC','BUY','MARKET',0.1))
# print(client.marketBuy('LTCBTC','BUY','MARKET',0.1))
# print(client.newOrder('LTCBTC','BUY','MARKET',10))
# print(client.orderStatus('LTCBTC'))
# print(client.openOrders('LTCBTC'))
# print(client.cancelOrder())

#private methods
