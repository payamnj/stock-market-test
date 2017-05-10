import os
from classes.stocks import Stock
from classes.markets import Market

sample_stocks_data = {
	'TEA': {
		'type': 'common', 
		'last_dividend': 0,
		'par_value': 100
	},
	'POP': {
		'type': 'common',
		'last_dividend': 8,
		'par_value': 100
	},
	'ALE': {
		'type': 'common',
		'last_dividend': 23,
		'par_value': 60
	},
	'GIN': {
		'type': 'preferred',
		'last_dividend': 8,
		'fixed_dividend': 0.02,
		'par_value': 100
	},
	'JOE': {
		'type': 'common',
		'last_dividend': 13,
		'par_value': 250
	}
}

# Create a new Market 
gbce = Market()

# Iterate the sample data to create the initial stock objects
for stock in sample_stocks_data:

	stock_object = Stock(stock, sample_stocks_data[stock])
	entered = False
	
	while entered == False:
		try:
			# Ask user for the initial prices for sample stocks
			price = input("\nPlease enter the price for %s: " % stock_object.symbol)
			stock_object.set_price(price)
			entered = True
		except:
			print('Please enter a numeric value.')
			pass
	
	# Add the newly created stock object to the GBCE market
	gbce.add_stock(stock_object)


# Print an Overview from market stoks to display price, dividend yield and P/E ratio
gbce.overview()


# call the get_action method of the GBCE market object
# This method displays all the available options that user can interact with the code
gbce.get_action()


