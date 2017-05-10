import datetime

class Stock(object):

	def __init__(self, symbol, values):
		
		# List of the trades for the stock instance
		self.trades = []
		setattr(self, 'symbol', symbol)
		
		for key in values:
			setattr(self, key, values[key])

	def __str__(self):
		return self.symbol

	def __unicode__(self):
		return self.symbol

	# 
	def set_price(self, price):
		self.price = price

	# dividend Yield Calculator Method
	def get_dividend_yield(self):
		try:
			# Check for the stock type to select the proper equation
			if self.type == 'common':
				return float(self.last_dividend) / self.price
			elif self.type == 'preferred':
				return float(self.fixed_dividend) * self.par_value / self.price
			
		except Exception, e:
			print(e)
			return None

	# P/E Radtio Calculator MEthod
	def get_pe_ratio(self):
		dividend_yield =  self.get_dividend_yield()
		if dividend_yield:
			return float(self.price) / dividend_yield
		else:
			return 0


	# Trade recorder
	def trade(self, type, quantity):
		self.trades.append({
			'timestamp': datetime.datetime.now(),
			'type': type,
			'quantity': quantity,
			'traded_price': self.price
			})


	# function to calculate Volume Weighted stock price
	# Based on trades in past 15 minutes
	def volume_weighted_price(self):
		from_time = datetime.datetime.now() - datetime.timedelta(minutes=15)
		sum_value = 0
		sum_quantity = 0 
		for trade in self.trades:
			if trade['timestamp'] > from_time:
				sum_value += trade['quantity'] * trade['traded_price']
				sum_quantity += trade['quantity']

		try:
			return float(sum_value) / sum_quantity
		except Exception, e:
			return 0
			print(e)