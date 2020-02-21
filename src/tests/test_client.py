import unittest
import json
from nose.tools import assert_is_none, assert_list_equal
from mock import patch, Mock

from omnitradeClient.client import Client

OMNITRADE_URL = 'https://omnitrade.io'
class TestClientMethods(unittest.TestCase):
    
    def test_get_public_valid_request(self):
        public_client = Client()
        market_path = '/api/v2/markets'
        markets = [{"id": "btcbrl", "name": "BTC/BRL"}, {"id": "ltcbrl", "name": "LTC/BRL"}, {"id": "bchbrl", "name": "BCH/BRL"}, {"id": "btgbrl", "name": "BTG/BRL"}, {"id": "ethbrl", "name": "ETH/BRL"}, {"id": "dashbrl", "name": "DASH/BRL"}, {"id": "dcrbrl", "name": "DCR/BRL"}, {"id": "ltcbtc", "name": "LTC/BTC"}, {"id": "bchbtc", "name": "BCH/BTC"}, {"id": "btgbtc", "name": "BTG/BTC"}, {"id": "ethbtc", "name": "ETH/BTC"}, {"id": "dashbtc", "name": "DASH/BTC"}, {"id": "dcrbtc", "name": "DCR/BTC"}, {"id": "ltceth", "name": "LTC/ETH"}, {"id": "bcheth", "name": "BCH/ETH"}, {"id": "btgeth", "name": "BTG/ETH"}, {"id": "dasheth", "name": "DASH/ETH"}, {"id": "dcreth", "name": "DCR/ETH"}, {"id": "xrpbrl", "name": "XRP/BRL"}, {"id": "xrpbtc", "name": "XRP/BTC"}, {"id": "xrpeth", "name": "XRP/ETH"}, {"id": "mftbrl", "name": "MFT/BRL"}, {"id": "mftbtc", "name": "MFT/BTC"}, {"id": "mfteth", "name": "MFT/ETH"}, {"id": "btcusdc", "name": "BTC/USDC"}, {"id": "ltcusdc", "name": "LTC/USDC"}, {"id": "bchusdc", "name": "BCH/USDC"}, {"id": "btgusdc", "name": "BTG/USDC"}, {"id": "ethusdc", "name": "ETH/USDC"}, {"id": "dashusdc", "name": "DASH/USDC"}, {"id": "dcrusdc", "name": "DCR/USDC"}, {"id": "xrpusdc", "name": "XRP/USDC"}, {"id": "bnbbtc", "name": "BNB/BTC"}, {"id": "bnbusdc", "name": "BNB/USDC"}]

        response = public_client.get_public(market_path)

        self.assertEqual(response.json(), markets)

    def test_post_request(self):
        access_key = 'FUkESEYRJmO42MfqXcgJfm73GfIMw61qogExtcX7' #TODO improve this requests tests

        client = Client({'access_key': access_key,'secret_key': '123456'})
        response = client.post('/api/v2/orders/clear', {'side': 'sell' })

        self.assertEqual(response.status_code, 201)

    def test_post_request(self):
        access_key = 'FUkESEYRJmO42MfqXcgJfm73GfIMw61qogExtcX7' #TODO improve this requests tests

        client = Client({'access_key': access_key,'secret_key': '123456'})
        response = client.get('/api/v2/order', {'id': 1 })
        self.assertEqual(response.status_code, 404)
