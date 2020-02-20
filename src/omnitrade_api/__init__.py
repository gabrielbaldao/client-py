from client import Client
import json


cl = Client()
# print(type(cl))
# print(json.dumps(cl.get_public('/api/v2/markets')))
access_key = 'FUkESEYRJmO42MfqXcgJfm73GfIMw61qogExtcX7'

cl1 = Client({'access_key': access_key,'secret_key': '123456'})
# print(cl1.get('api/v2/markets', {'market': 'btcbrl','price': '10','side': 'buy','tonce': 123,'volume': 1}).url)
# print(cl1.get('api/v2/markets', {'market': 'btcbrl','price': '10','side': 'buy','tonce': 123,'volume': 1}).json())
# order = {
#   'total': 10,
#   'type': "bid",
#   'volume': 10
# }

# print(cl.get_public('/api/v2/order_markets', order).url)
# print(cl.get_public('/api/v2/order_markets', order).json())
# # print(cl1.get('api/v2/orders/multi', {'market': 'btcbrl','price': '10','side': 'buy','tonce': 123,'volume': 1}).url)



