# Capstone project IV - Submitted by Bhavya Patteeswaran
# ========The beginning of the class==========
class Shoe:
    # Initialise the country,code,product,cost and quantity attributes.
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # get_cost() method will return the cost of shoes.
    def get_cost(self):
        return float(self.cost)  # Return float value

    # get_quantity() method will return the quantity of shoes.
    def get_quantity(self):
        return int(self.quantity)  # Return int value

    # get_code() method will return the code of shoes which will be used to search the code in shoe_list
    def get_code(self):
        return self.code

    # returns string representation of a class.
    def __str__(self):
        return f"Country: {self.country}\nCode: {self.code}\nProduct: {self.product}\nCost: R{float(self.cost):.2f}\nQuantity: {self.quantity}"


# =============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []


# ==========Functions outside the class==============
# Function 1 - Read the inventory.txt file and create shoes object in the list. Skip the first line from file.
def read_shoes_data():
    try:
        with open("inventory.txt", "r") as inventory:
            next(inventory)  # Skip the first line
            for line in inventory:
                line_list = line.replace("\n", "").split(",")  # Splitting the line to a list
                # Creating shoes object from getting list indexes
                shoes = Shoe(
                    country=line_list[0],
                    code=line_list[1],
                    product=line_list[2],
                    cost=line_list[3],
                    quantity=line_list[4])
                shoe_list.append(shoes)
    except FileNotFoundError:
        print("File not found.")
        exit()


# Capture the data from user and append on the shoe_list and inventory text file.
def capture_shoes():
    country = input("Country: ")
    code = input("Code: ").upper()
    product = input("Product: ")
    # Error handling for cost and quantity on datatype value error.
    while True:
        try:
            cost = float(input("Cost: "))
            quantity = int(input("Quantity: "))
            break
        except ValueError:
            print("Enter valid number value")
    # Creating shoes object and append to the shoe_list and inventory text file.
    shoes = Shoe(
        country=country,
        code=code,
        product=product,
        cost=cost,
        quantity=quantity
    )
    shoe_list.append(shoes)
    with open("inventory.txt", "a") as inventory:
        inventory.write(f"\n{country},{code},{product},{cost},{quantity}")


# Iterate the shoes list and print the details returned from __str__ function.
def view_all():
    for shoes in shoe_list:
        print()
        print(shoes)


# Find the lowest quantity of shoe object and ask user input to add and update in file and list.
def re_stock():
    lowest_quan = shoe_list[0].get_quantity()  # Set the lowest value to first item on list
    for index, shoe in enumerate(shoe_list):
        if (shoe.get_quantity()) < lowest_quan:
            lowest_quan = (shoe.get_quantity())  # Set new lowest quantity
            lowest_shoe = shoe  # Set new lowest shoe
            i = index
    print("Shoe with lowest quantity:")
    print(lowest_shoe)

    while True:
        user_input = input("Do you want to update the stock of shoes (y/n): ").lower()
        if user_input == "y":
            shoe_list[i].quantity = input("New Quantity: ")  # Set new quantity by using index from above for loop
            with open("inventory.txt", "w") as inventory:
                inventory.write("Country,Code,Product,Cost,Quantity")
                # Writing each line to file again
                for shoe in shoe_list:
                    inventory.write(f"\n{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}")
            print("Low quantity shoe is restocked in inventory.")
            break

        elif user_input == "n":
            print("Not required to restock.")
            break

        else:
            print("Invalid input please try again.")


# Search shoe from list using shoe code and return the object to print.
def search_shoe():
    search_input = input("Code to search: ").upper()  # eg SKU44386
    for shoe in shoe_list:
        if shoe.get_code() == search_input:
            return shoe
        else:
            return "Shoe not found"


# Calculate the total value for each item - value = cost * quantity and print for all shoes.
def value_per_item():
    for shoe in shoe_list:
        print()
        print(shoe)
        print("--Total value of this item--")
        print("R{:.2f}".format(shoe.get_cost() * shoe.get_quantity()))


# Find the highest quantity and print the shoe for sale.
def highest_qty():
    highest_quan = shoe_list[0].get_quantity()  # Set the highest value to the first item on the list
    for shoe in shoe_list:
        if (shoe.get_quantity()) > highest_quan:
            highest_quan = (shoe.get_quantity())
            new_shoe = shoe

    print("Shoe is on sale!!")
    print(new_shoe)
    # While loop to enter the discount logic on the high quantity shoes for sales. Extra logic
    while True:
        try:
            sale_percentage = int(input("Enter discount percentage: "))
            percentage_amount = 1 - (sale_percentage / 100)
            print("The sale price is")
            print("R{:.2f}".format(new_shoe.get_cost() * percentage_amount))
            break
        except ValueError:
            print("Enter the valid number.")


# =========Main Menu=============
def main():
    # Initialise by calling the method read_shoes_data() first
    read_shoes_data()
    print("'Welcome to Nike warehouse inventory'")
    while True:
        user_choice = input('''\nSelect one of the following Options below by entering number 1-7:
1. Log shoe
2. View current stock
3. Re-stock a shoe
4. Search for an item
5. Value of each item
6. Highest value item
7. quit
: ''')

        if user_choice == "1":
            capture_shoes()

        elif user_choice == "2":
            view_all()

        elif user_choice == "3":
            re_stock()

        elif user_choice == "4":
            print(search_shoe())

        elif user_choice == "5":
            value_per_item()

        elif user_choice == "6":
            highest_qty()

        elif user_choice == "7":
            print("Goodbye")
            break

        else:
            print("Please enter a valid value")


# Calling the main function
if __name__ == "__main__":
    main()
