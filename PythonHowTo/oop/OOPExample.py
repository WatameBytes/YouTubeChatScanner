from carFile import CarClass

car_1 = CarClass("Chevy", "Corvette", 2021, "blue")

print(car_1.color)
car_1.stop()
print(car_1.wheels)
car_1.wheels = 29
print(car_1.wheels)

from product import Product

george_foreman = Product("Fit Medium Health Grill", "39.99", "George Foreman")

george_foreman.show_price()