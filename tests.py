import unittest
from classes.stocks import Stock
from classes.markets import Market

sample_common_stock = {
        'type': 'common', 
        'last_dividend': 8,
        'par_value': 100
    }

sample_preffered_stock = {
    'type': 'preferred',
    'last_dividend': 8,
    'fixed_dividend': 0.02,
    'par_value': 100
}

class TestStockObject(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        self.common_stock = Stock(
            'COM', sample_common_stock)

        self.preffered_stock = Stock(
            'PER', sample_preffered_stock)

        super(TestStockObject, self).__init__(*args, **kwargs)

    def test_setprice(self):
        self.common_stock.set_price(25)
        self.assertEqual(self.common_stock.price, 25)

    def test_dividend_yield(self):
        self.common_stock.set_price(64)
        self.preffered_stock.set_price(64)

        self.assertEqual(
            self.common_stock.get_dividend_yield(),
            0.125)

        self.assertEqual(
            self.preffered_stock.get_dividend_yield(),
            0.03125)

    def test_pe_ratio(self):
        self.common_stock.set_price(64)
        self.preffered_stock.set_price(64)

        self.assertEqual(
            self.common_stock.get_pe_ratio(),
            512)

        self.assertEqual(
            self.preffered_stock.get_pe_ratio(),
            2048)

    def test_volume_weighted_price(self):
        self.common_stock.set_price(49)
        self.common_stock.trade('BUY', 30)
        self.common_stock.set_price(75)
        self.common_stock.trade('BUY', 20)

        self.assertEqual(len(self.common_stock.trades), 2)

        self.assertEqual(
            self.common_stock.volume_weighted_price(),
            59.4)

class TestMarketObject(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        self.common_stock = Stock(
            'COM', sample_common_stock)
        self.common_stock.set_price(25)
        self.preffered_stock = Stock(
            'PER', sample_preffered_stock)
        self.preffered_stock.set_price(34)

        self.market = Market()

        super(TestMarketObject, self).__init__(*args, **kwargs)

    def test_add_stock(self):
        self.assertNotIn('COM', self.market.stocks)
        self.market.add_stock(self.common_stock)
        self.assertIn('COM', self.market.stocks)

    def test_geometric_mean(self):
        self.market.add_stock(self.common_stock)
        self.assertEqual(self.market.geometric_mean(), 25)
        self.market.add_stock(self.preffered_stock)
        self.assertEqual(
            self.market.geometric_mean(),
            (25*34)**0.5)


if __name__ == '__main__':
    unittest.main()