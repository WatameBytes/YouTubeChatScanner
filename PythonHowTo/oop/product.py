class Product:
	def __init__(self, name, price, brand):
		self.name = name
		self.price = price
		self.brand = brand

	def show_price(self):
		print("The price of {} is ${}.".format(self.name, self.price))