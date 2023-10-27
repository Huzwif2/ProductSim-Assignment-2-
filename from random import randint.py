from random import randint

class Product():

    def __init__(self, code, name, stock, price, cost, units):
        self.code = code
        self.name = name
        self.stock = stock
        self.price = price
        self.cost = cost
        self.units = units

    def sales_sim(self):
        sold = randint(self.units - 10, self.units + 10)
        if sold < 0:
            sold = 0
        return sold
    
    def generate_stock_statement(self, months):
        total_profit = 0
        # Creating list for stock statement
        stock_statement = []
        for month in range(months):
            sold = self.sales_sim()
            units = self.units
            self.stock = max(0, self.stock + self.units - sold)
            profit = (sold * self.price) - (units * self.cost)
            total_profit += profit
            stock_statement.append(f"\nMonth {month + 1}:\n    Units Sold: {sold}\n    Stock Level: {self.stock}\n    Profit/Loss: {profit}")
        return stock_statement, total_profit
    

def main():
    print("Welcome to Programming Principles Sample Product Inventory")
    try:
        code = int(input("Please enter the Product Code (Between 100 to 1000): "))
        name = input("Please enter the Product Name: ")
        stock = int(input("Please enter the Current Stock: "))
        price = float(input("Please enter the Product Sale Price: "))
        cost = float(input("Please enter the Product Manufacture Cost: "))
        units = int(input("Please enter Estimated Monthly Production: "))

        # Validate user input return error and restart function upon type error
        if 100 <= code <= 1000 and stock > 0 and price > 0 and cost > 0 and units > 0:
            print("\n*******Programming Principles Sample Stock Statement******")
            print("\nProduct code: ", code)
            print("Product Name: ", name)
            print("\nSale Price: ", price," CAD")
            print("Manufacture Cost: ", cost," CAD")
            print("Monthly Production: ", units, "Units (Approximately)")
            
            product = Product(code, name, stock, price, cost, units)
            months = 12
            stock_statement, total_profit = product.generate_stock_statement(months)
            
            for statement in stock_statement:
                print(statement)

            print(f"\nTotal Net Profit/Loss: {total_profit} CAD")

        else:
            print("One or more of the values entered is incorrect. Please try again.")
            main()
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        main()

    print(Product.sales_sim)


if __name__ == "__main__":
    main()