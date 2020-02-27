import unittest
import json
from mock import patch

from src.omnitradeClient.client import Client

OMNITRADE_URL = 'https://omnitrade.io'
class TestClientMethods(unittest.TestCase):
    @patch('src.omnitradeClient.client.requests.get')
    def test_get_public_valid_request(self, mock_get):
        public_client = Client()
        market_path = '/api/v2/markets'
        markets = [{"id": "btcbrl", "name": "BTC/BRL"}, {"id": "ltcbrl", "name": "LTC/BRL"}, {"id": "bchbrl", "name": "BCH/BRL"}]

        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = markets

        response = public_client.get_public(market_path)

        self.assertEqual(response.json(), markets)
        self.assertEqual(response.status_code, 200)


    @patch('src.omnitradeClient.client.requests.get')
    def test_get_private_valid_request(self, mock_get):
        client = Client(access_key='123456', secret_key='123456')
        order_path = '/api/v2/markets'
        orders = [{'id': 1917314, 'side': 'buy', 'ord_type': 'limit', 'price': '40000.0', 'avg_price': '40000.0', 'state': 'wait', 'market': 'btcbrl', 'created_at': '2019-08-21T17:06:11-03:00', 'volume': '0.5', 'remaining_volume': '0.4975', 'executed_volume': '0.0025', 'trades_count': 1}, {'id': 1917316, 'side': 'sell', 'ord_type': 'limit', 'price': '45000.0', 'avg_price': '45000.0', 'state': 'wait', 'market': 'btcbrl', 'created_at': '2019-08-21T17:07:32-03:00', 'volume': '0.6', 'remaining_volume': '0.597', 'executed_volume': '0.003', 'trades_count': 1}]

        mock_get.return_value.json.return_value = orders

        response = client.get('api/v2/markets', market = 'btcbrl',price = '10',side = 'buy',tonce = 123,volume = 1)

        self.assertEqual(response.json(), orders)

    @patch('src.omnitradeClient.client.requests.post')
    def test_post_request(self, mock_post):
        order = [{'id': 1917316, 'side': 'sell', 'ord_type': 'limit', 'price': '45000.0', 'avg_price': '45000.0', 'state': 'wait', 'market': 'btcbrl', 'created_at': '2019-08-21T17:07:32-03:00', 'volume': '0.6', 'remaining_volume': '0.597', 'executed_volume': '0.003', 'trades_count': 1}]

        client = Client(access_key = '123456', secret_key = '123456')

        mock_post.return_value.json.return_value = order

        response = client.post('/api/v2/orders/clear', side = 'sell')

        self.assertEqual(response.json(), order)

