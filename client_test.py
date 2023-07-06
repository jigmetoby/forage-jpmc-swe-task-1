import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
      for quote in quotes:
        stock, top_bid_price, top_ask_price, stock_price_based_on_formula = getDataPoint(quote)
        self.assertEqual(stock, quote['stock'])
        self.assertEqual(top_bid_price, quote['top_bid']['price'])
        self.assertEqual(top_ask_price, quote['top_ask']['price'])
        self.assertEqual(stock_price_based_on_formula, (quote['top_bid']['price'] + quote['top_ask']['price']) / 2)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      stock, top_bid_price, top_ask_price, stock_price_based_on_formula = getDataPoint(quote)
      self.assertEqual(stock, quote['stock'])
      self.assertEqual(top_bid_price, quote['top_bid']['price'])
      self.assertEqual(top_ask_price, quote['top_ask']['price'])
      self.assertEqual(stock_price_based_on_formula, (quote['top_bid']['price'] + quote['top_ask']['price']) / 2)




  """ ------------ Add more unit tests ------------ """
    def test_getRatio(self):
    # Test cases for getRatio
    # Test cases for getRatio
        price_a = 100
        price_b = 50
        expected_ratio = 2

        ratio = getRatio(price_a, price_b)
        self.assertEqual(ratio, expected_ratio)
    pass


if __name__ == '__main__':
    unittest.main()
