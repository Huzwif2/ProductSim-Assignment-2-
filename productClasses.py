from random import randint

class Product_Program():

    def __init__(self, code, name, stock, price, cost, units):
        self.code = code
        self.name = name
        self.stock = stock
        self.price = price
        self.cost = cost
        self.manufactured_units = units

def get_user_info():
    try:
        code = int(input("Please enter the Product Code (Between 100 to 1000): "))
        name = input("Please enter the Product Name: ")
        stock = int(input("Please enter the Current Stock: "))
        price = float(input("Please enter the Product Sale Price: "))
        cost = float(input("Please enter the Product Manufacture Cost: "))
        units = int(input("Please enter Estimated Monthly Production: "))

        # Validate user input
        if 100 <= code <= 1000 and stock > 0 and price > 0 and cost > 0:
            print("Oki")
            print(code, name, stock, price, cost, units)
        else:
            print("One or more of the values entered is incorrect. Please try again.")
            get_user_info()
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        get_user_info()
        
get_user_info()