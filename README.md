# binance_python
This is a module to use the Binance Exchange API with python. Any questions about the API check out the official documentation at https://github.com/binance-exchange/binance-official-api-docs/blob/master/rest-api.md.

## Get starting

It is recommended to touch a `key.py` that contains your Binance credentials as follows:
```
apikey = 'PASTE_YOUR_API_KEY_HERE'
secret = 'PASTE_YOUR_SECRET_HERE'
```

Importing the Binance class in your code:
```
from binance_api import binance
import key
```

### Client
The 'binance' class is the object that connects you to Binance's server as a client. Its initial parameters are your credentials in exchange: `apikey` and `secret`.

First of all make the following client assignment:
```
client = binance(key.apikey, key.secret)
```

Any method is called following the format:
```
client.NAME_OF_THE_METHOD()
```

From now on we have all the methods described, exemplified, and ordered as the summary:
- [Public HTTP methos](#public-http-methods)
  - [Ping](#ping)
  - [Server time](#server time)
  - [Exchange info](#exchange-info)
  - [Last price](#last-price)
  - [All last prices](#all-last-prices)
  - [Order book](#order-book)
- [Private HTTP methos](#private-http-methods)
  - [Book ticker](#book-ticker)
  - [Account info](#account-info)
  - [Account balances](#account-balances)
  - [Maker and taker commissions](#maker-and-taker-comissions)
  - [Order status](#order-status)
- [DONATE](#donate)

## Public HTTP methods
These methods work without signature, i.e. the Binance credentials are NOT mandatory.
* The base endpoint is: https://api.binance.com/api/v1
* Endpoint returns JSON object.
* All methods can return either JSON object, or array, or float.
* Request types: `GET`.

### Ping
Test connectivity to the REST API.

Example:
```
client.ping()
```

### Server time
Test connectivity to the REST API and get the current server time.

Example:
```
client.serverTime()
```

### Exchange info
Current exchange trading rules and symbol information.

Example:
```
client.eInfo()
```

### Last price
The latest price for a symbol or symbols.

Parameter | Mandatory
--------- | ---------
symbol | Yes
* Each `symbol` in Binance is written in capital letters as `ASSETCURRENCY`. For instance `LTCBTC`, `BTC` is used as currency to buy a given asset, `LTC`.

Example:
```
client.rPrice('LTCBTC')
```

### All last prices
Returns the order book for a given market, as well as a sequence number used by websockets for synchronization of book updates and an indicator specifying whether the market is frozen.

Example:
```
client.rAllPrices()
```

### Order book
Returns the order book for a given market.

Parameter | Mandatory
--------- | ---------
symbol | Yes
depth | No
field | No
* Each `symbol` in Binance is written in capital letters as `ASSETCURRENCY`. For instance `LTCBTC`, `BTC` is used as currency to buy a given asset, `LTC`.
* `depth` means the amount of `asks` and `bids` in response. Default 100; max 5000. Valid depths:[5, 10, 20, 50, 100, 500, 1000, 5000]
* `field` can be filled with `lastUpdatedId`, `asks`, and `bids`.

Example:
```
client.rOrderBook('LTCBTC', 10, 'asks')
```

## Private HTTP methods
These methods need signature, i.e. the Binance credentials are mandatory.
* The base endpoint is: https://api.binance.com/api/v3
* Endpoint returns JSON object.
* All methods can return either JSON object, or array.
* Request types: `GET`, `POST`, `DELETE`, and `PUT`.

### Book ticker
Best price and quantity on the order book for a symbol or symbols.

Parameter | Mandatory
--------- | ---------
symbol | No
field | No
* Each `symbol` in Binance is written in capital letters as `ASSETCURRENCY`. For instance `LTCBTC`, `BTC` is used as currency to buy a given asset, `LTC`.
* If the symbol is not sent, bookTickers for all symbols will be returned in an array.
* `field` can be filled with `symbol`, `bidPrice`, `bidQty`, `askPrice`, and `askQty`.

Example:
```
client.bookTicker('LTCBTC','askPrice')
```

### Account info
Get current account information.

Parameter | Mandatory
--------- | ---------
field | No
* `field` can be filled with `balances`, `makerCommission`, `takerCommission`, `buyerCommission`, `sellerCommission`, `canTrade`, `canWithdraw`, `canDeposit`, `updateTime`, and `accountType`.

Example:
```
client.aInfo(`takerCommission`)
```

### Account balances
Returns all of your balances.

Parameter | Mandatory
--------- | ---------
asset | No
status | No
* `asset` is a given currency symbol, e.g. decred is named as `DCR`
* `status` can be filled with `asset`, `free`, and `locked`.

Example:
```
client.rBalances('DCR')
```

### Maker and taker commissions
Returns taker/maker commission in percentage. For instance, if commission is of 0.1% the value exhibited is 0.001.

Examples:
```
client.rTaker()
```
```
client.rMaker()
```

### Order status
Coming soon.

## DONATE
* Bitcoin (BTC): bc1qe49xvnvgp2qey833ut3qgdv2nltg2xhnv2p6tl
* Decred (DCR): DsWrvibjbh8x8RWdH3CSnsEmD52mi6WxvR6
* DASH: XryxxDNdykosJX5MkNLw9Q5rBVPkNHjmDS
