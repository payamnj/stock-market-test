class Market(object):

	# Dictionary of Stock objects
	stocks = {}
	
	# define a dictioary for User interface actions
	# Keys of the dictionary are the expected user inputs
	# Values are the name of the method that should be executed in response to user action
	actions = {
		'T': 'submit_trade',
		'V': 'stock_volume_weightd_price',
		'G': 'geometric_mean',
		'U': 'update_price',
		'Q': 'quit'
	}
	# Function to add Stock to Market
	def add_stock(self, stock):
		if stock.symbol not in self.stocks:
			self.stocks[stock.symbol] = stock

	# Define response method for action (G) Get Market Geometric Mean
	# This method doesn't ask any more input from the user 
	# because the geometric mean is calculated for the whole market
	def geometric_mean(self):
		n = 1
		count = 0
		for symbol in self.stocks:
			count += 1
			n *= self.stocks[symbol].price

		gm = n**(float(1)/count)
		print('\nMarket Geometric mean: %f\n' % gm)
		return gm

	
	# Define response method for action (T) Record a Trade
	# This method ask the user to input Stock symbol, trade_type (sell/buy)
	# and quantity of shares and call the trade method of the requested stock
	def submit_trade(self):
		input_symbol = raw_input(
			'Which stock do you want to trade? (%s) ' % '/'.join(self.stocks))

		try:
			stock = self.stocks[input_symbol.upper()]
			type_input = ''
			
			# this while loop is just used to show the input message 
			# until user enters a correct action (buy/sell)
			while type_input.upper() not in ('BUY', 'SELL'):
				type_input = raw_input('Trade type? (BUY/SELL) ')

			quantity_entered = False
			while quantity_entered != True:
				try:
					quantity_input = input('Quantity of shares? ')
					quantity_entered = True
				except:
					print('\nPlease enter a numeric value!\n')

			# add a record to the instance's trades list
			stock.trade(type_input, quantity_input)
			self.overview()


		except KeyError:
			print('\n Invalid stock symbol! \n')
			self.submit_trade()

	# Define response method for action (V) Get Volume Weighted Stock Price
	# This method ask the user to input stock symbol and call the 
	# volume_weighted_price method of the requested stock.
	def stock_volume_weightd_price(self):
		input_symbol = raw_input(
			'Which Stock? (%s) ' % '/'.join(self.stocks))
		try:
			stock = self.stocks[input_symbol.upper()]
			print('\nVolume Weighted Stock Price (%s): %f' % (
				stock.symbol, stock.volume_weighted_price()))


		except KeyError:
			print('\n Invalid stock symbol! \n')
			self.stock_volume_weightd_price()

	# Define response method for action (U) update Price
	# this method ask the user to enter stock symbol and new price
	# and will call the set_price method of the requested stock
	def update_price(self):
		input_symbol = raw_input(
			'Which Stock? (%s) ' % '/'.join(self.stocks))
		try:
			stock = self.stocks[input_symbol.upper()]
			price_entered = False
			while price_entered == False:
				try:
					stock.set_price(input('\nEnter new price: '))
					self.overview()
					price_entered = True
				except:
					print('Please enter a numeric value')

		except KeyError:
			print('\n Invalid stock symbol! \n')
			self.update_price()
		



	# Define response method for action (Q) Quit
	def quit(self):
		print('Bye!')


	# Display User interface action options to the user
	def get_action(self):
		print('\nPlease select an Action:')
		action_input = raw_input(
			'(T) Record a trade | (V) Get Volume Weighted Stock Price | (U) Update Price | (G) Get Market Geometric Mean | (Q) Quit ')
		
		try:
			action_method = getattr(self, self.actions[action_input.upper()])
			action_method()
			if action_input.upper() != 'Q':
				self.get_action()

		except KeyError:
			print('\nInvalid Action!\n')
			self.get_action()

	# This method will display an overview of the stock objects with
	# their price, dividend yield and P/E ratio
	def overview(self):
		
		for stock in self.stocks:
			print('\n---------------------------------------------------\n%s' % stock)
			print('Price: %f\nDividend Yield: %f\nP/E Ratio: %f\n' % (
				self.stocks[stock].price,
				self.stocks[stock].get_dividend_yield(),
				self.stocks[stock].get_pe_ratio()))
			if len(self.stocks[stock].trades):
				print('Trades:')
				for trade in self.stocks[stock].trades:
					print('    %d shares | %s | traded price: %f | %s' % (
						trade['quantity'], trade['type'],
						trade['traded_price'], trade['timestamp']))

